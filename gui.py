import tkinter as tk
from tkinter import ttk
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
        "thanks a lot",
        "definitely"
    ]
    return any(phrase in lowered for phrase in sarcasm_triggers)

def detect_tone():
    text = entry.get("1.0", tk.END).strip()
    scores = analyze_sentiment(text)
    tones = []

    if is_possibly_sarcastic(scores, text):
        tones.append("possibly sarcastic")

    sentiment_line = (
        f"Negative: {scores['neg']:.2f}     "
        f"Neutral: {scores['neu']:.2f}     "
        f"Positive: {scores['pos']:.2f}"
    )

    tone_line = "Tone: " + (", ".join(tones) if tones else "none")

    result_text = f"{sentiment_line}\n{tone_line}"

    output_label.config(text=result_text, anchor="center", justify="center")

    return {
        "scores": scores,
        "tones": tones
    }


window = tk.Tk()
window.title("Tone")
window.geometry('400x400')

# Title
title_label = ttk.Label(master=window, text="Analyze text", font="Calibri 24", padding=8)
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
entry = tk.Text(input_frame, width=50, height=10, padx=10)
entry.pack()
button = ttk.Button(input_frame, text="Analyze", command=detect_tone)
button.pack(pady=2)
input_frame.pack(padx=10)

# Output
output_label = ttk.Label(master=window, text='Result will appear here', wraplength=380)
output_label.pack(pady=10)

window.mainloop()
