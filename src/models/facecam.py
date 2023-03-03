import cv2
import base64
import numpy as np
import globals

class Facecam(object):  
    globals.initialize()
    
    def __init__(self, frame):
        self.frame = frame
        
    def base64_to_image(self, base64_string):
        # Extract the base64 encoded binary data from the input string
        base64_data = base64_string.split(",")[1]
        # Decode the base64 data to bytes
        image_bytes = base64.b64decode(base64_data)
        # Convert the bytes to numpy array
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        # Decode the numpy array as an image using OpenCV
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return image
        
    def get_frame(self, detector, brushThickness, eraserThickness):
        frame = self.base64_to_image(self.frame)
        frame = cv2.resize(frame, (1280, 720))

        # Find Hand Landmarks
        frame = cv2.flip(frame, 1)
        frame = detector.findHands(frame)
        landmarkList = detector.findPosition(frame, draw=False)

        if len(landmarkList) != 0:
            # tip of index and middle finger
            x1, y1 = landmarkList[8][1:]
            x2, y2 = landmarkList[12][1:]

            # Check which fingers are up
            fingers = detector.checkFingersUp()

            # If Selection Mode (2 fingers are up)
            if fingers[1] and fingers[2]:
                globals.xp, globals.yp = 0, 0

                if y1 < 125:
                    if 256 < x1 < 512:
                        globals.drawColor = (255, 0, 255)
                    elif 512 < x1 < 768:
                        globals.drawColor = (255, 0, 0)
                    elif 768 < x1 < 1024:
                        globals.drawColor = (0, 255, 0)
                    elif 1024 < x1 < 1280:
                        globals.drawColor = (0, 0, 0)
                elif y1 > 125 and x1 < 128:
                    if 125 < y1 < 273:
                        globals.shape = "painter"
                    elif 273 < y1 < 421:
                        globals.shape = "circle"
                    elif 421 < y1 < 569:
                        globals.shape = "rectangle"
                    elif 444 < y1 < 720:
                        globals.shape = "line"  
                else:
                    if globals.isDrawingShape:
                        # circle
                        if globals.shape == "circle":
                            globals.isDrawingShape = False
                            cv2.circle(globals.imgCanvas, (globals.xp1, globals.yp1), globals.dist,
                                    globals.drawColor, 5)

                        # rectangle
                        elif globals.shape == "rectangle":
                            globals.isDrawingShape = False
                            cv2.rectangle(globals.imgCanvas, (globals.xpt, globals.ypt), (globals.xp1, globals.yp1),
                                        globals.drawColor, 5)

                        # oval
                        elif globals.shape == "line":
                            globals.isDrawingShape = False
                            cv2.line(globals.imgCanvas, (globals.xpt, globals.ypt), (globals.xp1, globals.yp1),
                                          globals.drawColor, 5)
                     
                cv2.rectangle(frame, (x1, y1 - 25), (x2, y2 + 25),
                              globals.drawColor, cv2.FILLED)

            # If Drawing Mode (1 fingers are up)
            if not (fingers[1] and fingers[2]):
                
                xt, yt = landmarkList[4][1:]
                
                cv2.circle(frame, (x1, y1), 15,
                           globals.drawColor, cv2.FILLED)
                
                if globals.xp == 0 and globals.yp == 0:
                    globals.xp, globals.yp = x1, y1
                    
                if globals.drawColor == (0, 0, 0):
                    cv2.line(frame, (globals.xp, globals.yp), (x1, y1),
                             globals.drawColor, eraserThickness)
                    cv2.line(globals.imgCanvas, (globals.xp, globals.yp), (x1, y1),
                             globals.drawColor, eraserThickness)
                else:
                    # draw
                    if globals.shape == "painter":
                        cv2.line(frame, (globals.xp, globals.yp), (x1, y1),
                                globals.drawColor, brushThickness)
                        cv2.line(globals.imgCanvas, (globals.xp, globals.yp), (x1, y1),
                                globals.drawColor, brushThickness)
                    # circle
                    elif globals.shape == "circle":
                        globals.isDrawingShape = True
                        dist = int((((yt - y1) ** 2) + ((xt - x1) ** 2)) ** 0.5)
                        cv2.circle(frame, (x1, y1), dist,
                                   globals.drawColor, 5)
                        globals.xp1, globals.yp1 = x1, y1
                        globals.dist = dist
                            
                    # rectangle
                    elif globals.shape == "rectangle":
                        globals.isDrawingShape = True
                        cv2.rectangle(frame, (xt, yt), (x1, y1),
                                      globals.drawColor, 5)
                        globals.xp1, globals.yp1 = x1, y1
                        globals.xpt, globals.ypt = xt, yt
                            
                    # oval
                    elif globals.shape == "line":
                        globals.isDrawingShape = True
                        cv2.line(frame, (xt, yt), (x1, y1),
                                      globals.drawColor, 5)
                        globals.xp1, globals.yp1 = x1, y1
                        globals.xpt, globals.ypt = xt, yt
                    
                globals.xp, globals.yp = x1, y1
        
        if globals.drawColor == (255, 0, 255):
            cv2.putText(frame, "red", (70, 45),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, globals.drawColor, 2)
        elif globals.drawColor == (255, 0, 0):
            cv2.putText(frame, "blue", (70, 45),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, globals.drawColor, 2)
        elif globals.drawColor == (0, 255, 0):
            cv2.putText(frame, "green", (70, 45),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, globals.drawColor, 2)
        elif globals.drawColor == (0, 0, 0):
            cv2.putText(frame, "eraser", (70, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, globals.drawColor, 2)
        
        if globals.drawColor != (0, 0, 0):
            if globals.shape == "painter":
                cv2.putText(frame, "painter", (70, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, globals.drawColor, 2)
            elif globals.shape == "circle":
                cv2.putText(frame, "circle", (70, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, globals.drawColor, 2)
            elif globals.shape == "rectangle":
                cv2.putText(frame, "rectangle", (70, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, globals.drawColor, 2)
            elif globals.shape == "line":
                cv2.putText(frame, "line", (70, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, globals.drawColor, 2)

        imgHSV = cv2.cvtColor(globals.imgCanvas, cv2.COLOR_BGR2HSV)
        imgGray = cv2.cvtColor(imgHSV, cv2.COLOR_BGR2GRAY)
        _, imgInverse = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInverse = cv2.cvtColor(imgInverse, cv2.COLOR_GRAY2BGR)
        frame = cv2.bitwise_and(frame, imgInverse)
        frame = cv2.bitwise_or(frame, globals.imgCanvas)
        jpeg = cv2.imencode(
            '.jpeg', frame, [cv2.IMWRITE_JPEG_QUALITY, 40])[1]
        return base64.b64encode(jpeg).decode()
