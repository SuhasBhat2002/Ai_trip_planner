import streamlit as st
import requests
import datetime

BASE_URL = "http://localhost:8000"  # Backend endpoint

# Streamlit page config (no globe icon)
st.set_page_config(
    page_title="Travel Planner Agentic Application",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Inject custom CSS for white background and handwritten text
st.markdown(
    """
    <style>
    /* Import a handwritten-style font */
    @import url('https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap');

    html, body, [class*="css"] {
        background-color: white !important;
        font-family: 'Indie Flower', cursive !important;
        color: #333333;
    }

    /* Handwritten-style headings */
    h1, h2, h3, h4 {
        font-family: 'Indie Flower', cursive;
        font-weight: normal;
        color: #2a2a2a;
        text-shadow: 1px 1px 0px rgba(0,0,0,0.1);
    }

    /* Input styling */
    .stTextInput > div > div > input {
        border: 2px dashed #555;
        border-radius: 12px;
        padding: 12px;
        font-family: 'Indie Flower', cursive;
        font-size: 18px;
    }

    /* Button styling */
    .stButton button {
        background-color: #666 !important;
        color: #fff !important;
        font-family: 'Indie Flower', cursive;
        font-size: 18px;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6em 1.4em !important;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    /* Footer note styling */
    .stMarkdown p {
        font-size: 16px;
        line-height: 1.4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title (handwritten)
st.title("🌍 Travel Planner Agentic Application")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Prompt header
st.header("How can I help you plan your next adventure?")

# Input form
with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("Your question:", placeholder="e.g. Plan a trip to Bali for 7 days")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        with st.spinner("Let me think…"):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")
            st.markdown(f"""
**📝 Generated:** {datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')}  
**✍️ Created by:** Suhas's Travel Agent Buddy

---

{answer}

---

*This travel plan was generated by AI. Please double‑check prices, hours, and requirements before you go!*
""")
        else:
            st.error("Bot failed to respond: " + response.text)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
