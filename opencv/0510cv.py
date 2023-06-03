import cv2
a=[[123,34,57,62,"dog"],[55,66,99,400,"cat"]]

img=cv2.imread("terria.png")

def show_result(img,a,issave):#給他框框
    j=0
    color=(0,255,0)
    for i in a:
        p1=(i[0],i[1])
        p2=(i[2],i[3])
        rectangleimg = cv2.rectangle(img,p1,p2,color,2)
        if issave==True:
            cv2.imwrite(str(j)+"save_img.jpg",rectangleimg)
            j+=1

    # cv2.imshow(i[4],rectangleimg)
    #cv2.waitKey(0)S
    return rectangleimg
def show_word(img,a):#先做文字
    # img=cv2.imread("0.jpg")
    position=[(111,99),(123,546)]
    size=2
    color=(233,0,0)
    linewidth=5
    j=0
    for i in a:
        cv2.putText(img,str(j)+i[4],position[j],cv2.FONT_HERSHEY_SIMPLEX,size,color,linewidth)
        j+=1
    cv2.imshow("cool",img)
    cv2.waitKey(0)
    return 
for i in a:

    show_result(show_word(img,a),a,True)