#!/bin/bash

# Open the URL in a web browser
open "https://tradexy.github.io/musicplayer/"

# Wait for the page to load
sleep 5

# Execute JavaScript to play the audio
osascript -e "document.getElementById('music').play()"
