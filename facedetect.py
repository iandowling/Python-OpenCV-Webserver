
# import opencv
import cv2

# Face recognition files
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

# pass the cascade classifier to each frame
def faceRec(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facedetect = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    #Draw a rectangle around faces
    for (x, y, w, h) in facedetect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame
