import pyautogui

pyautogui.FAILSAFE = False


class MouseController:

    def __init__(self):
        self.screen_w, self.screen_h = pyautogui.size()
        self.plocX = 0
        self.plocY = 0
        self.smoothening = 7

    def move(self, x, y, cam_w, cam_h, frameR=100):

        x = max(frameR, min(x, cam_w - frameR))
        y = max(frameR, min(y, cam_h - frameR))

        screen_x = (x - frameR) * self.screen_w / (cam_w - 2 * frameR)
        screen_y = (y - frameR) * self.screen_h / (cam_h - 2 * frameR)

        clocX = self.plocX + (screen_x - self.plocX) / self.smoothening
        clocY = self.plocY + (screen_y - self.plocY) / self.smoothening

        pyautogui.moveTo(clocX, clocY)

        self.plocX = clocX
        self.plocY = clocY

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def scroll(self, amount):
        pyautogui.scroll(amount)