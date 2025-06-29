import os
import requests
import uuid
import urllib.parse
from dotenv import load_dotenv
from logger import get_logger
from exceptions import LinkedInAPIError

# # Load environment variables from .env file
load_dotenv(dotenv_path="./.env")
logger = get_logger(__name__)

CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
REDIRECT_URI = os.getenv("LINKEDIN_REDIRECT_URI")
SCOPE = "w_member_social"


if not CLIENT_ID or not CLIENT_SECRET or not REDIRECT_URI:
    raise LinkedInAPIError("Missing LinkedIn CLIENT_ID or CLIENT_SECRET or LINKEDIN_REDIRECT_URI in environment variables.")


def get_authorization_url():
    auth_code_url = "https://www.linkedin.com/oauth/v2/authorization"
    state = str(uuid.uuid4())  # Generates a random UUID

    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "state": state
    }
    return f"{auth_code_url}?{urllib.parse.urlencode(params)}"

def exchange_code_for_access_token(code: str):
    access_token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    try:
        response = requests.post(access_token_url, headers=headers, data=data)
        response.raise_for_status()

        access_token = response.json().get("access_token")
        if not access_token:
            raise LinkedInAPIError("Access token missing in LinkedIn response.")
        logger.debug("Successfully retrieved LinkedIn access token.")

        expires_in = response.json().get("expires_in")
        logger.info(f"✅ Access token received. Expires in {expires_in} seconds.")
        return access_token

    except requests.RequestException as e:
        logger.exception("❌ Failed to exchange code for access token.")
        raise LinkedInAPIError(f"Access token request failed: {e}")
    except Exception as e:
        logger.exception("Unexpected error while getting access token.")
        raise