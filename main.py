import requests
import json
import os
from dotenv import load_dotenv
from loguru import logger


load_dotenv()
from datetime import datetime
from zoneinfo import ZoneInfo

logger.info("Environment variables loaded")
logger.info(f"Starting Engine Worker for flow: {os.getenv('LANGFLOW_URL')}")

url = os.getenv('LANGFLOW_URL')
logger.info(f"LANGFLOW_URL: {url}")

headers = {
    'Content-Type': 'application/json',
    'x-api-key': os.getenv('LANGFLOW_API_KEY')
}

payload = {
    "input_value": "What were we discussing earlier?",
    "output_type": "chat",
    "input_type": "chat",
    "tweaks": {
        "ToolCallingAgent-h3cvP": {},
        "Prompt-uyRWS": {},
        "ChatInput-gdxRp": {},
        "ChatOutput-MlBIz": {},
        "SQLiteTool-9cowO": {},
        "Memory-4KtBa": {},
        "OpenAIModel-HaVzR": {},
        "CurrentDateComponent-eDDIe": {}
    }
}
logger.info("Payload prepared")

logger.info("Sending POST request to Langflow")
response = requests.post(url, headers=headers, data=json.dumps(payload))

logger.info(f"Response status code: {response.status_code}")

print(response.status_code)
print(response.json())
logger.success("Request completed")
