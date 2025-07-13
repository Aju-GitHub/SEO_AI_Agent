# Ranking and Filtering Logic

import pandas as pd

def rank_keywords(keyword_data):
    
    #converting format to DataFrame
    df = pd.DataFrame(keyword_data)
   
    # Remove empty or duplicate keywords
    df =  df.dropna(subset=['keyword'])
    df = df.drop_duplicates(subset=["keyword"])

    # Convert numeric fields
    df["search_volume"] = pd.to_numeric(df["search_volume"], errors='coerce').fillna(0)
    df["competition"] = pd.to_numeric(df["competition"], errors='coerce').fillna(100)

    # Sort by: High Search Volume (desc), Low Competition (asc)
    df = df.sort_values(by=["search_volume", "competition"], ascending=[False, True])

    # Return top 50 keywords
    return df.head(50)


