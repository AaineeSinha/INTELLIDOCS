import streamlit as st

def inject_custom_css():
    """Injects high-end CSS for a clean, SaaS-like dashboard."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');
        
        /* Global Background */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #0b0e14;
            color: #e6edf3;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #161b22;
            border-right: 1px solid #30363d;
        }

        /* Main Header Styling */
        .main-title {
            font-size: 2.8rem;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 1.5rem;
        }

        /* Status Module Cards */
        .status-box {
            background: #21262d;
            border: 1px solid #30363d;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        /* Clean up interface */
        #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)  # type: ignore

def render_sidebar_status(vector_store, filename):
    """Renders the sidebar status indicator."""
    st.markdown("<h3 style='font-size: 1rem; color: #8b949e;'>SYSTEM STATUS</h3>", unsafe_allow_html=True) # type: ignore
    
    if vector_store:
        st.markdown(f"""
        <div class='status-box' style='border-left: 4px solid #238636;'>
            <p style='margin:0; font-weight:600; color:#3fb950;'>● ACTIVE</p>
            <p style='margin:0; font-size: 0.85rem;'>{filename}</p>
        </div>
        """, unsafe_allow_html=True)  # type: ignore
    else:
        st.markdown("""
        <div class='status-box' style='border-left: 4px solid #d29922;'>
            <p style='margin:0; font-weight:600; color:#d29922;'>○ STANDBY</p>
            <p style='margin:0; font-size: 0.85rem;'>Awaiting document</p>
        </div>
        """, unsafe_allow_html=True)  # type: ignore