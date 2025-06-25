# 📰 Sutra News Summarizer (Hindi & English)

A multilingual news summarizer app that extracts content from regional news websites, summarizes using **Sutra API**, translates content (English ↔ Hindi), and provides **text-to-speech (TTS)** support with audio download options.

---

## 🚀 Features

- 🌐 **URL-based Article Scraping** – Extracts clean text from Indian news websites.
- 🧠 **Sutra API Summarization** – Generates concise summaries in English or Hindi.
- 🈳 **Language Auto-Detection** – Detects original language using `langdetect`.
- 🌍 **Translation Support** – Translates summaries between Hindi and English using Sutra.
- 🔊 **Text-to-Speech (TTS)** – Converts summaries to speech using `gTTS` or `pyttsx3`.
- 💾 **Audio Download Option** – Provides `.mp3` file for offline listening.
- 🧠 **Content Caching** – Locally stores previously fetched articles.

---

## 🛠️ Tech Stack

| Component       | Tech Used                      |
|----------------|--------------------------------|
| Frontend       | Streamlit                      |
| Backend        | Python                         |
| Web Scraping   | Newspaper3k                    |
| Summarization  | Sutra API (via Two.AI)         |
| Translation    | Sutra API                      |
| TTS Engine     | pyttsx3 (offline), gTTS (online) |
| Caching        | Local file system              |
| Environment    | `.env`, dotenv                 |

---

## 🧰 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sutra-news-summarizer.git
cd sutra-news-summarizer
```

### 2. Create & activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up `.env`

Create a `.env` file in the root directory:

```env
SUTRA_API_KEY=your_two_ai_api_key_here
```

You can get your API key from: [https://www.two.ai/sutra/api](https://www.two.ai/sutra/api)

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🔍 How It Works

1. **User inputs a news URL**
2. The app:
   - Scrapes the article
   - Detects the language
   - Sends content to Sutra API for summarization
   - Optionally translates the output
   - Generates an audio file (if selected)
3. The app displays:
   - Full article content
   - Summary
   - Audio playback & download

---

## 🚧 Future Enhancements

- 🧠 Add user-defined summary length
- 🗣️ Add support for other Indian languages (e.g., Tamil, Telugu, Bengali)
- 📱 Integrate with WhatsApp or Telegram for daily updates
- 📈 Analytics for tracking article types & language usage

---

## 🙏 Acknowledgements

- [Two.AI](https://www.two.ai) for Sutra API
- [Streamlit](https://streamlit.io/) for the UI framework
- [newspaper3k](https://github.com/codelucas/newspaper) for article scraping
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) & [gTTS](https://pypi.org/project/gTTS/) for TTS

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.