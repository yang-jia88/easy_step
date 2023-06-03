import cv2
# for i in range(x):
#     IMG=cv2.imread(str(x)+".jpg")
#     cv2.imshow(str(i)+"image",IMG)
#     cv2.waitKey(0)


IMG=cv2.imread("photo.png")
cv2.imshow("image",IMG)
def show_circle(center,color):
    radius=10
    newImg=cv2.circle(IMG,center,radius,color,2)
    return newImg

center=(100,300)
radius=10
color=(0,0,255)
newImg=cv2.circle(IMG,center,radius,color,2)
cv2.imshow("image",newImg)
cv2.waitKey(0)
# # while cv2.waitKey(100)!=50:
# #     if cv2.getWindowProperty("image",cv2.WND_PROP_VISIBLE)<=0:
# #         break
# # print("end program")
# cv2.waitKey(0)
