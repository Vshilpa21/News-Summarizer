import streamlit as st
from news_scraper import fetch_article_text
from summarizer import summarize_with_sutra, detect_language, translate_text
import pyttsx3
import tempfile
import os

st.set_page_config(page_title="📰 Sutra News Summarizer")
st.title("📰 Sutra News Summarizer (Hindi & English)")

url = st.text_input("Enter news article URL:")
lang_option = st.selectbox("Choose language (auto or manual):", ["Auto Detect", "English", "Hindi"])
translate_option = st.selectbox("Translate summary to:", ["None", "English", "Hindi"])

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
        engine = pyttsx3.init()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
            engine.save_to_file(summary, tf.name)
            engine.runAndWait()
            audio_file = open(tf.name, 'rb')
            st.audio(audio_file.read(), format='audio/mp3')
        os.remove(tf.name)
