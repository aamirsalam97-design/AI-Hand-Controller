import cv2
import time

from hand_detector import HandDetector
from mouse_controller import MouseController
from gesture_controller import GestureController
from utils import FPSCounter


cap = cv2.VideoCapture(0)

detector = HandDetector()
mouse = MouseController()
fps = FPSCounter()

click_time = 0
click_delay = 0.5

scroll_time = 0
scroll_delay = 0.2


while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = detector.findHands(img)

    lmList = detector.findPosition()

    if len(lmList) != 0:

        x1, y1 = lmList[8][1], lmList[8][2]

        cam_h, cam_w, _ = img.shape

        mouse.move(x1, y1, cam_w, cam_h)

        cv2.circle(img, (x1, y1), 12, (255, 0, 255), cv2.FILLED)

    img = fps.draw(img)

    cv2.imshow("AI Virtual Mouse Pro", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()