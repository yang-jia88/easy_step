import cv2
import detect_face
video = cv2.VideoCapture = ("output_2.mp4")

while cv2.waitkey(1) != 27:
    ret , frame = video.read()
    new_frame = detect_face(frame,ret)
    if ret == False:break
    cv2.imshow("frame",new_frame)

video.release()
cv2.destroyAllWindows()