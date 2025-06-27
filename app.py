import streamlit as st
from news_scraper import fetch_article_text
from summarizer import summarize_with_sutra, detect_language, translate_text
from gtts import gTTS
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
            audio_lang = 'hi' if translate_option == "Hindi" else 'en'
        else:
            audio_lang = 'hi' if lang == "Hindi" else 'en'

        st.subheader("Summary")
        st.success(summary)

        # ✅ Text-to-Speech with gTTS
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
                tts = gTTS(text=summary, lang=audio_lang)
                tts.save(tf.name)
                st.audio(tf.name, format='audio/mp3')
        except Exception as e:
            st.warning(f"Text-to-Speech failed: {e}")
