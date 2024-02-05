import os
import datetime
import time
import random
import pywhatkit
import openai
import cv2
import pyjokes
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit as kit

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Error fetching results from Google Speech Recognition: {e}")
            return ""

def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Sorry, I couldn't calculate that. Error: {str(e)}"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am SNLiAI")

    sites = [
        ["YouTube", "https://www.youtube.com/"],
        ["Map", "https://www.google.com/maps/"],
        ["Google", "https://www.google.com/"],
        ["Chrome", "https://www.google.com/"],
        ["Wikipedia", "https://en.wikipedia.org/"]
        # Add more websites with their names and URLs here
    ]

    while True:
        query = takeCommand()
        query_lower = query.lower()

        for site in sites:
            if f"open {site[0].lower()}" in query_lower:
                say(f"Opening {site[0]}, ...")
                webbrowser.open_new(site[1])
                break  # Exit the loop after opening the website
        else:
            if "exit" in query_lower or "quit" in query_lower or "shut up" in query_lower:
                say("Goodbye, Friend!")
                break
            else:
                say("")

        """if "music" in query_lower or "song" in query_lower:
            musicPath ="music/SOLO.mp3"  #Replace with your music directory path
            say("playing Music ")
            os.startfile(musicPath)"""

        if "random song" in query_lower or "random music" in query_lower:
            music_directory = "music/SOLO.mp3"  # Replace with your music directory path
            music_files = [file for file in os.listdir(music_directory) if
                           file.endswith(('.mp3', '.wav', '.ogg', '.flac'))]

            if not music_files:
                say("I couldn't find any music files in your music directory.")
            else:
                random_song = random.choice(music_files)
                music_path = os.path.join(music_directory, random_song)
                say(f"Playing random song: {random_song}")
                os.startfile(music_path)

        elif "play" in query_lower and "song" in query_lower:
            # Extract the song name from the query
            song_name = query_lower.replace("play", "").replace("song", "").strip()

            if song_name:
                say(f"Playing the song: {song_name}")
                kit.playonyt(song_name)
            else:
                say("Please specify a song to play.")

        if "what is the time" in query_lower:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} and {min} minutes")

        if "open camera" in query_lower:
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow("Camera", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                query = takeCommand()
                if "close camera" in query.lower():
                    say("Closing the camera, sir.")
                    break
            cap.release()
            cv2.destroyAllWindows()

        if "open vs code" in query:
            vscodePath ="YOUR PATH"
            os.startfile(vscodePath)

        """if "open word" in query:
            wordPath ="YOUR PATH"
            os.startfile(wordPath)"""

        if "joke" in query_lower or "fact" in query_lower:
            joke = pyjokes.get_joke()
            say(joke)
            print(f"Assistant: {joke}")

        if "navigate to" in query_lower:
            location = query_lower.replace("navigate to", "").strip()
            say(f"Opening Google Maps and navigating to {location}")
            map_url = f"https://www.google.com/maps/place/{location}"
            webbrowser.open_new(map_url)

        if "open youtube" in query_lower and "play" in query_lower:
            query_parts = query_lower.split("play")
            if len(query_parts) > 1:
                video_query = query_parts[1].strip()
                say(f"Opening YouTube and playing {video_query}")
                kit.playonyt(video_query)
            else:
                say("Please specify a video to play.")


        if "calculate" in query_lower:
            expression = query_lower.replace("calculate", "").strip()
            result = calculate(expression)
            say(result)
            print(f"Assistant: {result}")


