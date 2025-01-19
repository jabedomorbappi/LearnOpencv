import cv2
path="first/oen.png"
img=cv2.imread(path)
width,height=400,400
imgresize=cv2.resize(img,(width,height))
imgcrop=img[60:300,50:]


cv2.imshow("original image",img)
cv2.imshow("resized image",imgcrop)
cv2.waitKey(0)