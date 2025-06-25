import os
import requests
from dotenv import load_dotenv
from langdetect import detect

load_dotenv()
API_KEY = os.getenv("SUTRA_API_KEY")
API_URL = "https://api.two.ai/v2/chat/completions"

def detect_language(text: str) -> str:
    try:
        lang_code = detect(text)
        return "Hindi" if lang_code == "hi" else "English"
    except:
        return "English"

def summarize_with_sutra(text: str, lang: str = "English") -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"Summarize this {lang} news article in 2-3 sentences:\n\n{text}"
    payload = {
        "model": "sutra-v2",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200,
        "temperature": 0.3
    }
    try:
        resp = requests.post(API_URL, headers=headers, json=payload)
        if resp.status_code == 200:
            return resp.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Error {resp.status_code}: {resp.text}"
    except Exception as e:
        return f"Error contacting Sutra API: {e}"

def translate_text(text: str, target_lang: str) -> str:
    prompt = f"Translate this text to {target_lang}:\n\n{text}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sutra-v2",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200,
        "temperature": 0.3
    }
    try:
        resp = requests.post(API_URL, headers=headers, json=payload)
        if resp.status_code == 200:
            return resp.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Error {resp.status_code}: {resp.text}"
    except Exception as e:
        return f"Error translating text: {e}"
