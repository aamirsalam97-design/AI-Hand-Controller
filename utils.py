import cv2
import time


class FPSCounter:

    def __init__(self):
        self.pTime = time.time()

    def draw(self, img):
        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime

        cv2.putText(
            img,
            f"FPS: {int(fps)}",
            (20, 460),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

        return img