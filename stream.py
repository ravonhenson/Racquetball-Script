import cv2

class Stream:

    camera = cv2.VideoCapture(0)

    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, 
               cv2.TM_CCORR, cv2.TM_CCORR_NORMED, 
               cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    def run(self):
        while True:
            ret, frame = self.camera.read()
            cv2.imshow('ballistic calculator', frame)

            if cv2.waitKey(1) == 27:
                break

        self.camera.release()
        cv2.destroyAllWindows()



    