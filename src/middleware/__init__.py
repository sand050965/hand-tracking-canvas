from flask import *
from routes.index_route import index_api

def create_app():
    app = Flask(__name__, template_folder='../views/',
                static_folder='../static/')

    app.register_blueprint(index_api)
    
    return app
