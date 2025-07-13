# llm_expand.py — Pytrends + fallback keyword generator
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError

def generate_keywords(seed):
    print(f"📊 Getting keyword suggestions for: '{seed}' using Google Trends")

    pytrends = TrendReq(hl="en-US", tz=330)

    try:
        pytrends.build_payload([seed], cat=0, timeframe='today 12-m', geo='', gprop='')
        related = pytrends.related_queries()[seed]['top']

        if related is None or related.empty:
            raise ValueError("⚠️ No related keywords found.")

        keywords = related['query'].tolist()
        print(f"✅ Got {len(keywords)} keywords from Google Trends")
        return keywords

    except TooManyRequestsError as e:
        print(f"❌ Google Trends rate limit hit (429): {e}")
    except Exception as e:
        print(f"❌ Pytrends failed: {e}")

    print("🔁 Falling back to built-in keyword generator...")

    # Simple fallback keyword list
    fallback_keywords = [
        f"{seed} tips",
        f"{seed} tools",
        f"{seed} guide",
        f"{seed} strategy",
        f"{seed} for beginners",
        f"{seed} free tools",
        f"{seed} automation tools",
        f"how to use {seed}",
        f"{seed} in 2025",
        f"top {seed} trends",
        f"ai and {seed}",
        f"{seed} marketing hacks",
        f"latest {seed} techniques",
        f"{seed} for business growth",
        f"{seed} and SEO",
        f"{seed} content ideas",
        f"{seed} growth hacks"
    ]
    return fallback_keywords
