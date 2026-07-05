class GestureController:

    def getFingerCount(self, lmList):

        if len(lmList) == 0:
            return 0

        fingers = []

        tipIds = [4, 8, 12, 16, 20]

        # Thumb
        if lmList[4][1] > lmList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other fingers
        for i in range(1, 5):
            if lmList[tipIds[i]][2] < lmList[tipIds[i]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers.count(1)