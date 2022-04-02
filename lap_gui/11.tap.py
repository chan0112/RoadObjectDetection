from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QVBoxLayout
import sys

class RoadObjectDetectionAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('도로 객체 검출 AI')

        button1_tab = QPushButton('버튼1')
        button2_tab = QPushButton('버튼2')

        tabs = QTabWidget()
        tabs.addTab(button1_tab,'탭 1')
        tabs.addTab(button2_tab,'탭 2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    rod_ai = RoadObjectDetectionAI()
    rod_ai.show()
    sys.exit(app.exec_())
