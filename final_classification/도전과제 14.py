from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QGroupBox, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import model

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')
        self.a = ''
        self.group_box1 = QGroupBox('메뉴')
        self.group_box2 = QGroupBox('이미지')
        self.group_box3 = QGroupBox('분류 예측')

        self.model = model.Model()

        self.text_lable = QLabel(self)
        self.text_lable.setText(str(self.a))

        self.image_lable = QLabel(self)
        pixmap = QPixmap('')
        self.image_lable.setPixmap(pixmap)

        self.button1 = QPushButton('데이터 불러오기')
        self.button2 = QPushButton('모델 학습')
        self.button3 = QPushButton('모델 저장')
        self.button4 = QPushButton('모델 불러오기')
        self.button5 = QPushButton('이미지 분류')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)
        self.button3.clicked.connect(self.button3_click)
        self.button4.clicked.connect(self.button4_click)
        self.button5.clicked.connect(self.button5_click)


        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button3)
        self.hbox_layout.addWidget(self.button4)
        self.hbox_layout.addWidget(self.button5)
        self.group_box1.setLayout(self.hbox_layout)

        self.hbox_layout1 = QHBoxLayout()
        self.hbox_layout1.addWidget(self.image_lable)
        self.group_box3.setLayout(self.hbox_layout1)

        self.hbox_layout2 = QHBoxLayout()
        self.hbox_layout2.addWidget(self.text_lable)
        self.group_box2.setLayout(self.hbox_layout2)


        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 4)
        self.main_layout.addWidget(self.group_box2, 1, 0, 5, 3)
        self.main_layout.addWidget(self.group_box3, 1, 3, 5, 1)
        self.setLayout(self.main_layout)

    def button1_click(self):
        self.button1.setEnabled(False)
        self.model.load_data()
        self.button1.setText('데이터 불러오기 완료')


    def button2_click(self):
        self.button4.setEnabled(False)
        self.model.train()


    def button3_click(self):
        self.button4.setEnabled(False)
        self.model.save()


    def button4_click(self):
        self.button4.setEnabled(False)
        self.model.load()
        self.button4.setText('모델 불러오기 완료')


    def button5_click(self):
        self.button5.setEnabled(False)
        path, _ = QFileDialog.getOpenFileName(self, '', '../data.images', 'IMAGE Files(*.jpg *.png)')
        if path == '':
           print('취소')
        else:
            self.text_lable.setText(self.model.predict(path))
            self.button5.setText('이미지 분류 완료')




if __name__=='__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())