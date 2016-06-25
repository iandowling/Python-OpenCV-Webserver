
# opencv import an time
import time
import cv2
import facedetect

#Camera class 
class Camera(object):

    # open camera stream
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 800)
        self.cam.set(4, 600)
        time.sleep(1)

    # read in the video frame, 
    # pass the faceRec method from facedetect.py on each frame
    # return the frame as a jpg
    def get_frame(self):
        ret, video = self.cam.read()
        video = facedetect.faceRec(video)
        ret2, jpeg = cv2.imencode('.jpeg', video)
        return jpeg.tostring()

    # close the connection
    def __del__(self):
        self.cam.release()