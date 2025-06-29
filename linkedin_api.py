import os
import requests
from dotenv import load_dotenv
from logger import get_logger
from exceptions import LinkedInAPIError

# # Load environment variables from .env file
load_dotenv(dotenv_path="./.env")
logger = get_logger(__name__)


def post_to_linkedin(post_text, access_token=None, user_urn=None):
    if not post_text:
        raise ValueError("Post text must not be empty.")

    if not user_urn:
        user_urn = os.getenv("LINKEDIN_USER_URN")   # Use Get UserInfo LinkedIn API call. Check Postman collection under ./etc/postman.
    if not user_urn:
        raise LinkedInAPIError("Missing LinkedIn USER_URN in environment variables.")

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    # Refer https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin
    payload = {
        "author": f"urn:li:person:{user_urn}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": post_text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    try:
        response = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=payload)
        logger.debug(f"LinkedIn Post Response: {response.status_code} - {response.text}")

        if response.status_code == 201:
            return True, "✅ Successfully posted to LinkedIn!"
        else:
            raise LinkedInAPIError(f"LinkedIn API Error [{response.status_code}]: {response.text}")

    except requests.exceptions.RequestException as e:
        logger.exception("Request to LinkedIn API failed.")
        return False, f"❌ LinkedIn API request error: {e}"
    except LinkedInAPIError as e:
        logger.error(str(e))
        return False, f"❌ {str(e)}"
    except Exception as e:
        logger.exception("Unexpected error during LinkedIn post.")
        return False, f"❌ Unexpected error: {e}"
