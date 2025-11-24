from google import genai
import os

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

response = client.models.generate_content(
    model="models/gemini-3-pro-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)