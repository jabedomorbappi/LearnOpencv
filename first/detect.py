import cv2 
def mousepoints(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
         

img=cv2.imread('first/oen.png')
cv2.imshow("original image",img)
cv2.setMouseCallback("original image",mousepoints)
cv2.waitKey(0)        