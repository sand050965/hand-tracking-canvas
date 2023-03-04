import sys, os
from flask import *
from routes.app_route import app_api

def create_app():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    template_folder = os.path.join(base_path, 'templates')
    static_folder = os.path.join(base_path, 'static')
    app = Flask(__name__, template_folder=template_folder,
                    static_folder=static_folder)
        
    app.register_blueprint(app_api)
    
    return app
