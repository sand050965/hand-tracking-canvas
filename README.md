# Hand-Tracking-Canvas 

[MacOS]
pyinstaller --onefile --noconsole -w --icon=static/images/favicon.icns --add-data "templates:templates" --add-data "static:static" --add-data "mediapipe/modules:mediapipe/modules" app.py


[windows]
pyinstaller -F -w --i "C:\Code\Hand-Tracking-Canvas\src\static\images\favicon.ico" --add-data "C:\Code\Hand-Tracking-Canvas\src\templates\;templates" --add-data "C:\Code\Hand-Tracking-Canvas\src\static\;static" --add-data "C:\Code\Hand-Tracking-Canvas\src\mediapipe\modules;mediapipe\modules" app.py

pyinstaller app.spec