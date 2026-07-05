import math
import time
import cv2
import pyautogui
pyautogui.FAILSAFE = False
from hand_detector import HandDetector

# Webcam
cap = cv2.VideoCapture(0)

# Screen Size
screen_w, screen_h = pyautogui.size()

# Hand Detector
detector = HandDetector()

# Smoothness
smoothening = 5
click_time = 0
click_delay = 0.5

plocX, plocY = 0, 0
clocX, clocY = 0, 0

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = detector.findHands(img)

    lmList = detector.findPosition()

    if len(lmList) != 0:

        x1, y1 = lmList[8][1], lmList[8][2]
        # Thumb Tip
x2, y2 = lmList[4][1], lmList[4][2]

# Distance between Thumb and Index
distance = math.hypot(x2 - x1, y2 - y1)

# Left Click
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

        cam_h, cam_w, _ = img.shape

        screen_x = x1 * screen_w / cam_w
        screen_y = y1 * screen_h / cam_h

        clocX = plocX + (screen_x - plocX) / smoothening
        clocY = plocY + (screen_y - plocY) / smoothening

        pyautogui.moveTo(clocX, clocY)

        plocX, plocY = clocX, clocY

        cv2.circle(img, (x1, y1), 12, (255, 0, 255), cv2.FILLED)

    cv2.imshow("AI Hand Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows(import cv2
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

# Smoothness
smoothening = 5

plocX, plocY = 0, 0
clocX, clocY = 0, 0

click_time = 0
click_delay = 0.5

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition()

    if len(lmList) != 0:

        # Index Finger
        x1, y1 = lmList[8][1], lmList[8][2]

        # Thumb
        x2, y2 = lmList[4][1], lmList[4][2]

        # Distance
        distance = math.hypot(x2 - x1, y2 - y1)

        # Camera Size
        cam_h, cam_w, _ = img.shape

        # Mouse Movement
        screen_x = x1 * screen_w / cam_w
        screen_y = y1 * screen_h / cam_h

        clocX = plocX + (screen_x - plocX) / smoothening
        clocY = plocY + (screen_y - plocY) / smoothening

        pyautogui.moveTo(clocX, clocY)

        plocX, plocY = clocX, clocY

        # Left Click
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

        cv2.circle(img, (x1, y1), 12, (255, 0, 255), cv2.FILLED)

    cv2.imshow("AI Hand Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()