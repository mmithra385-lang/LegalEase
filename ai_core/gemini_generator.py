import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Loaded API Key:", api_key)
print("Key Length:", len(api_key) if api_key else 0)

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Create Gemini client
client = genai.Client(api_key=api_key)

import sys
import google.genai

print("=" * 50)
print("Python:", sys.executable)
print("google.genai:", google.genai.__file__)
print("=" * 50)


def generate_document(document_type, parties, terms, effective_date):
    return f"""
{document_type}

Parties:
{parties}

Terms:
{terms}

Effective Date:
{effective_date}

This is a sample legal document generated for demonstration purposes.

Signatures:

Party 1: ___________________

Party 2: ___________________
"""