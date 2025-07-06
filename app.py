from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

app = Flask(__name__)

# Setup Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Language options
LANGUAGES = {
    "English": "English",
    "Hindi": "Hindi",
    "French": "French",
    "Spanish": "Spanish",
    "German": "German",
    "Chinese": "Chinese",
    "Arabic": "Arabic",
    "Bengali": "Bengali",
    "Japanese": "Japanese",
    "Korean": "Korean"
}

@app.route('/')
def index():
    return render_template("index.html", languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    target_language = data['target_language']
    source_language = data['source_language']

    if source_language == "auto":
        prompt = f"Detect the language and translate the following text to {target_language}:\n\"{text}\""
    else:
        prompt = f"Translate from {source_language} to {target_language}:\n\"{text}\""

    response = model.generate_content(prompt)
    
    detected_lang = "Auto-detected"
    if source_language == "auto":
        try:
            lang_prompt = f"What language is this text written in?\n\"{text}\""
            lang_response = model.generate_content(lang_prompt)
            detected_lang = lang_response.text.strip()
        except:
            detected_lang = "Unknown"

    else:
        detected_lang = source_language

    return jsonify({
        "translated_text": response.text.strip(),
        "detected_language": detected_lang
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT environment variable
    app.run(host="0.0.0.0", port=port)
