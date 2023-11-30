import cv2
import numpy as np
import matplotlib.pyplot as plt

class Detection:

    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, 
               cv2.TM_CCORR, cv2.TM_CCORR_NORMED, 
               cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    def __init__(self, imageFileName, templateFileName):
        #need grayscale for algorithm
        self.imageFileName = imageFileName
        self.templateFileName = templateFileName
        self.image = cv2.imread(f"images/{imageFileName}", cv2.IMREAD_GRAYSCALE)
        self.template = cv2.imread(f"images/{templateFileName}", cv2.IMREAD_GRAYSCALE)
        self.w, self.h = self.template.shape[::-1]

    def match(self):
        for method in self.methods:
            img = self.image.copy()

            res = cv2.matchTemplate(img, self.template, method)
            in_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + self.w, top_left[1] + self.h)
            cv2.rectangle(img,top_left, bottom_right, 255, 2)
            plt.subplot(121),plt.imshow(res,cmap = 'gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(img,cmap = 'gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(method)
            plt.show()    

detector = Detection('target.jpg', 'target.png')
detector.match()