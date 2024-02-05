import pyttsx3
import speech_recognition as sr
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio =r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from SNLiAI"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello i am SNLiAI")
    while True:
        print("Listening.....")
        query = takeCommand()