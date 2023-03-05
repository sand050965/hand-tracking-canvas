import models.handTrackingModule as htm

class VideoFeed():
    def __init__(self):
        pass

    def pre_gen(camera):
        frame = camera.pre_get_frame()
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + 
                frame + b'\r\n\r\n')

    def gen(camera):
        brushThickness = 15
        eraserThickness = 100
        detector = htm.HandDetector(detectionCon=0.85)
        while True:
            frame = camera.get_frame(
                detector, brushThickness, eraserThickness)
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + 
                  frame + b'\r\n\r\n')