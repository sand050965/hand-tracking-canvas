import numpy as np

def initialize():
 global xp, yp, xp1, yp1, xpt, ypt, dist, drawColor, shape, isDrawingShape, imgCanvas
 xp, yp = 0, 0
 xp1, yp1 = 0, 0
 xpt, ypt = 0, 0
 dist = 0, 0
 drawColor = (255, 0, 255)
 shape = "painter"
 isDrawingShape = False
 imgCanvas = np.zeros((720, 1280, 3), np.uint8)
