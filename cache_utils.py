import os
import json
import hashlib

CACHE_DIR = "cache"

def get_cache_filename(url: str) -> str:
    os.makedirs(CACHE_DIR, exist_ok=True)
    file_hash = hashlib.md5(url.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{file_hash}.json")

def save_to_cache(url: str, content: str):
    path = get_cache_filename(url)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"url": url, "content": content}, f)

def load_from_cache(url: str) -> str:
    path = get_cache_filename(url)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("content", "")
    return ""
