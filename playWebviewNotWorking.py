# python3 -m venv .john
# source .john/bin/activate
# python3 -m pip install webview

import webview

# Create a webview window
window = webview.create_window("My Music Player", "https://tradexy.github.io/musicplayer/")

# Run the webview loop
webview.start(window)

# Wait for the page to load
time.sleep(5)

# Execute JavaScript to play the audio
window.evaluate_js("document.getElementById('music').play()")
