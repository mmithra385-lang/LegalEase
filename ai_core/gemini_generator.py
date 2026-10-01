import os
import sys
from dotenv import load_dotenv
from google import genai
import google.genai

# Load environment variables
load_dotenv()

# Read API key and model
api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

print("=" * 50)
print("Python:", sys.executable)
print("google.genai:", google.genai.__file__)
print("=" * 50)

print("Loaded API Key:", "Found" if api_key else "Not Found")
print("Key Length:", len(api_key) if api_key else 0)

# Create Gemini client only if API key exists
client = None

if api_key:
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        print("Gemini Client Error:", e)


def generate_document(document_type, parties, terms, effective_date):
    """
    Generates a legal document using Gemini.
    Falls back to a sample document if Gemini is unavailable.
    """

    # Fallback if API key is missing
    if client is None:
        return f"""
{document_type}

Parties:
{parties}

Terms:
{terms}

Effective Date:
{effective_date}

This is a sample legal document generated because Gemini API is not configured.

Signatures:

Party 1: ___________________

Party 2: ___________________
"""

    prompt = f"""
Generate a professional legal {document_type}.

Parties:
{parties}

Terms:
{terms}

Effective Date:
{effective_date}

Include:
- Title
- Introduction
- Legal Clauses
- Signature Section
"""

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        if hasattr(response, "text") and response.text:
            return response.text

        return "No response generated."

    except Exception as e:
        print("Gemini Error:", e)

        return f"""
{document_type}

Parties:
{parties}

Terms:
{terms}

Effective Date:
{effective_date}

This is a sample legal document generated because Gemini API failed.

Signatures:

Party 1: ___________________

Party 2: ___________________
"""