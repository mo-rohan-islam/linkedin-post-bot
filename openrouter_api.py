import os
import requests
from logger import get_logger
from dotenv import load_dotenv
from jinja2 import Template

# # Load environment variables from .env file
load_dotenv(dotenv_path="./.env")
logger = get_logger(__name__)


API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
AI_MODEL = "meta-llama/llama-3.3-70b-instruct"
TEMPLATE_FILE = "prompt_template.txt"


def render_prompt(template_file, topic, context):
    with open(template_file, "r", encoding="utf-8") as file:
        template_str = file.read()
    template = Template(template_str)
    prompt = template.render(topic=topic, context=context)
    return prompt

def generate_post(topic, context):
    prompt = render_prompt(TEMPLATE_FILE, topic, context or "N/A")

    logger.debug(f'Formatted prompt: {prompt}')
    logger.debug(f'API KEY: {API_KEY}')

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": f'{AI_MODEL}',
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        logger.debug(f"Sending request to OpenRouter for topic: {topic}")
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        logger.debug(f"Response Status Code: {response.status_code}")
        logger.debug(f"Response Text: {response.text.strip()}")

        response.raise_for_status()
        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            logger.warning("Unexpected response structure: %s", data)
            raise Exception(f"API error: {data}")

    except Exception as e:
        logger.exception("Error during API call:", e)
        return f"❌ Error: Could not generate post.\n\nDetails:\n{e}"
