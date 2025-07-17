import sys
from typing import List
from PySide6.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFrame, QSizePolicy, QScrollArea
)
from PySide6.QtCore import Qt, QMimeData, QTimer
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QDrag, QMouseEvent, QPixmap
from src.view.main_window import MainWindow
from src.view.intro_window import IntroWidow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load external style sheet
    with open("src/view/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    # Example usage
    window.start_string_feed(
        ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta"],
        initial_delay_ms=1000,
        acceleration=0.9
    )

    sys.exit(app.exec())
