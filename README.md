# 📄 IntelliDocs AI 🤖
### LIVE DEMO:- https://intellidocs-mxxzhue7snt2aldcbqbefn.streamlit.app/

### Overview 🌟

IntelliDocs AI is a robust, submission-ready internship project designed to extract insights from PDF documents using **Retrieval-Augmented Generation (RAG)**. This solution allows users to interact with complex documents, transforming static text into an accessible, data-driven conversational experience. 💡

### Problem 🚩

Professionals and students often face the challenge of scanning through lengthy, dense documentation to find specific information. Manually searching for details is time-consuming, prone to error, and inefficient, especially when dealing with massive datasets or technical reports. 📉

### Solution 🚀

This project leverages advanced Large Language Models (LLMs) and Vector Databases to provide an intelligent document-querying interface. Key highlights include:

* 🔹 **Intelligent Retrieval:** Uses semantic search to find precise document sections. 🎯
* 🔹 **Persistent Storage:** Utilizes ChromaDB for efficient, on-disk document indexing. 💾
* 🔹 **Scalability:** Handles large PDF files without memory bottlenecks. ⚖️
* 🔹 **High-Performance Architecture:** Streamlined pipeline for fast, accurate response generation. ⚡

### Tech Stack 🛠️

* 🐍 **Python:** Core development language.
* 🦜 **LangChain:** Framework for building the RAG pipeline.
* 🧠 **Google Gemini:** Advanced LLM for natural language processing.
* 📊 **ChromaDB:** Persistent vector database for document storage.
* 🌐 **Streamlit:** Framework for the responsive web interface.

### Dataset & Capability 🧠

This system supports any standard PDF file. It breaks down documents into contextually relevant "chunks" using `RecursiveCharacterTextSplitter`, ensuring that the AI has the most accurate information to generate answers based on:

* 📄 **Document content extraction**
* 🔍 **Context-aware semantic searching**
* 💡 **Precise answer generation** using Gemini's reasoning

### Objectives 🏆

* 🏆 Build a production-ready RAG application for document analysis.
* 📌 Minimize "hallucinations" by grounding model responses in provided document context.
* 🚀 Optimize retrieval latency for a better user experience.

### How to Run Locally 💻

1. **Prerequisites:** Python 3.11+
2. **Setup:**
```bash
git clone https://github.com/AaineeSinha/INTELLIDOCS
cd INTELLIDOCS
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

```


3. **Execution:**
```bash
streamlit run app.py

```



### Future Scope 🔮

* 🚀 Support for multi-format document uploads (Docx, Txt, Images).
* 📊 Integration of persistent user chat history using a database like PostgreSQL.
* 🧠 Implement agentic workflows for summarizing complex multi-document sets.

Happy querying! 📄✨ Enjoy exploring your documents with data-driven precision. 🥂
