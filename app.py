import streamlit as st
from news_scraper import fetch_article_text
from summarizer import summarize_with_sutra, detect_language, translate_text
import tempfile
import os
from gtts import gTTS
import pyttsx3
import time

st.set_page_config(page_title="📰 Sutra News Summarizer")
st.title("📰 Sutra News Summarizer (Hindi & English)")

url = st.text_input("Enter news article URL:")

lang_option = st.selectbox("Choose language (auto or manual):", ["Auto Detect", "English", "Hindi"])
translate_option = st.selectbox("Translate summary to:", ["None", "English", "Hindi"])
tts_option = st.selectbox("Audio Output:", ["None", "pyttsx3 (Offline)", "gTTS (Online)"])

if st.button("Summarize"):
    article = fetch_article_text(url)

    if not article or article.startswith("🛑"):
        st.error("🛑 Could not extract article text.")
    else:
        st.subheader("Original Article")
        st.write(article[:1500])

        if lang_option == "Auto Detect":
            lang = detect_language(article)
            st.write(f"Detected Language: {lang}")
        else:
            lang = lang_option

        summary = summarize_with_sutra(article, lang)

        if translate_option != "None" and translate_option != lang:
            summary = translate_text(summary, target_lang=translate_option)
            st.write(f"🔁 Translated Summary ({translate_option}):")

        st.subheader("Summary")
        st.success(summary)

        # Text-to-Speech
        if tts_option != "None":
            with st.spinner("🔊 Generating audio..."):
                audio_path = os.path.join("temp_audio.mp3")
                if tts_option == "pyttsx3 (Offline)":
                    engine = pyttsx3.init()
                    engine.save_to_file(summary, audio_path)
                    engine.runAndWait()
                elif tts_option == "gTTS (Online)":
                    tts = gTTS(text=summary, lang='hi' if "Hindi" in translate_option else 'en')
                    tts.save(audio_path)

                time.sleep(1)  # Ensure file is fully written
                st.audio(audio_path, format="audio/mp3")
                with open(audio_path, "rb") as f:
                    st.download_button("⬇️ Download Audio", f, file_name="summary.mp3")
