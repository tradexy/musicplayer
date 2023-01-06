# python3 -m venv .john
# source .john/bin/activate
# python3 -m pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Fetch the page content
response = requests.get("https://tradexy.github.io/musicplayer/")

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the audio element
audio = soup.find(id="music")

# Get the URL of the audio file
audio_url = audio["src"]

# Play the audio file
subprocess.run(["mpv", audio_url])
