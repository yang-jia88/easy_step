import cv2
a=[[123,34,57,62,"dog"],[55,66,99,400,"cat"]]
position=[(555,99),(888,99)]
img=cv2.imread("0.jpg")


def write_text(img,text,pos):
    position=pos
    size=2
    color=(233,0,0)
    linewidth=5
    write=cv2.putText(img,text,position,cv2.FONT_HERSHEY_SIMPLEX,size,color,linewidth)
    return write

def draw_rectangle(img,local):
    p1=(local[0],local[1])
    p2=(local[2],local[3])
    color=(0,255,0)
    rectangleimg = cv2.rectangle(img,p1,p2,color,2)
    return rectangleimg

def result(img,j,issave):
    if issave==True:
        cv2.imwrite(str(j)+"save_img.jpg",img)

def ending(firstnum,recandtext,position):
    for i in recandtext:
        write_text(img,str(firstnum)+i[4],position[firstnum])
        draw_rectangle(img,i)
        result(img,firstnum,True)
        firstnum+=1
        
ending(5,a,position)

