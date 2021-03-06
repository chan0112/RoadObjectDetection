from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QLabel

import sys

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')

        self.group_box1 = QGroupBox('그룹1')
        self.group_box2 = QGroupBox('그룹2')
        self.a = 0

        self.text_lable = QLabel(self)
        self.text_lable.setText(str(self.a))

        self.button1 = QPushButton('-')
        self.button2 = QPushButton('+')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.group_box1.setLayout(self.hbox_layout)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.text_lable)
        self.group_box2.setLayout(self.vbox_layout)


        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 2)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 1)
        self.setLayout(self.main_layout)

    def button1_click(self):
        self.a -= 1
        self.text_lable.setText(str(self.a))

    def button2_click(self):
        self.a += 1
        self.text_lable.setText(str(self.a))

if __name__=='__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())