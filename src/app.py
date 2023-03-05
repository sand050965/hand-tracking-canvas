import os
import webview
from flask import *
from middleware.__init__ import create_app

app = create_app()

def on_closed():
    print('Destroying window..')
    os._exit(0)
    
if __name__ == '__main__':
    window = webview.create_window(
        'Hand Tracking Canvas', app, min_size=(2560, 1440))
    window.events.closed += on_closed
    webview.start()
