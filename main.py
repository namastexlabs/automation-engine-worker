import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('LANGFLOW_URL')
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

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.status_code)
print(response.json())
