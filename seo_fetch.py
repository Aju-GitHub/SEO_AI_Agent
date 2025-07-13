# SEO Fetch

# seo_fetch.py (mock version)

import random

def fetch_keyword_data(keyword):
    return {
        "keyword": keyword,
        "search_volume": random.randint(500, 10000),     # Simulated monthly search volume
        "competition": round(random.uniform(10, 80), 2)  # Simulated SEO competition score
    }
