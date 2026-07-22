import os
import requests
from src.config.db import get_db

GENERAL_KEYWORDS = ["opec", "opec+", "crude oil", "oil tanker", "sanctions oil"]

def get_corridor_keywords(db):
    corridors = db.table("corridors").select("id, name").execute().data
    keywords = {}
    for c in corridors:
        # Generate some basic keywords from the corridor name
        name_lower = c["name"].lower()
        base_kw = name_lower.replace("strait of ", "").replace("canal", "").strip()
        keywords[c["id"]] = [name_lower, base_kw]
    return keywords

def fetch_candidate_entries() -> list[dict]:
    """Fetch global energy/shipping news using the Tinyfish AI API."""
    api_key = os.environ.get("TINYFISH_API_KEY")
    if not api_key:
        print("WARNING: TINYFISH_API_KEY not found in environment.")
        return []
        
    url = "https://api.tinyfish.ai/v1/news"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    payload = {
        "query": "oil tanker disruption OR suez OR hormuz OR bab-el-mandeb OR OPEC",
        "limit": 50
    }
    
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        if resp.status_code != 200:
            print(f"Tinyfish API error: {resp.status_code} {resp.text}")
            return []
            
        data = resp.json()
        entries = []
        for item in data.get("data", []):
            entries.append({
                "url": item.get("url", ""),
                "title": item.get("title", ""),
                "source": item.get("source", "tinyfish"),
                "published_at": item.get("published_at", None),
            })
        return entries
    except Exception as e:
        print(f"Tinyfish request failed: {e}")
        return []


def match_corridor(title: str, db) -> str | None:
    """Return the corridor id this headline is relevant to, or None if no match."""
    lower = title.lower()
    corridor_keywords = get_corridor_keywords(db)
    
    for corridor_id, keywords in corridor_keywords.items():
        if any(kw in lower for kw in keywords if len(kw) > 3):
            return corridor_id
            
    # General energy/geopolitical keywords without a specific corridor match
    # still count as relevant but need Gemini to assign the corridor.
    if any(kw in lower for kw in GENERAL_KEYWORDS):
        return "unassigned"
    return None


def filter_relevant(entries: list[dict]) -> list[dict]:
    db = get_db()
    relevant = []
    for e in entries:
        if not e["url"] or not e["title"]:
            continue
        corridor_guess = match_corridor(e["title"], db)
        if corridor_guess:
            e["corridor_guess"] = corridor_guess
            relevant.append(e)
    return relevant


def dedup_against_db(entries: list[dict]) -> list[dict]:
    """Only return entries whose URL isn't already in the headlines table."""
    db = get_db()
    if not entries:
        return []
    urls = [e["url"] for e in entries]
    existing = db.table("headlines").select("url").in_("url", urls).execute()
    existing_urls = {row["url"] for row in existing.data}
    new_entries = [e for e in entries if e["url"] not in existing_urls]
    return new_entries


def insert_headlines(entries: list[dict]) -> list[dict]:
    """Insert new headline rows, return them with their DB ids."""
    db = get_db()
    inserted = []
    for e in entries:
        row = {
            "url": e["url"],
            "title": e["title"],
            "source": e["source"],
            "processed": False,
        }
        result = db.table("headlines").insert(row).execute()
        if result.data:
            inserted.append(result.data[0])
    return inserted
