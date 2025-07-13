# Main code

# main.py

from llm_expand import generate_keywords
from seo_fetch import fetch_keyword_data
from rank_keywords import rank_keywords
import pandas as pd

def main():
    seed = input("🔍 Enter a seed keyword: ").strip()
    print("\n🔄 Generating long-tail keywords using OpenAI...\n")
    keywords = generate_keywords(seed)

    keyword_data = []
    print(f"🌐 Fetching SEO metrics for {len(keywords)} keywords...\n")

    for kw in keywords[:100]:  # Limit to 100 to avoid excess
        data = fetch_keyword_data(kw)
        keyword_data.append(data)

    print("✅ Ranking and selecting the top 50 keywords...\n")

    if not keyword_data:
       print("❗ No keyword data to rank. Exiting...")
       return

    top_keywords = rank_keywords(keyword_data)

    print(top_keywords[["keyword", "search_volume", "competition"]])

    # Save to CSV
    top_keywords.to_csv("top_keywords.csv", index=False)
    print("\n📁 Results saved to top_keywords.csv")

if __name__ == "__main__":
    main()
