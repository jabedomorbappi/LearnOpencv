import numpy as np
import cv2

image_path = "image.webp"
image = cv2.imread(image_path)

width,height=500,250
pts1 = np.float32([[264, 218], [831, 112], [369, 512], [947, 401]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)

output=cv2.warpPerspective(image,matrix,(width,height))
# Draw a red circle at the first point in pts1
for i in range(4):
    
    cv2.circle(image, (int(pts1[i][0]), int(pts1[i][1])), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("image", image)
cv2.imshow('cut',output)
cv2.waitKey(0)
