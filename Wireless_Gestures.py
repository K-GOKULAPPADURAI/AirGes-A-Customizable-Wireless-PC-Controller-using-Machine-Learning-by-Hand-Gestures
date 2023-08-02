# importing Python multiprocessing module


import multiprocessing
import cv2
import numpy as np
import HandTrackingModule as htm
import HandTrackingModul as ht
import time
import autopy
import pyautogui as p
#cap = cv2.VideoCapture("http://192.168.43.220:9000/stream.mjpg")
#cap = cv2.VideoCapture("http://192.168.43.1:6677/videofeed?username=CCJDMAFKB&password=")
    
cap = cv2.VideoCapture(0)
wCam, hCam = 1080, 720
cap.set(3, wCam)
cap.set(4, hCam)

def mousePointer():

    ######################
    frameR = 100     #Frame Reduction
    smoothening = 7  #random value
    ######################

    pTime = 0
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0
    #cap = cv2.VideoCapture("http://192.168.43.220:9000/stream.mjpg")
    #cap = cv2.VideoCapture(0)
   
    detector = ht.handDetector(maxHands=1)
    wScr, hScr = autopy.screen.size()

    # print(wScr, hScr)

    while True:
        # Step1: Find the landmarks
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)

        # Step2: Get the tip of the index and middle finger
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            # Step3: Check which fingers are up
            fingers = detector.fingersUp()
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                          (255, 0, 255), 2)

            # Step4: Only Index Finger: Moving Mode
            if fingers[1] == 1 and fingers[2] == 0:

                # Step5: Convert the coordinates
                x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

                # Step6: Smooth Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                # Step7: Move Mouse
                autopy.mouse.move(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

            # Step8: Both Index and middle are up: Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1:

                # Step9: Find distance between fingers
                length, img, lineInfo = detector.findDistance(8, 12, img)

                # Step10: Click mouse if distance short
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()

        # Step11: Frame rate
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (28, 58), cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)

        # Step12: Display
        cv2.imshow("Image", img)
        cv2.waitKey(1)


def fingerCounter():
    folderPath = "C:/Users/APPAtacker.py/Desktop/FigerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75)

    tipIds = [4, 8, 12, 16, 20]

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # print(fingers)
            totalFingers = fingers.count(1)
            print(totalFingers)

            h, w, c = overlayList[totalFingers - 1].shape
            img[0:h, 0:w] = overlayList[totalFingers - 1]

            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)

        cv2.imshow("Image1", img)
        cv2.waitKey(1)

if __name__ == "__main__":
# creating multiple processes

    proc1 = multiprocessing.Process(target=mousePointer)

    proc2 = multiprocessing.Process(target=fingerCounter)

    # Initiating process 1

    proc2.start()

    # Initiating process 2

    proc1.start()


