# python3 -m venv .john
# source .john/bin/activate
# python3 -m pip install selenium

import webbrowser
import time

# Open the URL in a new tab
webbrowser.open_new_tab("https://tradexy.github.io/musicplayer/")

# Wait for the page to load
time.sleep(5)

# Get the audio element
audio = webbrowser.find_element_by_id("music")

# Play the music
audio.click()
