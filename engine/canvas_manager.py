import numpy as np

class CanvasManager:
    def __init__(self):
        self.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
        self.word_canvas = np.zeros((480, 640, 3), dtype=np.uint8)
        self.cursor_x = 20
        self.cursor_y = 50
        self.line_height = 50

    def clear_draw(self):
        self.canvas[:] = 0

    def clear_word(self):
        self.word_canvas[:] = 0
        self.cursor_x = 20
        self.cursor_y = 50
