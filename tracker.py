import cv2
import numpy as np
import time
from collections import deque
import argparse
import imutils
from imutils.video import VideoStream

class Tracker:

    def __init__(self, lowerHSV, upperHSV):
        self.lowerHSV = lowerHSV
        self.upperHSV = upperHSV

    
