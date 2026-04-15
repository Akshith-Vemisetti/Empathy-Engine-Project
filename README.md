Empathy Engine: Emotion-Aware Text-to-Speech System
Overview

The Empathy Engine is a web-based application that converts text into speech while dynamically adjusting vocal characteristics based on the emotional tone of the input. Unlike standard text-to-speech systems that produce monotonic output, this system introduces variations in speech rate and delivery style to better reflect the sentiment of the text.

The application also allows users to select from available system voices, enabling more personalized and expressive audio output.

Features
Accepts user input text via a web interface
Detects sentiment using natural language processing
Classifies text into emotional categories:
Happy / Excited
Sad
Angry
Negative
Neutral
Dynamically adjusts speech properties based on emotion:
Speech rate
Delivery style
Supports multiple system voices using pyttsx3
Generates playable audio output in real time
Includes a clean and interactive UI with:
Custom dropdown for voice selection
Microphone input (speech-to-text)
Animated background
Confidence score visualization
Tech Stack
Backend: Python, Flask
NLP: TextBlob
Text-to-Speech: pyttsx3
Frontend: HTML, CSS, JavaScript
Audio Handling: WAV file generation
Project Structure
empathy_engine/
│
├── app.py
├── static/
│   └── output.wav
├── templates/
│   └── index.html
└── README.md
Installation and Setup
1. Clone the repository
git clone <your-repo-url>
cd empathy_engine
2. Install dependencies
pip install flask
pip install textblob
pip install pyttsx3
python -m textblob.download_corpora
3. Run the application
python app.py
4. Open in browser
http://127.0.0.1:5000/
How It Works
The user inputs text through the web interface
TextBlob analyzes the sentiment polarity of the input
Based on polarity and keyword heuristics, the system classifies emotion
The selected voice is retrieved from available system voices
Speech parameters such as rate are adjusted according to emotion
pyttsx3 generates an audio file
The audio is played back in the browser
Emotion to Voice Mapping
Emotion	Speech Rate	Description
Excited	High	Fast and energetic delivery
Happy	Moderately High	Lively tone
Angry	High	Strong and intense delivery
Sad	Low	Slow and softer speech
Negative	Medium-Low	Slightly subdued tone
Neutral	Medium	Balanced delivery
Design Choices
pyttsx3 was chosen for offline TTS capability and access to system voices
TextBlob was used for simplicity and fast sentiment analysis
A single audio file overwrite strategy was implemented to prevent performance issues caused by file accumulation
A custom dropdown UI was used to improve user interaction compared to default HTML select elements
Limitations
Voice quality depends on system-installed TTS voices
Limited emotional expressiveness compared to advanced cloud-based TTS APIs
Emotion detection is rule-based and may not capture nuanced context
Future Improvements
Integration with advanced TTS APIs (e.g., ElevenLabs, Google Cloud TTS)
More granular emotion classification (e.g., surprise, curiosity)
Emotion intensity scaling
Real-time streaming audio instead of file-based playback
Improved NLP using transformer-based models
Conclusion

The Empathy Engine demonstrates how sentiment analysis and speech synthesis can be combined to produce more human-like AI interactions. It serves as a foundation for building emotionally aware conversational systems in domains such as customer support, virtual assistants, and AI-driven communication tools.