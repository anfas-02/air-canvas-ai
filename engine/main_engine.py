import cv2
import time
from hand_tracker import HandTracker
from predictor import Predictor
from canvas_manager import CanvasManager

def run():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    predictor = Predictor()
    canvas_manager = CanvasManager()

    xp, yp = 0, 0
    last_draw = time.time()
    hold_start = None
    prediction = ""
    locked = False

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        lmList = tracker.find_hands(img)
        fingers = tracker.fingers_up(lmList)

        if lmList and not locked:
            x, y = lmList[8][1], lmList[8][2]

            # DRAW
            if fingers == [0,1,0,0,0]:
                if xp == 0:
                    xp, yp = x, y
                cv2.line(canvas_manager.canvas,
                         (xp, yp), (x, y),
                         (255,255,255), 25)
                xp, yp = x, y
                last_draw = time.time()
            else:
                xp, yp = 0, 0

            # ERASE
            if fingers == [0,1,1,1,0]:
                cv2.circle(canvas_manager.canvas,
                           (x,y), 40,
                           (0,0,0), -1)

            # SAVE (5 fingers hold 3 sec)
            if fingers.count(1) == 5:
                if hold_start is None:
                    hold_start = time.time()
                elif time.time() - hold_start > 3:
                    prediction = predictor.predict(canvas_manager.canvas)
                    canvas_manager.clear_draw()
                    hold_start = None
            else:
                hold_start = None

        # AUTO PREDICT
        if time.time() - last_draw > 1:
            prediction = predictor.predict(canvas_manager.canvas)

        img[canvas_manager.canvas > 0] = \
            canvas_manager.canvas[canvas_manager.canvas > 0]

        cv2.putText(img, prediction,
                    (20,460),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255), 2)

        cv2.imshow("Air Canvas Pro", img)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('c'):
            canvas_manager.clear_draw()
        elif key == ord('l'):
            locked = not locked

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
