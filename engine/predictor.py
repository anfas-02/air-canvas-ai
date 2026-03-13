import tensorflow as tf
import numpy as np
import cv2
import os

class Predictor:
    def __init__(self):
        self.model = tf.keras.models.load_model("models/letter_model.h5")
        self.class_names = sorted([
            d for d in os.listdir("dataset")
            if os.path.isdir(os.path.join("dataset", d))
        ])

    def preprocess(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        if not contours:
            return None

        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) < 800:
            return None

        x,y,w,h = cv2.boundingRect(c)
        letter = thresh[y:y+h, x:x+w]

        size = max(w, h) + 20
        square = np.zeros((size, size), dtype=np.uint8)

        xoff = (size - w)//2
        yoff = (size - h)//2
        square[yoff:yoff+h, xoff:xoff+w] = letter

        letter = cv2.resize(square, (28,28)) / 255.0
        return letter.reshape(1,28,28,1)

    def predict(self, canvas):
        processed = self.preprocess(canvas)
        if processed is None:
            return "No Prediction"

        probs = self.model.predict(processed, verbose=0)[0]
        idx = np.argmax(probs)
        conf = probs[idx]

        if conf < 0.75:
            return "Uncertain"

        return f"{self.class_names[idx]} ({conf:.2f})"
