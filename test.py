import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key= GOOGLE_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")

response = model.generate_content("Translate to French: I love programming.")
print(response.text)
