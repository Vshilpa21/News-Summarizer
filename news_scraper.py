from newspaper import Article
from cache_utils import load_from_cache, save_to_cache
import re

def clean_text(text: str) -> str:
    lines = text.split("\n")
    clean_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if any(kw in line.lower() for kw in ["related news", "follow us", "click here", "read also", "social media"]):
            continue
        clean_lines.append(line)
    return "\n".join(clean_lines).strip()

def fetch_article_text(url: str) -> str:
    cached = load_from_cache(url)
    if cached:
        return cached
    try:
        article = Article(url)
        article.download()
        article.parse()
        cleaned = clean_text(article.text)
        save_to_cache(url, cleaned)
        return cleaned if len(cleaned) > 100 else "🛑 Not enough content extracted."
    except Exception as e:
        return f"🛑 Error scraping article: {e}"
