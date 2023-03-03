from flask import *

def create_app():
    app = Flask(__name__, template_folder='./views/',
                static_folder='./static/')

    return app
