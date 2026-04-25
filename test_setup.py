import requests
print("Testing Ollama connection...")
try:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": "Say 'Hello from Ollama!' in one line",
            "stream": False
        }
    )
    data = response.json()
    text = data.get("response", data.get("message", str(data)))
    print("Success!")
    print("Response:", text)
except Exception as e:
    print("Error:", e)
    print("Make sure 'ollama serve' is running in terminal")