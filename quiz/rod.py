from PyQt5.QtCore import Qt, QUrl, QFileInfo, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSlider, QStyle, QGridLayout, QTabWidget, QGroupBox, QLabel
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys


class RoadObjectDetectionAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("도로 객체 검출 AI")

        tabs = QTabWidget()

        self.group_box1 = QGroupBox('메뉴')
        self.group_box2 = QGroupBox('원본 이미지')
        self.group_box3 = QGroupBox('사물 검출 결과')
        self.group_box4 = QGroupBox('메뉴')
        self.group_box5 = QGroupBox('영상')

        self.button1 = QPushButton('이미지 선택')
        self.button2 = QPushButton('영상 선택')

        self.hbox_layout1 = QHBoxLayout()
        self.hbox_layout1.addWidget(self.button1)
        self.group_box1.setLayout(self.hbox_layout1)

        self.hbox_layout2 = QHBoxLayout()
        self.group_box2.setLayout(self.hbox_layout2)

        self.hbox_layout3 = QHBoxLayout()
        self.group_box3.setLayout(self.hbox_layout3)

        self.hbox_layout4 = QHBoxLayout()
        self.hbox_layout4.addWidget(self.button2)
        self.group_box4.setLayout(self.hbox_layout4)

        self.hbox_layout5 = QHBoxLayout()
        self.group_box5.setLayout(self.hbox_layout5)

        self.main_layout1 = QGridLayout()
        self.main_layout1.addWidget(self.group_box1, 0, 0, 1, 4)
        self.main_layout1.addWidget(self.group_box2, 1, 0, 5, 3)
        self.main_layout1.addWidget(self.group_box3, 1, 3, 5, 1)
        self.setLayout(self.main_layout1)

        self.main_layout2 = QGridLayout()
        self.main_layout2.addWidget(self.group_box4, 0, 0, 1, 4)
        self.main_layout2.addWidget(self.group_box5, 1, 5, 5, 5)
        self.setLayout(self.main_layout2)

        tabs.addTab(self.main_layout1,'이미지')
        tabs.addTab(self.main_layoyt2,'동영상')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    rod_ai = RoadObjectDetectionAI()
    rod_ai.show()
    sys.exit(app.exec_())