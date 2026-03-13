import streamlit as st
import cv2
import numpy as np
import time
from core.hand_tracker import HandTracker
from core.predictor import Predictor

st.set_page_config(layout="wide")

st.title("✋ Air Canvas Pro (Dark Mode)")

# -------- Sidebar --------
lock = st.sidebar.toggle("🔒 Hand Tracking Lock")

start = st.checkbox("Start Camera")

FRAME_WINDOW = st.empty()

if "canvas" not in st.session_state:
    st.session_state.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
    st.session_state.prediction = ""
    st.session_state.last_draw = time.time()
    st.session_state.hold_start = None

if start:

    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    predictor = Predictor()

    xp, yp = 0, 0

    while start:
        ret, img = cap.read()
        if not ret:
            st.error("Camera not detected")
            break

        img = cv2.flip(img, 1)

        lmList = tracker.find_hands(img)
        fingers = tracker.fingers_up(lmList)

        if not lock and lmList:

            x, y = lmList[8][1], lmList[8][2]

            # DRAW (1 finger)
            if fingers == [0,1,0,0,0]:
                if xp == 0:
                    xp, yp = x, y
                cv2.line(st.session_state.canvas,
                         (xp, yp), (x, y),
                         (255,255,255), 25)
                xp, yp = x, y
                st.session_state.last_draw = time.time()
            else:
                xp, yp = 0, 0

            # ERASE (3 fingers)
            if fingers == [0,1,1,1,0]:
                cv2.circle(st.session_state.canvas,
                           (x,y), 40,
                           (0,0,0), -1)

            # SAVE (5 fingers hold 3 sec)
            if fingers.count(1) == 5:
                if st.session_state.hold_start is None:
                    st.session_state.hold_start = time.time()
                elif time.time() - st.session_state.hold_start > 3:
                    st.session_state.prediction = predictor.predict(
                        st.session_state.canvas
                    )
                    st.session_state.canvas[:] = 0
                    st.session_state.hold_start = None
            else:
                st.session_state.hold_start = None

        # AUTO PREDICT AFTER PAUSE
        if time.time() - st.session_state.last_draw > 1:
            st.session_state.prediction = predictor.predict(
                st.session_state.canvas
            )

        img[st.session_state.canvas > 0] = \
            st.session_state.canvas[st.session_state.canvas > 0]

        cv2.putText(img,
                    st.session_state.prediction,
                    (20,460),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    2)

        FRAME_WINDOW.image(img, channels="BGR")

    cap.release()
