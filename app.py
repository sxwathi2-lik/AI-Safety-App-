from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form["text"].lower()

    scam_words = ["urgent", "click now", "limited offer", "winner", "free money", "otp", "bank"]
    fake_words = ["worst", "fake", "waste", "bad", "not good"]

    result = "Safe ✅"
    reason = "No major issues detected"
    trust = 90

    # Scam detection
    for word in scam_words:
        if word in text:
            result = "Scam Detected ⚠️"
            reason = f"Suspicious word found: {word}"
            trust = 20

    # Fake review detection
    for word in fake_words:
        if word in text:
            result = "Fake Review ❌"
            reason = f"Negative/spam word detected: {word}"
            trust = 40

    # URL detection
    if re.search(r"http[s]?://", text):
        result = "Phishing Link ⚠️"
        reason = "Contains suspicious link"
        trust = 10

    # Sentiment
    if "good" in text or "love" in text:
        sentiment = "Positive 😊"
    elif "bad" in text or "worst" in text:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    return render_template("index.html",
                           result=result,
                           reason=reason,
                           trust=trust,
                           sentiment=sentiment)

app.run(host="0.0.0.0", port=10000)
