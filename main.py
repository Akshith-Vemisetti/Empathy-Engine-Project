from textblob import TextBlob
import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Step 1: Input
text = input("Enter your text: ")

# Step 2: Sentiment
blob = TextBlob(text)
polarity = blob.sentiment.polarity

# Step 3: Advanced Emotion Detection

text_lower = text.lower()

if polarity > 0:
    if "very" in text_lower or "best" in text_lower or "amazing" in text_lower:
        emotion = "Excited 😄"
    else:
        emotion = "Happy 🙂"

elif polarity < 0:
    if "hate" in text_lower or "angry" in text_lower:
        emotion = "Angry 😠"
    elif "sad" in text_lower or "tired" in text_lower:
        emotion = "Sad 😢"
    else:
        emotion = "Negative 😞"

else:
    emotion = "Neutral 😐"

# Step 4: Emotion-based Voice Modulation

if "Excited" in emotion:
    engine.setProperty('rate', 220)
    engine.setProperty('volume', 1.0)

elif "Happy" in emotion:
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 0.9)

elif "Angry" in emotion:
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1.0)

elif "Sad" in emotion:
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.7)

elif "Negative" in emotion:
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 0.8)

else:
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 0.9)

# Step 5: Speak
# Save audio
engine.save_to_file(text, "output.wav")
engine.runAndWait()

print("Audio saved as output.wav")