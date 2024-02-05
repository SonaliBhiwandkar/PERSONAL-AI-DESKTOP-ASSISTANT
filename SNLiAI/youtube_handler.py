# youtube_handler.py

import pyttsx3
import pywhatkit as kit

def play_youtube(query):
    query_lower = query.lower()

    if "open youtube" in query_lower and "play" in query_lower:
        query_parts = query_lower.split("play")
        if len(query_parts) > 1:
            video_query = query_parts[1].strip()
            say(f"Opening YouTube and playing {video_query}")
            kit.playonyt(video_query)
        else:
            say("Please specify a video to play.")

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
