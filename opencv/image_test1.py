import cv2

img_color = cv2.imread('c:\image\gate_b.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('Show Color image')
cv2.imshow('Show Color image', img_color)

cv2.waitKey(0)

# change to gray scale  
img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)

cv2.imshow('Show GrayScale image', img_gray)
cv2.waitKey(0)

cv2.imwrite('gate_b_grayscale.jpg', img_gray)

cv2.destroyAllWindows()