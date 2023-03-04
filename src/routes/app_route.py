from flask import *
from controllers.videoFeed import VideoFeed
from models.facecam import Facecam

app_api = Blueprint("app_api", __name__)


@app_api.route("/")
def index():
    return render_template("index.html")

@app_api.route("/canvas")
def canvas():
    return render_template("canvas.html")

@app_api.route("/video")
def videoFeed():
    return Response(VideoFeed.gen(Facecam()), mimetype='multipart/x-mixed-replace; boundary=frame')
