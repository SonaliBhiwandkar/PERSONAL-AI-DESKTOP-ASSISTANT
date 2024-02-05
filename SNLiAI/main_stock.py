# main_stock.py
import os
import pyttsx3
import speech_recognition as sr
from stock_handler import get_stock_data

def say(text):
    engine\
        = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        print("Raw Audio:", audio)

        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language="en-in")
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Error fetching results from Google Speech Recognition: {e}")
            return ""

def handle_commands(query):
    query_lower = query.lower()

    if "stock" in query_lower:
        symbol = input("Enter the stock symbol (e.g., AAPL): ")
        stock_data = get_stock_data(symbol)

        if stock_data:
            print(f"Stock data for {symbol}:\n{stock_data}")
            say(f"Stock data for {symbol}: {stock_data}")
        else:
            print("Failed to fetch stock data. Please check the symbol and try again.")
            say("Failed to fetch stock data. Please check the symbol and try again.")

if __name__ == "__main__":
    print('Hello! I can check stock prices for you.')

    while True:
        query = takeCommand()
        if 'exit' in query.lower() or 'quit' in query.lower():
            say("Goodbye!")
            break

        handle_commands(query)
