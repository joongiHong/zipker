# coding=utf-8

# 임포트 부분
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# Gui (Pyqt) 구성 부분

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Zipker Gui (Beta 2)')  # 타이틀 설정

        self.move(300, 300)  # 위치 설정
        self.resize(400, 200)  # 사이즈 설정
        self.setMinimumSize(400, 200)  # 사이즈 조절 금지
        self.setMaximumSize(400, 200)

        windowIcon = QIcon('theme\\icon.png')
        self.setWindowIcon(windowIcon)  # 아이콘 설정

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
