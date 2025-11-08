# main.py
from sentiment_analyser import analyze_sentiment

def main():
    print("🧠 Simple Sentiment Analysis Bot 🧠")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("Enter a sentence: ")

        # Exit condition
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        # Analyze and display result
        result = analyze_sentiment(user_input)
        print(f"Sentiment: {result['sentiment']} | Polarity Score: {result['polarity']}\n")

if __name__ == "__main__":
    main()
