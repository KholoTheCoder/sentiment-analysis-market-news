from textblob import TextBlob # type: ignore

text = "I love learning Python!"
blob = TextBlob(text)

print(blob.sentiment)

