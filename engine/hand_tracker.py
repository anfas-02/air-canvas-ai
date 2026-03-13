import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        lmList = []
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                h, w, _ = img.shape
                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append((id, cx, cy))
                self.mpDraw.draw_landmarks(
                    img, handLms, self.mpHands.HAND_CONNECTIONS
                )
        return lmList

    def fingers_up(self, lmList):
        if not lmList:
            return []

        tips = [4, 8, 12, 16, 20]
        fingers = []

        # Thumb
        fingers.append(1 if lmList[tips[0]][1] > lmList[tips[0]-1][1] else 0)

        # Other fingers
        for i in range(1, 5):
            fingers.append(
                1 if lmList[tips[i]][2] < lmList[tips[i]-2][2] else 0
            )

        return fingers
