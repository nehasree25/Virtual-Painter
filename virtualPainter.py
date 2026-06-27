import cv2
import mediapipe as mp
import numpy as np
import time
import os
import handDetection
folderPath = "Paint_Images"
myList = os.listdir(folderPath)

overLayList = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overLayList.append(image)
imgCanvas = np.zeros((720,1280,3),np.uint8)
header = overLayList[0]
cap = cv2.VideoCapture(0)
cap.set(3, 1280)   # Width
cap.set(4, 720)    # Height
detector = handDetection.HandDetector(detectionCon=0.85)
drawColor = (255,0,255)
xp, yp = 0, 0
brushThickness = 15
eraserThickness = 35
while True:
    # 1. import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.detect_hands(img)
    lmList = detector.get_landmark_positions(img)
    if len(lmList) != 0:
        # tip of index and middle fingers
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]

    # 3. Check which fingers are up
    fingers = detector.fingers_up()


    # 4. If Selection Mode - Two fingers are up
    if len(fingers)!=0:
        if fingers[1] and fingers[2]:
            cv2.rectangle(img, (x1, y1-25), (x2, y2+25), drawColor, cv2.FILLED)
            if y1 < 125:
                if 225 < x1 < 360:
                    header = overLayList[0]
                    drawColor = (255,0,255)   # Pink brush

                elif 375 < x1 < 510:
                    header = overLayList[1]  
                    drawColor = (0,165,255)   # Orange brush

                elif 530 < x1 < 665:
                    header = overLayList[2] 
                    drawColor = (0,255,0)   # Green brush

                elif 680 < x1 < 815:
                    header = overLayList[3]  
                    drawColor = (0,255,255)   # Yellow brush

                elif 925 < x1 < 1085:
                    header = overLayList[4] 
                    drawColor = (0,0,0)   # Eraser
        # 5. If Drawing Mode - Index finger is up
        if fingers[1] and fingers[2]==0:
            cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
            if xp==0 and yp==0:
                xp,yp = x1,y1
            if drawColor==(0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness)
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
            else:
                cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
            xp,yp = x1,y1
            
    if not success:
        break

    # Setting the header image
    img[0:125, 0:1280] = header
    img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
    cv2.imshow("Image", img)
    cv2.imshow("Canvas", imgCanvas)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
