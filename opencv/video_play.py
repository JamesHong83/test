import cv2

capture = cv2.VideoCapture('output.avi')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
# writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

while(1):
    ret,img_color = capture.read()

    if ret == 0:
        break
    
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
    
    cv2.imshow("Video Capture_Color", img_color)
    cv2.imshow("Video Capture_Gray", img_gray)
    
    #writer.write(img_color)

    if cv2.waitKey(1)&0xFF==27:
        break

capture.release()
# writer.release()

cv2.destroyAllWindows()