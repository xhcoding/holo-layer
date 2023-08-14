from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColor

from utils import *


class HighlightColumn(QObject):

    def __init__(self) -> None:
        super().__init__()

        self.highlight_column_color = None
        self.cursor_info = None
        self.enable_highlight_column = False

    def update_info(self, cursor_info, emacs_frame_info):
        if not self.enable_highlight_column or cursor_info is None or len(cursor_info) != 4:
            return False
        [x, y, w, h] = cursor_info
        cursor_info = [int(x), int(y), int(w), int(h)]
        self.cursor_info = cursor_info
        return True

    def draw(self, painter, window_info, emacs_frame_info):
        if not self.enable_highlight_column or self.cursor_info is None or len(self.cursor_info) != 4:
            return
        if self.highlight_column_color is None:
            highlight_column_color = get_emacs_var("holo-layer-cursor-color")
            self.highlight_column_color = QColor(highlight_column_color)

        for info in window_info:
            if info[4] == 't':
                [x, y, w, h] = self.cursor_info
                width = int(w * 2 / 3)
                self.highlight_column_color.setAlpha(25)
                painter.fillRect(x + int(width / 2), info[1],  width , info[3], self.highlight_column_color)
