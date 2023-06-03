import cv2

def ReviseFrame(frame,scale = 0.75):
    #all can do
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)
def changeRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)


capture = cv2.VideoCapture(0)



while True :
    isTrue , frame = capture.read()
    framerevize = ReviseFrame(frame)
    cv2.imshow("cool20",frame)
    cv2.imshow("cool",framerevize)
    if cv2.waitKey(100) == 27:
        break

capture.release()
cv2.destroyAllWindows