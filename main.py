import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, camera = cap.read()
    image = np.zeros((400, 580, 3), dtype=np.uint8)
    image = cv2.resize(image, (400, 580))

    # hands, camera = detector.findHands(camera)
    hands, camera = detector.findHands(camera, draw=True)
    totalFingers = 0

    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        bbox = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType1 = hand1["type"]

        fingers1 = detector.fingersUp(hand1)
        totalFingers = fingers1.count(1)
        handType2=""
        fingers2 = ["0"] * 5
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2["center"]
            handType2 = hand2["type"]
            fingers2 = detector.fingersUp(hand2)
            totalFingers += fingers2.count(1)


        os.system('cls')  # made for linux system only
        font = cv2.FONT_HERSHEY_PLAIN
        if(len(hands)==1 and handType1=="Right"):
            fingers2=list(fingers1)
            fingers1=["0","0","0","0","0"]
        # Use putText() method for
        cv2.putText(image,
                    'FINGERS      LEFT           RIGHT',
                    (50, 50),
                    font, 1,
                    (0, 255, 255),
                    2)

        cv2.putText(image,'Thumb',
                    (50, 100),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image,str(fingers1[0]),
                    (200, 100),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers2[0]),
                    (300, 100),
                    font, 1,
                    (0, 255, 255),
                    2)

        cv2.putText(image, 'Index',
                    (50, 150),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers1[1]),
                    (200, 150),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers2[1]),
                    (300, 150),
                    font, 1,
                    (0, 255, 255),
                    2)

        cv2.putText(image, 'Middle',
                    (50, 200),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers1[2]),
                    (200, 200),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers2[2]),
                    (300, 200),
                    font, 1,
                    (0, 255, 255),
                    2)

        cv2.putText(image, 'Ring',
                    (50, 250),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers1[3]),
                    (200, 250),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers2[3]),
                    (300, 250),
                    font, 1,
                    (0, 255, 255),
                    2)

        cv2.putText(image, 'Pinky',
                    (50, 300),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers1[4]),
                    (200, 300),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv2.putText(image, str(fingers2[4]),
                    (300, 300),
                    font, 1,
                    (0, 255, 255),
                    2)

        print("Fingers\tLeft\tRight\n")
        print("Thumb  \t", str(fingers1[0]), "   \t", str(fingers2[0]), "\n")
        print("Index  \t", str(fingers1[1]), "   \t", str(fingers2[1]), "\n")
        print("Middle  \t", str(fingers1[2]), "   \t", str(fingers2[2]), "\n")
        print("Ring  \t", str(fingers1[3]), "   \t", str(fingers2[3]), "\n")
        print("Pinky  \t", str(fingers1[4]), "   \t", str(fingers2[4]), "\n")

        cv2.putText(image, str(totalFingers), (40, 500), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
    camera = cv2.resize(camera, (640, 580))
    cv2.imshow("Image", np.hstack((image, camera)))
    cv2.waitKey(1)
