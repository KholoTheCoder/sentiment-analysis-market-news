


__all__ = ["analyze_sentiment"]
# sentiment_analyzer.py
from textblob import TextBlob # type: ignore

def analyze_sentiment(text):
 

    # Create a TextBlob object (which automatically analyzes text)
    blob = TextBlob(text)

    # Polarity score ranges from -1 (negative) to +1 (positive)
    polarity = blob.sentiment.polarity

    # Determine sentiment category
    if polarity > 0:
        sentiment = "Positive 😀"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    # Return structured result
    return {"text": text, "polarity": polarity, "sentiment": sentiment}
