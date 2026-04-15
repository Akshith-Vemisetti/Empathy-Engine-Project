from flask import Flask, render_template, request
from textblob import TextBlob
import pyttsx3
import time
import gc

app = Flask(__name__)


# 🔹 Get all available system voices
def get_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    voice_list = []
    for v in voices:
        voice_list.append({
            "id": v.id,
            "name": v.name
        })

    engine.stop()
    return voice_list


import os

def generate_voice(text, voice_id):

    engine = pyttsx3.init()

    # 🔥 CLEAN OLD FILES (VERY IMPORTANT)
    for file in os.listdir("static"):
        if file.startswith("output_"):
            try:
                os.remove(os.path.join("static", file))
            except:
                pass

    # 🔹 Sentiment
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    confidence = round(abs(polarity) * 100, 2)

    text_lower = text.lower()

    # 🔹 Voice selection
    for v in engine.getProperty('voices'):
        if v.id == voice_id:
            engine.setProperty('voice', v.id)
            break

    # 🔹 Emotion
    if polarity > 0:
        emotion = "Excited 😄" if any(w in text_lower for w in ["very","best","amazing"]) else "Happy 🙂"
    elif polarity < 0:
        if "hate" in text_lower or "angry" in text_lower:
            emotion = "Angry 😠"
        elif "sad" in text_lower or "tired" in text_lower:
            emotion = "Sad 😢"
        else:
            emotion = "Negative 😞"
    else:
        emotion = "Neutral 😐"

    # 🔹 Voice modulation
    rate_map = {
        "Excited 😄": 220,
        "Happy 🙂": 190,
        "Angry 😠": 200,
        "Sad 😢": 120,
        "Negative 😞": 140,
        "Neutral 😐": 160
    }

    engine.setProperty('rate', rate_map.get(emotion, 160))

    # 🔥 SINGLE FILE (NO MEMORY LEAK)
    filename = "output.wav"

    engine.save_to_file(text, f"static/{filename}")
    engine.runAndWait()
    engine.stop()
    gc.collect()

    return emotion, confidence, filename

@app.route("/", methods=["GET", "POST"])
def index():
    emotion = None
    confidence = None
    voices = get_available_voices()
    error = None
    audio_file = None

    if request.method == "POST":
        text = request.form["text"].strip()
        voice_id = request.form.get("voice")

        if text == "":
            error = "Please enter some text"
        else:
            emotion, confidence, audio_file = generate_voice(text, voice_id)

    return render_template(
        "index.html",
        emotion=emotion,
        confidence=confidence,
        voices=voices,
        error=error,
        audio_file=audio_file
    )


if __name__ == "__main__":
    app.run(debug=True)