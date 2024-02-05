import webbrowser

websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "amazon": "https://www.amazon.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://www.twitter.com",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "stackoverflow": "https://stackoverflow.com",
    "wikipedia": "https://www.wikipedia.org",
    "instagram": "https://www.instagram.com",
    "ebay": "https://www.ebay.com",
    "netflix": "https://www.netflix.com",
    "spotify": "https://www.spotify.com",
    "microsoft": "https://www.microsoft.com",
    "apple": "https://www.apple.com",
    "yahoo": "https://www.yahoo.com",
    "cnn": "https://www.cnn.com",
    "bbc": "https://www.bbc.com",
    "espn": "https://www.espn.com",
    "nasa": "https://www.nasa.gov",
    "pinterest": "https://www.pinterest.com",
    "wordpress": "https://www.wordpress.com",
    "twitch": "https://www.twitch.tv",
    "hulu": "https://www.hulu.com",
    "coursera": "https://www.coursera.org",
    "spotify": "https://www.spotify.com",
    "dropbox": "https://www.dropbox.com",
    "evernote": "https://www.evernote.com",
    "quora": "https://www.quora.com",
    "udemy": "https://www.udemy.com",
    "zoom": "https://www.zoom.us",
    "alibaba": "https://www.alibaba.com",
    "newegg": "https://www.newegg.com",
    # Add more websites as needed
}

def open_website(website_name):
    if website_name in websites:
        webbrowser.open_new(websites[website_name])
    else:
        print(f"Website '{website_name}' not found.")