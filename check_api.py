from os import getenv

from google import genai

client = genai.Client(
    api_key= getenv("GOOGLE_API_KEY")
)

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Say hello"
    )
    print(response.text)
except Exception as e:
    print("ERROR:", e)