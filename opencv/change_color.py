import cv2

img = cv2.imread("terria.png")
color=str(input("輸入顏色:(black or same or blue to red) "))
if color == "black":
    newimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("black_photo.png",newimg)
elif color == "same":
    cv2.imwrite("same_photo.png",img)
else:
    newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite("B2R.PNG",newimg)