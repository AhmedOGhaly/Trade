def analyze_data(df):
    summary = {
        "total_imports": df.shape[0],
        "total_volume": df["volume"].sum() if "volume" in df else "N/A",
        "total_value": df["value"].sum() if "value" in df else "N/A",
        "top_country": df["country"].value_counts().idxmax() if "country" in df else "N/A",
    }
    return summary
