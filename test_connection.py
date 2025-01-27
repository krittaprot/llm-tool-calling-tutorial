# Add this before your first API call
import requests
try:
    response = requests.get("http://localhost:1234/v1/models", timeout=3)
    print("Server response:", response.text)
except Exception as e:
    print("Connection failed:", str(e))