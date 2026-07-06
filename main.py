import cv2
import pyautogui
import math
import time
from hand_detector import HandDetector

pyautogui.FAILSAFE = False

# Webcam
cap = cv2.VideoCapture(0)

# Screen Size
screen_w, screen_h = pyautogui.size()

# Hand Detector
detector = HandDetector()

smoothening = 7

plocX, plocY = 0, 0
clocX, clocY = 0, 0

click_time = 0
click_delay = 0.5

scroll_delay = 0.2
scroll_time = 0

dragging = False

double_click_time = 0
double_click_delay = 0.5

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition()

    if len(lmList) != 0:

        x1, y1 = lmList[8][1], lmList[8][2]
        x2, y2 = lmList[4][1], lmList[4][2]
        # Middle Finger
        x3, y3 = lmList[12][1], lmList[12][2]
        # Ring Finger
        x4, y4 = lmList[16][1], lmList[16][2]
        # Pinky Finger
        x5, y5 = lmList[20][1], lmList[20][2]
        
        index_up = lmList[8][2] < lmList[6][2]
        middle_up = lmList[12][2] < lmList[10][2]
        ring_up = lmList[16][2] < lmList[14][2]
        pinky_up = lmList[20][2] < lmList[18][2]
        
        distance = math.hypot(x2 - x1, y2 - y1)
        right_distance = math.hypot(x2 - x3, y2 - y3)
        scroll_distance = math.hypot(x2 - x4, y2 - y4)
        double_distance = math.hypot(x2 - x5, y2 - y5)

        cam_h, cam_w, _ = img.shape

        frameR = 100

        x3 = max(frameR, min(x1, cam_w - frameR))
        y3 = max(frameR, min(y1, cam_h - frameR))

        screen_x = (x3 - frameR) * screen_w / (cam_w - 2 * frameR)
        screen_y = (y3 - frameR) * screen_h / (cam_h - 2 * frameR)

        clocX = plocX + (screen_x - plocX) / smoothening
        clocY = plocY + (screen_y - plocY) / smoothening

        pyautogui.moveTo(clocX, clocY)

        plocX, plocY = clocX, clocY

        current_time = time.time()

        if distance < 20 and current_time - click_time > click_delay:
            pyautogui.click()
            click_time = current_time

            cv2.putText(
                img,
                "LEFT CLICK",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3
            )
            
        if right_distance < 20 and current_time - click_time > click_delay:
            pyautogui.rightClick()
            click_time = current_time

            cv2.putText(
                img,
                "RIGHT CLICK",
                (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                3
            )    
            
        if scroll_distance < 20 and time.time() - scroll_time > scroll_delay:

            if y4 < y2:
                pyautogui.scroll(150)

                cv2.putText(
                    img,
                    "SCROLL UP",
                    (20, 130),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 0),
                    3
                )

            else:
                pyautogui.scroll(-150)

                cv2.putText(
                    img,
                    "SCROLL DOWN",
                    (20, 130),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 0),
                    3
                )

            scroll_time = time.time()
                    # Drag & Drop

        if (not index_up and
           not middle_up and
           not ring_up and
           not pinky_up):

            if not dragging:
                pyautogui.mouseDown()
                dragging = True

                cv2.putText(
                    img,
                    "DRAGGING",
                    (20, 210),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

        else:

            if dragging:
                pyautogui.mouseUp()
                dragging = False

        cv2.circle(img, (x1, y1), 12, (255, 0, 255), cv2.FILLED)

    cv2.imshow("AI Hand Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()