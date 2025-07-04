from PySide6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt, Signal
import sys

class IntroWidow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Broaden your Experience')
        self.resize(200, 80)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        title = QLabel('Select the appropriate grade level:')
        layout.addWidget(title)

        buttons = QHBoxLayout()

        third_grade_button = QPushButton('3rd')
        ## Missing signal
        buttons.addWidget(third_grade_button)

        sixth_grade_button = QPushButton('6th')
        ## Missing signal
        buttons.addWidget(sixth_grade_button)

        layout.addLayout(buttons)

        layout.setContentsMargins(20,20,20,20)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    intro = IntroWidow()
    intro.show()
    sys.exit(app.exec())