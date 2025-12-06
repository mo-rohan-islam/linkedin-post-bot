import pyperclip
import streamlit as st
from dotenv import load_dotenv
from openrouter_api import generate_post
from logger import get_logger
from formatter import format_model_output
from linkedin_api import post_to_linkedin

# Load environment variables from .env file
# load_dotenv(dotenv_path="./.env")
logger = get_logger(__name__)

st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

# Check login state
if "access_token" not in st.session_state or not st.session_state["access_token"]:
    st.title("📢 AI-Generated LinkedIn Post")
    st.warning("🔒 Please log in via LinkedIn first.")
    st.switch_page("Login.py")

# Authenticated view
st.title("📢 AI-Generated LinkedIn Post")

topic = st.text_input("Enter the trending topic", placeholder="e.g., LangChain, Vector Databases")
context = st.text_area("Optional context", placeholder="e.g., Used in AI apps, RAG pipelines, etc.")

# Generate post
if st.button("Generate LinkedIn Post", use_container_width=True):
    if topic.strip():
        with st.spinner("Generating..."):
            logger.info(f"Generating post for topic: {topic}")
            raw_post = generate_post(topic.strip(), context.strip())
            formatted_post = format_model_output(raw_post)
            st.session_state["post_text"] = formatted_post
            st.success("Here’s your post!")
    else:
        st.error("Please enter a topic.")

# Display generated post and action buttons only if post exists
if "post_text" in st.session_state and st.session_state["post_text"]:
    # Use key="post_text" to bind to session state and allow editing
    st.text_area("Generated LinkedIn Post", key="post_text", height=350)

    # Create 2 columns for side-by-side buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        # Use lambda to copy the current value from session state
        st.button("📋 Copy to clipboard", use_container_width=True, on_click=lambda: pyperclip.copy(st.session_state["post_text"]))
    with col2:
        if st.button("🚀 Post to LinkedIn", use_container_width=True):
            success, message = post_to_linkedin(
                post_text=st.session_state["post_text"],
                access_token=st.session_state["access_token"]
            )
            st.success(message)
