import streamlit as st
from dotenv import load_dotenv
from linkedin_auth import get_authorization_url, exchange_code_for_access_token
from logger import get_logger

# Load environment variables from .env file
# load_dotenv(dotenv_path="./.env")   # Should only be present in the App.py but exists here for being the entrypoint
logger = get_logger(__name__)

st.set_page_config(page_title="LinkedIn Login", layout="centered")

st.title("🔐 LinkedIn Auth Integration")

# Same code used to handle LinkedIn callback
query_params = st.query_params
auth_code = query_params.get("code")
logger.debug(f"Auth code: {auth_code}")

if auth_code:
    # Handle callback
    with st.spinner("Exchanging code for access token..."):
        token = exchange_code_for_access_token(auth_code)
        if token:
            st.session_state["access_token"] = token
            st.success("✅ Logged in successfully with LinkedIn!")

            # redirect to app
            st.switch_page("pages/App.py")
        else:
            st.error("❌ Failed to authenticate. Try again.")
else:
    # No code yet, show login screen
    if "access_token" not in st.session_state:
        st.markdown("### 👤 Login with LinkedIn to continue")
        login_url = get_authorization_url()
        # st.markdown(f"[🔗 Click here to Login with LinkedIn]({login_url})")
        st.markdown(
            f'<a href="{login_url}" target="_self">🔗 Click here to Login with LinkedIn</a>',
            unsafe_allow_html=True
        )
    else:   # TODO: Code not being used. Fix the logic
        st.success("✅ Already authenticated with LinkedIn!")
        # st.markdown("Continue to [Generate Posts ➡️](../App.py)")
        # st.markdown("Continue to [Generate Posts ➡️](http://localhost:8501/App)")
        st.markdown(
            '<a href="http://localhost:8501/App" target="_self">Continue to [Generate Posts ➡️</a>',
            unsafe_allow_html=True
        )

