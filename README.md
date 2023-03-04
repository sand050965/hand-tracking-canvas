# Hand-Tracking-Canvas 

pyinstaller --onefile --noconsole -w --icon=static/images/favicon.icns --add-data "templates:templates" --add-data "static:static" --add-data "mediapipe/modules:mediapipe/modules" app.py
pyinstaller app.spec