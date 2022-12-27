# Generates a random Wikipedia article and reads a 2 sentence summary.

import wikipedia
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
query = wikipedia.random(pages=1)
results = wikipedia.summary(query, sentences=2)
print(results)
speak(results)
