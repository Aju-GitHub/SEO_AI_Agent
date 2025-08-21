## Automated SEO Keyword Agent

I did this project to stay relevant in today tech landscape. This project implements a lightweight AI-powered agent to generate, rank, and automate SEO keyword reporting. Given a seed term, the agent fetches related keywords, ranks them based on search volume and competition, and sends the results to Google Sheets via n8n workflow automation.

**Repository Structure:**

SEO_AI_Agent/

/- .env - Empty because, no paid API is used

/- SEO_AI_Agent_Ajmal_MS.pdf - Contains complete PDF document

/- llm_expand.py - Python code for pytrends and fallback keyword generator

/- main.py - Contains main python code

/- rank_keywords.py - Python code Ranking and Filtering Logic

/- requirements.txt - Contains all requiements file

/- seo_fetch.py - Python code for simulating search metrics

/- SEO_AI_Agent - Fetched top keywords for "Engineering Tools"

# Objective

- Generate SEO keyword suggestions from a user-provided seed term.

- Rank keywords by search volume and competition.

- Automate reporting to Google Sheets for tracking and analysis.

# Tech Stack

- Flask – REST API server for keyword requests.

- PyTrends – Python wrapper for Google Trends data.

- Pandas – Data manipulation, sorting, and filtering.

- n8n.io – Workflow automation (webhook + Sheets).

- Google Sheets – Storage for generated keyword reports.

# Workflow

1. Input: User sends JSON { "seed": "..." } to Flask endpoint /generate.

2. Keyword Generation:
- Fetches related keywords via PyTrends.
- If API unavailable, uses a fallback keyword list.

3. Data Enrichment: Each keyword is assigned simulated metrics: search volume, competition.

4. Ranking:
- Keywords are sorted by high search volume and low competition.
- Top 50 keywords are selected.

5. Push to n8n: Results sent as JSON to n8n webhook.

6. n8n Flow:
- Webhook → Split Items → Set Fields → Append to Google Sheets.

# Outputs

- JSON response from Flask containing ranked keywords.

- Google Sheet with keyword, search volume, and competition.

- Console logs for debugging and verification.

# Advantages

- Works offline with fallback data if Google Trends is unavailable.

- Lightweight, fast to deploy, and minimal dependencies.

- Easily extendable using n8n for additional workflows.

**Rights and Usage:**

All reports, documentation, and related artifacts are the intellectual property of Ajmal M S.

Shared resources are provided solely as a record of my involvement, competencies, and learning outcomes.

No content from this repository may be copied, altered, shared, or reused without explicit permission.

© Ajmal M S, 2025
