from flask import *
from controllers.videoFeed import VideoFeed
from models.facecam import Facecam

index_api = Blueprint("index_api", __name__)


@index_api.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@index_api.route("/video_feed", methods=['GET'])
def videoFeed():
    return Response(VideoFeed.gen(Facecam()), mimetype='multipart/x-mixed-replace; boundary=frame')
