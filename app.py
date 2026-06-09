import streamlit as st
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import ui_utils
import warnings

# --- Initialization ---
warnings.filterwarnings("ignore")
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")

st.set_page_config(page_title="IntelliDocs AI", layout="wide")
ui_utils.inject_custom_css()  # type: ignore

# Session State Management
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "vector_store" not in st.session_state: st.session_state.vector_store = None
if "processed_filename" not in st.session_state: st.session_state.processed_filename = None

# --- Sidebar Controls ---
with st.sidebar:
    st.header("Workspace Control")
    uploaded_file = st.file_uploader("Upload PDF Document", type=["pdf"])
    process_button = st.button("Analyze Document")
    ui_utils.render_sidebar_status(st.session_state.vector_store, st.session_state.processed_filename)  # type: ignore

# --- Document Processing Pipeline ---
if uploaded_file and process_button:
    with st.spinner("Indexing PDF..."):
        try:
            # 1. Extract Text
            pdf_reader = PdfReader(uploaded_file)
            raw_text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
            
            # 2. Chunking
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_text(raw_text)
            
            # 3. Embedding (Using current stable model: gemini-embedding-2-preview)
            embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
            
            # 4. Persistent Storage (RAM-efficient)
            st.session_state.vector_store = Chroma.from_texts(
                chunks, 
                embeddings, 
                persist_directory="./chroma_db"
            )
            st.session_state.processed_filename = uploaded_file.name
            st.rerun()
        except Exception as e:
            st.error(f"Processing Error: {e}")

# --- Chat Interface ---
st.markdown("<h1 class='main-title'>IntelliDocs AI</h1>", unsafe_allow_html=True)  # type: ignore

for role, message in st.session_state.chat_history:
    with st.chat_message(role): st.write(message)

if user_question := st.chat_input("Ask a question about your PDF..."):
    st.session_state.chat_history.append(("user", user_question))
    with st.chat_message("user"): st.write(user_question)
    
    if st.session_state.vector_store:
        with st.spinner("Thinking..."):
            # Using current stable model: gemini-2.5-flash
            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
            
            retriever = st.session_state.vector_store.as_retriever()
            prompt = ChatPromptTemplate.from_messages([("system", "Context: {context}"), ("human", "{input}")])
            
            chain = (
                {"context": retriever | (lambda d: "\n\n".join([x.page_content for x in d])), "input": RunnablePassthrough()} 
                | prompt | llm | StrOutputParser()
            )
            
            answer = chain.invoke(user_question)
            with st.chat_message("assistant"): st.write(answer)
            st.session_state.chat_history.append(("assistant", answer))
    else:
        st.warning("Please upload and analyze a PDF first.")