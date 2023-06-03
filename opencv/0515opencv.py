import cv2

circleradius = 1

def update(x):
    print(x)
    global circleradius
    circleradius = x
img = cv2.imread("photo.png")
cv2.namedWindow("win")
cv2.createTrackbar("bar","win",0,100,update)#創造一個能更改變數的輸入
center = (100,100)
color = (255,0,0)
thinkness = 2
# cv2.circle(img,center,circleradius,color,thinkness)
# cv2.imshow("win",img)
# cv2.waitKey(0)
while cv2.waitKey(100) != 27:
    circleimg = img.copy()
    cv2.circle(circleimg,center,circleradius,color,thinkness)
    cv2.imshow("win",circleimg)
    continue



