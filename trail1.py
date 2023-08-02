import cv2
import time
import os
import HandTrackingModule as htm
import pyautogui as p
p.FAILSAFE=False
print("#####################Welcome to Hand Gesture controlled pc#####################")
appMode={2:'Microsoft excel',3:'Microsoft word',5:'VLC Media player',4:'Chrome',1:'Microsoft Power point'}
print(appMode)
choice=int(input("Enter the presentation application:    "))
wCam, hCam = 1080, 720


#cap = cv2.VideoCapture("http://192.168.43.220:9000/stream.mjpg")
#cap = cv2.VideoCapture("http://192.168.43.1:6677/videofeed?username=CCJDMAFKB&password=")
#cap=cv2.VideoCapture(0)
#l="http://192.168.43.1:6677/videofeed?username=CCJDMAFKB&password="
cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FigerImages"
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

    l=[]
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
        l.append(totalFingers)
        print(l)
        
        if appMode[choice]=='Microsoft Power point':   
            if(totalFingers==0):
                time.sleep(2)
                p.hotkey('f5')
            if(totalFingers==1):
                time.sleep(2)
                 #p.hotkey('ctrl', 't')
                p.press('left')
            if(totalFingers==2):
                time.sleep(2)
                 #p.hotkey('ctrl', 'n')
                p.press('right')
            if(totalFingers==3):
                time.sleep(2)
                 #p.hotkey('ctrl', 'w')
                p.press('esc')
            if(totalFingers==4):
                time.sleep(2)
                p.hotkey('fn','alt','f4')
        elif appMode[choice]=='Microsoft excel':
            if(totalFingers==0):
                time.sleep(2)
                p.hotkey('fn','alt','f4')
            if(totalFingers==1):
                time.sleep(2)
                 #p.hotkey('ctrl', 't')
                p.press('left')
            if(totalFingers==2):
                time.sleep(2)
                 #p.hotkey('ctrl', 'n')
                p.press('right')
            if(totalFingers==3):
                time.sleep(2)
                 #p.hotkey('ctrl', 'w')
                p.press('up')
            if(totalFingers==4):
                time.sleep(2)
                p.press('down')
                 
        elif appMode[choice]=='Microsoft word':
            if(totalFingers==0):
                time.sleep(2)
                p.hotkey('fn','alt','f4')
            if(totalFingers==1):
                time.sleep(2)
                 #p.hotkey('ctrl', 't')
                p.press('left')
            if(totalFingers==2):
                time.sleep(2)
                 #p.hotkey('ctrl', 'n')
                p.press('right')
            if(totalFingers==3):
                time.sleep(2)
                 #p.hotkey('ctrl', 'w')
                p.press('up')
            if(totalFingers==4):
                time.sleep(2)
                p.press('down')
            
        elif appMode[choice]=='Chrome':
            if(totalFingers==0):
                time.sleep(2)
                p.hotkey('fn','alt','f4')
            if(totalFingers==1):
                time.sleep(2)
                 #p.hotkey('ctrl', 't')
                p.hotkey('ctrl','tab')
            if(totalFingers==2):
                time.sleep(2)
                 #p.hotkey('ctrl', 'n')
                p.hotkey('ctrl','t')
            if(totalFingers==3):
                time.sleep(2)
                 #p.hotkey('ctrl', 'w')
                p.hotkey('up')
            if(totalFingers==4):
                time.sleep(2)
                p.hotkey('down')
        elif appMode[choice]=='VLC Media player':
            if(totalFingers==0):
                time.sleep(2)
                p.hotkey('space')
            if(totalFingers==1):
                 #p.hotkey('ctrl', 't')
                time.sleep(2)
                p.press('left')
            if(totalFingers==2):
                 #p.hotkey('ctrl', 'n')
                time.sleep(2)
                p.press('right')
            if(totalFingers==3):
                time.sleep(2)
                 #p.hotkey('ctrl', 'w')
                p.press('up')
            if(totalFingers==4):
                time.sleep(2)
                p.press('down')
            
        
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

    cv2.imshow("Image", img)
    cv2.waitKey(1)

