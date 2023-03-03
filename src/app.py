from flask import *
from flask_socketio import *
from middleware.__init__ import create_app
from controllers.video import Video
from models.facecam import Facecam

app = create_app()

socketio = SocketIO(app)

@socketio.on('catch-frame')
def catch_frame(data):
    emit('processed-image', data)


@socketio.on("image")
def receive_image(image):
    # Decode the base64-encoded image data
    image = Video.gen(Facecam(image))
    
    # Prepend the base64-encoded string with the data URL prefix
    image = "data:image/jpg;base64," + image

    # Send the processed image back to the client
    emit("processed-image", image)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=3000)
