import cv2
import mediapipe as mp

class HandDetector():
    def __init__(self, mode=False, maxHands=2, modelComplex=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplex
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.handLandmarksStyle = self.mpDraw.DrawingSpec(
            color=(0, 0, 255), thickness=10)
        self.handConnectionsStyle = self.mpDraw.DrawingSpec(
            color=(0, 255, 0), thickness=5)
        self.tipIds = [4, 8, 12, 16, 20]
        
    
    def findHands(self, frame, draw = True):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(frameRGB)
        
        if self.results.multi_hand_landmarks:
            for landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        frame, landmarks, self.mpHands.HAND_CONNECTIONS, self.handLandmarksStyle, self.handConnectionsStyle)
         
        return frame 
                
    def findPosition(self, frame, handNum = 0, draw = True):
        self.landmarkList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNum]
            
            for id, lm in enumerate(myHand.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.landmarkList.append([id, cx, cy])
                if draw:
                    cv2.circle(frame, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return self.landmarkList
                    
    def checkFingersUp(self):
        self.fingers = []
        
        # Thumb
        if self.landmarkList[self.tipIds[0]][1] < self.landmarkList[self.tipIds[0] - 1][1]:
            self.fingers.append(1)
        else:
            self.fingers.append(0)
            
        # 4 Fingers
        for id in range(1, 5):
            if self.landmarkList[self.tipIds[id]][2] < self.landmarkList[self.tipIds[id] - 2][2]:
                self.fingers.append(1)
            else:
                self.fingers.append(0)
         
        return self.fingers
