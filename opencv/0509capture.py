import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"555")
out=cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480))
while cv2.VideoWriter(1)!=27:
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow("frame",frame)
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
