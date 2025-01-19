import cv2 
import numpy as np 

circles=np.zeros((4,2))
counter=0

def mousepoints(event,x,y,flags,params):
    global counter
    if event==cv2.EVENT_LBUTTONDBLCLK:
       
        circles[counter]= x,y 
        counter=counter+1 
      
        
      
         

img=cv2.imread('image.webp')

while True:
    if counter==4:
        width,height=500,250
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix=cv2.getPerspectiveTransform(pts1,pts2)
        output=cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("output image",output)
        
    for i in range(4):
        cv2.circle(img, (int(circles[i][0]), int(circles[i][1])), 1, (0, 0, 255), cv2.FILLED)
    cv2.imshow("original image",img)


    cv2.setMouseCallback("original image",mousepoints)

    key = cv2.waitKey(1) & 0xFF  # Get key press
    if key == ord('q'):  # If 'q' is pressed, break the loop
        print("Exiting program.")
        break

cv2.destroyAllWindows()       