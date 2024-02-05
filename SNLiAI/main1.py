import os
import pyttsx3
import speech_recognition as sr
from websites import open_website, websites
from weather_handler import get_weather_data, get_temperature, get_conditions, get_description
from news_handler import get_news_alert, read_news, take_command
from youtube_handler import play_youtube
from stock_handler import get_stock_data

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice command...")
        r.pause_threshold = 0.6
        try:
            audio = r.listen(source, timeout=5)  # Set a timeout (e.g., 5 seconds)
            print("Recognizing voice command...")
            command = r.recognize_google(audio, language="en-in")
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Error fetching results from Google Speech Recognition: {e}")
            return ""
        finally:
            # Explicitly release the microphone resource
            r.adjust_for_ambient_noise(source, duration=0.2)

news_index = 0  # Add this global variable
news_requested = False  # Flag to track whether news has been requested
def handle_commands(query):
    global news_index
    global news_requested
    query_lower = query.lower()

    if "stock" in query_lower:
        symbol = input("Enter the stock symbol (e.g., AAPL): ")
        say(f"Stock Entered is {symbol}")
        stock_data = get_stock_data(symbol)

        if stock_data:
            print(f"Stock data for {symbol}:\n{stock_data}")
            say(f"Stock data for {symbol}: {stock_data}")
        else:
            print("Failed to fetch stock data. Please check the symbol and try again.")
            say("Failed to fetch stock data. Please check the symbol and try again.")
        return True

    elif "weather" in query or "temperature" in query:
        weather_data = get_weather_data()
        temperature = get_temperature(weather_data)
        weather_info = f"The current temperature is {temperature} degrees Celsius."
        print(weather_info)
        say(weather_info)
        #return True

    elif "conditions" in query or "description" in query or "weather" in query:
        weather_data = get_weather_data()
        conditions = get_conditions(weather_data)
        description = get_description(weather_data)
        weather_info1 = f"The current conditions are: {conditions}.\nHere is the description: {description}."
        print(weather_info1)
        say(weather_info1)
        #return True

    elif "news" in query_lower or "headlines" in query_lower:
        news_headlines = get_news_alert()
        if news_headlines:
            for index, news in enumerate(news_headlines, start=1):
                print(f"News {index}: {news}")
                say(f"News {index}: {news}")

                response = take_command()
                if "stop" in response.lower() or "stop the news" in response.lower() or "stop news"in response.lower():
                    print("Stopping news. What else can I do for you?")
                    say("Stopping news. What else can I do for you?")
                    return True
        else:
            say("Sorry, I couldn't fetch the latest news.")
        return True

    elif "open" in query and any(website in query_lower for website in websites):
        website_name = next((website for website in websites if website in query_lower), None)
        if website_name:
            say(f"Opening {website_name}...")
            open_website(website_name)
        else:
            say("Sorry, I didn't understand the website name.")

    elif "exit" in query_lower or "quit" in query_lower:
        say("Goodbye!")
        return False

if __name__ == "__main__":
    print('Hello! I can open websites for you.')

    while True:
        query = take_command()
        if not handle_commands(query):
            #break
            pass
        # Add the following lines to use the youtube_handler module
        if "open youtube" in query.lower() and "play" in query.lower():
            play_youtube(query)
            continue  # Skip the rest of the loop

        if 'exit' in query.lower() or 'quit' in query.lower():
            say("Goodbye!")
            break
