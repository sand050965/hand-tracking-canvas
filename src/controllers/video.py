import numpy as np
import models.handTrackingModule as htm

class Video():
    def __init__(self):
        pass

    def gen(camera):
        brushThickness = 15
        eraserThickness = 100
        detector = htm.HandDetector(detectionCon=0.85)
        while True:
            proccessedFrame = camera.get_frame(
                detector, brushThickness, eraserThickness)
            return proccessedFrame