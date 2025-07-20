from PySide6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt, Signal
import sys
from src.view.main_window import MainWindow
from src.models.sequence_file import SequenceFile

class IntroWidow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("IntroWidow")
        self.setWindowTitle('GeneGenius')
        self.resize(200, 80)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        title = QLabel(
'''Welcome to GeneGenius!
Are you ready to take on the challenge of a bioinformatician?

Choose your grade level:''')
        title.setObjectName('IntroText')
        layout.addWidget(title)

        buttons = QHBoxLayout()

        third_grade_button = QPushButton('3rd')
        third_grade_button.clicked.connect(self.third_grade)
        ## Missing signal
        buttons.addWidget(third_grade_button)

        fifth_grade_button = QPushButton('5th')
        fifth_grade_button.clicked.connect(self.fifth_grade)
        ## Missing signal
        buttons.addWidget(fifth_grade_button)

        layout.addLayout(buttons)
        self.main_window = None

        layout.setContentsMargins(20,20,20,20)

    def third_grade(self):
        self.main_window = MainWindow()
        self.main_window.showMaximized()
        seqs = SequenceFile('src/data/seqs_3.txt')
        l_seqs = seqs.get_shuffled_list()
        self.main_window.start_string_feed(
            l_seqs,
            initial_delay_ms=3000,
            acceleration=0.99
        )

    def fifth_grade(self):
        self.main_window = MainWindow()
        self.main_window.showMaximized()
        seqs = SequenceFile('src/data/seqs_5.txt')
        l_seqs = seqs.get_shuffled_list()
        self.main_window.start_string_feed(
            l_seqs,
            initial_delay_ms=3000,
            acceleration=0.96
        )