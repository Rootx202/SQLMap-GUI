#!/usr/bin/env python3
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont, QScreen

from main_window import SqlmapGUI


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("SQLMap Pro GUI")
    app.setApplicationVersion("2.0")

    font = QFont("Segoe UI", 10)
    app.setFont(font)

    window = SqlmapGUI()

    screen = app.primaryScreen()
    if screen:
        geo = screen.availableGeometry()
        window.resize(int(geo.width() * 0.8), int(geo.height() * 0.85))

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
