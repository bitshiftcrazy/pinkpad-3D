#!/usr/bin/env python3

import sys
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QGuiApplication, QPainter, QPixmap, QCursor
from PyQt6.QtWidgets import QApplication, QWidget

PAW_IMAGE = "/home/kati/.icons/PinkPaw/cursors/src/paw_mouse32.png"

MAX_PAWS = 12
FADE_MS = 900
SPAWN_DISTANCE = 40
TICK_MS = 16


class PawTrail(QWidget):
    def __init__(self):
        super().__init__()

        self.paw = QPixmap(PAW_IMAGE)
        self.paws = []
        self.last_pos = None

        screen = QGuiApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
            | Qt.WindowType.X11BypassWindowManagerHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(TICK_MS)

        self.show()

    def tick(self):
        pos = QCursor.pos()

        if self.last_pos is None:
            self.last_pos = pos

        dx = pos.x() - self.last_pos.x()
        dy = pos.y() - self.last_pos.y()

        if dx * dx + dy * dy >= SPAWN_DISTANCE * SPAWN_DISTANCE:
            self.paws.append([QPoint(pos), FADE_MS])
            self.last_pos = pos

            if len(self.paws) > MAX_PAWS:
                self.paws.pop(0)

        for paw in self.paws:
            paw[1] -= TICK_MS

        self.paws = [paw for paw in self.paws if paw[1] > 0]
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for pos, life in self.paws:
            alpha = max(0, min(255, int(255 * life / FADE_MS)))
            painter.setOpacity(alpha / 255)

            x = pos.x() - self.paw.width() // 2
            y = pos.y() - self.paw.height() // 2

            painter.drawPixmap(x, y, self.paw)


app = QApplication(sys.argv)
trail = PawTrail()
sys.exit(app.exec())
