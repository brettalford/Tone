from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    return analyzer.polarity_scores(text)


def is_possibly_sarcastic(scores, text):
    lowered = text.lower()
    sarcasm_triggers = [
        "yeah right", 
        "great job", 
        "wonderful", 
        "just perfect", 
        "love that for me",
        "as if", 
        "sure thing", 
        "thanks a lot"
    ]
    return any(phrase in lowered for phrase in sarcasm_triggers)

def detect_tone(text):
    scores = analyze_sentiment(text)
    tones = []

    if is_possibly_sarcastic(scores, text):
        tones.append("possibly sarcastic")

    return {
        "scores": scores,
        "tones": tones
    }



if __name__ == "__main__":
    test_inputs = [
        "Oh, wonderful. Just perfect. Love that for me.",
        "I hate this so much. It's the worst thing ever.",
        "Great job, just what I needed!",
        "You're such an idiot. Amazing work."
    ]

    for message in test_inputs:
        result = detect_tone(message)
        print("Input:", message)
        print("Sentiment Scores:", result["scores"])
        print("Detected Tone(s):", result["tones"])
        print()
