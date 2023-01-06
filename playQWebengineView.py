# python3 -m venv .john
# source .john/bin/activate
# python3 -m pip install pyqt5
import pyqt5.qtwebengine

# Create a QWebEngineView widget
view = pyqt5.QtWebEngineWidgets.QWebEngineView()

# Load the URL
view.load(pyqt5.QUrl("https://tradexy.github.io/musicplayer/"))

# Show the widget
view.show()

# Wait for the page to load
pyqt5.QtTest.QTest.qWait(5000)

# Execute JavaScript to play the audio
view.page().runJavaScript("document.getElementById('music').play()")
