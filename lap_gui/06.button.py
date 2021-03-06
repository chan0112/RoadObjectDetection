from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')

        self.button1 = QPushButton('버튼1')
        self.button2 = QPushButton('버튼2')
        self.button3 = QPushButton('버튼3')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)
        self.button3.clicked.connect(self.button3_click)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.button1, 0, 0, 1, 2)  # 앞에 두개 버튼 위치, 뒤에 두개 버튼 크기
        self.main_layout.addWidget(self.button2, 1, 0, 1, 1)
        self.main_layout.addWidget(self.button3, 1, 1, 1, 1)

        self.setLayout(self.main_layout)

    def button1_click(self):
        self.button1.setEnabled(False)
        self.button1.setText('버튼1 클릭')

    def button2_click(self):
        self.button2.setEnabled(False)
        self.button2.setText('버튼2 클릭')

    def button3_click(self):
        self.button3.setEnabled(False)
        self.button3.setText('버튼3 클릭')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())