# PERSONAL AI DESKTOP ASSISTANT

## Overview
**PERSONAL AI DESKTOP ASSISTANT** is a Python-based application that integrates various APIs and libraries to act as a virtual assistant. It can perform tasks such as:

- Fetching stock market data
- Providing weather updates
- Playing YouTube videos
- Fetching the latest news
- Performing basic calculations
- Opening websites and applications
- Interacting with the user via voice commands

This assistant combines the power of speech recognition, text-to-speech, and web services to deliver a seamless user experience.

---

## Publication
This project has been published as a paper in the **INDIAN JOURNAL OF TECHNICAL EDUCATION**, Volume 47, Special Issue No. 1, February 2024. The paper discusses the design, implementation, and potential applications of the assistant in detail.

**Link to the paper:** [Download the paper](https://www.icstemsd.in/assets/pdf/Special%20issue%201%20Feb%202024.pdf)

**Indexed in:** UGC-Care Journal list

---
## Certificate
![Certificate of Publication](images/certificate%20paper%20presentation.png)

----
## Features
1. **Voice Interaction:**
   - Recognizes and responds to user commands using `speech_recognition` and `pyttsx3`.

2. **Web Services Integration:**
   - Fetches stock data via Alpha Vantage API.
   - Retrieves weather information from a weather API.
   - Plays YouTube videos with `pywhatkit`.
   - Provides news headlines using a news API.

3. **Application Control:**
   - Opens websites and local applications.
   - Controls camera and captures input using OpenCV.

4. **Task Execution:**
   - Performs calculations.
   - Provides jokes and fun facts.
   - Navigates to specified locations on Google Maps.

---

## Prerequisites
Ensure you have the following installed:

1. **Python 3.7+**
2. Required Python libraries (can be installed using `requirements.txt`):

   ```bash
   pip install -r requirements.txt
   ```

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/PERSONAL-AI-DESKTOP-ASSISTANT.git
   cd PERSONAL-AI-DESKTOP-ASSISTANT
   ```

2. **Install Dependencies**
   Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**
   - Obtain the following API keys:
     - **Alpha Vantage API** for stock data: [Get API Key](https://www.alphavantage.co/support/#api-key)
     - **Weather API** for weather updates: [Get API Key](https://openweathermap.org/api)
     - **News API** for news headlines: [Get API Key](https://newsapi.org/)
   
   - Add your API keys to a `.env` file in the project root:
     ```
     STOCK_API_KEY=your_stock_api_key
     WEATHER_API_KEY=your_weather_api_key
     NEWS_API_KEY=your_news_api_key
     ```

4. **Run the Application**
   ```bash
   python main.py
   ```

---

## Usage
1. Start the application.
2. Speak commands such as:
   - "What is the weather?"
   - "Open YouTube and play [song name]."
   - "Get stock data for AAPL."
   - "Tell me a joke."
   - "Navigate to New York on Google Maps."

3. The assistant will respond and execute the requested task.

---

## File Structure
```
PERSONAL-AI-DESKTOP-ASSISTANT/
├── stock_handler.py       # Handles stock data retrieval
├── weather_handler.py     # Handles weather data retrieval
├── youtube_handler.py     # Handles YouTube interactions
├── main.py                # Main script to run the assistant
├── config.py              # Configuration file (API keys)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Features to Implement (Future Enhancements)
- Adding support for additional APIs (e.g., Spotify, Calendar integrations).
- Personalization using user profiles.
- Improved NLP for better understanding of commands.
- Integration with IoT devices for smart home control.

---

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyWhatKit](https://pypi.org/project/pywhatkit/)
- [OpenAI](https://openai.com/)
- [OpenCV](https://opencv.org/)
