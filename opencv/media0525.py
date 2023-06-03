import mediapipe as mp
import cv2 as cv

face_det = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


img = cv.imread("three.png")
newimg = cv.cvtColor(img,cv.COLOR_BGR2RGB)
faceDetction = face_det.FaceDetection(model_selection = 1)
result = faceDetction.process(newimg)
print(result.detections)
for result in result.detections:
    mp_drawing.draw_detection(img,result)
cv.imshow("result",img)
cv.waitKey(0)
# print(result.detections)
# model_selection = 1
