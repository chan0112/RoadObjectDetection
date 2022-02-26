from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton

import sys

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')

        self.button1 = QPushButton('버튼1')
        self.button2 = QPushButton('버튼2')
        self.button3 = QPushButton('버튼3')
        self.button4 = QPushButton('버튼4')
        self.button5 = QPushButton('버튼5')
        self.button6 = QPushButton('버튼6')
        self.button7 = QPushButton('버튼7')
        self.button8 = QPushButton('버튼8')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button3)

        self.vbox_layout1 = QVBoxLayout()
        self.vbox_layout1.addWidget(self.button4)
        self.vbox_layout1.addWidget(self.button5)
        self.vbox_layout1.addWidget(self.button6)

        self.vbox_layout2 = QVBoxLayout()
        self.vbox_layout2.addWidget(self.button7)
        self.vbox_layout2.addWidget(self.button8)

        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.hbox_layout, 0, 0, 1, 2)
        self.main_layout.addLayout(self.vbox_layout1, 1, 0, 1, 1)
        self.main_layout.addLayout(self.vbox_layout2, 1, 1, 1, 1)
        self.setLayout(self.main_layout)


if __name__=='__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())