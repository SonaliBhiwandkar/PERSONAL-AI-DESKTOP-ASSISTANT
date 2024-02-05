import speech_recognition as sr
import requests
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

NEWS_API_KEY = "API KEY"  # Replace with your News API key

def get_news_alert():
    try:
        # Fetch the latest news headlines
        news_url = f"URL OF YOUR API={NEWS_API_KEY}"
        response = requests.get(news_url)
        news_data = response.json()

        # Extract headlines
        headlines = [article['title'] for article in news_data['articles']]
        return headlines

    except Exception as e:
        print(f"Error fetching news: {e}")
        return []


def read_news(news_headlines):
    global news_index
    for index, news in enumerate(news_headlines, start=1):
        print(f"News {index}: {news}")
        say(f"News {index}: {news}")

        response = take_command()
        if "next" in response.lower() or "next news" in response.lower():
            continue  # Continue to the next iteration of the loop
        elif "stop the news" in response.lower() or "stop news" in response.lower():
            break  # Exit the loop

    # If loop completes, it means the user listened to all news
    print("That's the end of today's news.")
    say("That's the end of today's news.")

    # Continue listening for other commands
    while True:
        command = take_command()
        if "stop" in command:
            say("Stopping news. What else can I do for you?")
            return False  # Stop reading news
        elif "next" in command:
            # Handle next command or any other commands you want here
            return True  # Continue reading news

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice command...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing voice command...")
            command = r.recognize_google(audio, language="en-in")
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Error fetching results from Google Speech Recognition: {e}")
            return ""
        pass
