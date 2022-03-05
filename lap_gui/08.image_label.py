from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
import sys

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')

        self.image_lable = QLabel(self)
        pixmap = QPixmap('../data/images/3b59c8a5-f0b031cc.jpg')
        self.image_lable.setPixmap(pixmap)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.image_lable)

        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.vbox_layout, 0, 0, 1, 1)

        self.setLayout(self.main_layout)


if __name__=='__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())