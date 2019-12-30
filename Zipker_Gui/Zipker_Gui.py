# -*- coding: utf-8 -*-

# 임포트 파트
from PyQt5 import QtCore, QtGui, QtWidgets
from Zipker import zip_decrypt, string

# 일부 변수 선언

filename = 0
opnum = 0
user_min = 0
user_max = 0
string2 = []

# Gui 구성 파트 (Qt 디자이너)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 폼 설정
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 370)
        MainWindow.setMinimumSize(420, 370)
        MainWindow.setMaximumSize(420, 370)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")  # 모든 폰트 맑은고딕 고정
        MainWindow.setFont(font)
        wicon = QtGui.QIcon('theme\\icon.png')  # 아이콘 설정
        MainWindow.setWindowIcon(wicon)

        # 위젯 배치
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 파일 설정 그룹
        self.filesetting = QtWidgets.QGroupBox(self.centralwidget)  # 그룹박스
        self.filesetting.setGeometry(QtCore.QRect(20, 20, 381, 81))
        self.filesetting.setObjectName("filesetting")
        self.filebutton = QtWidgets.QPushButton(self.filesetting)  # 파일찾기 버튼
        self.filebutton.setGeometry(QtCore.QRect(270, 35, 93, 28))
        self.filebutton.setObjectName("filebutton")
        self.filebutton.clicked.connect(self.filesurching)
        self.fileurl = QtWidgets.QLineEdit(self.filesetting)  # 파일링크 텍스트박스
        self.fileurl.setGeometry(QtCore.QRect(13, 35, 241, 28))
        self.fileurl.setObjectName("fileurl")
        self.fileurl.textChanged.connect(self.filesurching2)

        # 문자열 설정 그룹
        self.stringsetting = QtWidgets.QGroupBox(self.centralwidget)  # 그룹박스
        self.stringsetting.setGeometry(QtCore.QRect(20, 120, 381, 171))
        self.stringsetting.setObjectName("stringsetting")
        self.alphabet = QtWidgets.QCheckBox(self.stringsetting)  # 알파벳사용
        self.alphabet.setGeometry(QtCore.QRect(20, 40, 100, 31))
        self.alphabet.setIconSize(QtCore.QSize(20, 20))
        self.alphabet.setObjectName("alphabet")
        self.alphabet.stateChanged.connect(self.ustring)
        self.special = QtWidgets.QCheckBox(self.stringsetting)  # 특문사용
        self.special.setGeometry(QtCore.QRect(20, 120, 100, 31))
        self.special.setIconSize(QtCore.QSize(20, 20))
        self.special.setObjectName("special")
        self.special.stateChanged.connect(self.ustring)
        self.number = QtWidgets.QCheckBox(self.stringsetting)  # 숫자사용
        self.number.setGeometry(QtCore.QRect(20, 80, 100, 31))
        self.number.setIconSize(QtCore.QSize(20, 20))
        self.number.setObjectName("number")
        self.number.stateChanged.connect(self.ustring)
        self.label = QtWidgets.QLabel(self.stringsetting)  # 최소 글자수 라벨
        self.label.setGeometry(QtCore.QRect(143, 50, 81, 20))
        self.label.setObjectName("label")
        self.min = QtWidgets.QLineEdit(self.stringsetting)  # 최소 글자수 텍박
        self.min.setGeometry(QtCore.QRect(240, 50, 113, 21))
        self.min.setObjectName("min")
        self.min.textChanged.connect(self.min_set)
        self.label_2 = QtWidgets.QLabel(self.stringsetting)  # 최대 글자수 라벨
        self.label_2.setGeometry(QtCore.QRect(143, 90, 81, 20))
        self.label_2.setObjectName("label_2")
        self.max = QtWidgets.QLineEdit(self.stringsetting)  # 최대 글자수 텍박
        self.max.setGeometry(QtCore.QRect(240, 90, 113, 21))
        self.max.setObjectName("max")
        self.max.textChanged.connect(self.max_set)

        # 그 외
        self.start = QtWidgets.QPushButton(self.centralwidget)  # 검색 시작
        self.start.setGeometry(QtCore.QRect(292, 300, 111, 41))
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.start.clicked.connect(self.findpassword)

        # self.menubar = QtWidgets.QMenuBar(MainWindow)  # 메뉴바
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 26))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)  # 상태바
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('대기 중')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 타이틀, 텍스트 등 설정

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zipker"))
        self.filesetting.setTitle(_translate("MainWindow", "파일 설정"))
        self.filebutton.setText(_translate("MainWindow", "파일 찾기"))
        self.stringsetting.setTitle(_translate("MainWindow", "대입 문자열 설정"))
        self.alphabet.setText(_translate("MainWindow", "알파벳"))
        self.special.setText(_translate("MainWindow", "특수문자"))
        self.number.setText(_translate("MainWindow", "숫자"))
        self.label.setText(_translate("MainWindow", "최소 자릿수"))
        self.label_2.setText(_translate("MainWindow", "최대 자릿수"))
        self.start.setText(_translate("MainWindow", "대입 시작"))

    # 파일 찾기 (버튼을 눌렀을 때 이벤트)

    def filesurching(self):
        global filename

        f_filename = QtWidgets.QFileDialog.getOpenFileName(
            None, None, None, "zip(*.zip)")
        filename = f_filename[0]

        if filename == "":
            self.statusbar.showMessage('파일을 선택하여 주십시오.')
        elif filename[-3:] != "zip":
            QtWidgets.QMessageBox.warning(
                MainWindow, "Zipker", "선택하신 파일은 ZIP 형식의 파일이 아닙니다.\nZIP 파일만 지원 가능합니다.\n\nError code: F-TYPE", QtWidgets.QMessageBox.Yes)
        else:
            self.fileurl.setText(filename)
            self.statusbar.showMessage('파일 선택 완료')

    # 파일 찾기 (텍박을 수정했을 때 이벤트)

    def filesurching2(self):
        global filename

        filename = self.fileurl.text()

        if filename == "":
            self.statusbar.showMessage('파일을 선택하여 주십시오.')
        elif filename[-3:] == "zip":
            self.statusbar.showMessage('파일 선택 완료')
        else:
            QtWidgets.QMessageBox.warning(
                MainWindow, "Zipker", "입력하신 파일은 ZIP 형식의 파일이 아닙니다.\nZIP 파일만 지원 가능합니다.\n\nError code: F-TYPE", QtWidgets.QMessageBox.Yes)
            self.fileurl.setText("")

    # 문자열 설정 (체크박스)

    def ustring(self):
        global opnum
        global string2

        alpha_yn = self.alphabet.isChecked()
        num_yn = self.number.isChecked()
        spe_yn = self.special.isChecked()

        if alpha_yn == True and num_yn == True and spe_yn == True:
            opnum = 7
        elif alpha_yn == True and num_yn == True and spe_yn == False:
            opnum = 4
        elif alpha_yn == True and num_yn == False and spe_yn == True:
            opnum = 6
        elif alpha_yn == True and num_yn == False and spe_yn == False:
            opnum = 2
        elif alpha_yn == False and num_yn == True and spe_yn == True:
            opnum = 5
        elif alpha_yn == False and num_yn == True and spe_yn == False:
            opnum = 1
        elif alpha_yn == False and num_yn == False and spe_yn == True:
            opnum = 3
        else:
            opnum = 0

        if opnum == 0:
            self.statusbar.showMessage('옵션을 선택하여 주십시오.')
        else:
            self.statusbar.showMessage(str(opnum) + '번 옵션 선택 완료')
            string2 = string(opnum)

    # 최소 자릿수 설정

    def min_set(self):
        global user_min

        f_user_min = self.min.text()

        if f_user_min == "":
            self.statusbar.showMessage('최소 자릿수를 설정하여 주십시오.')
        else:
            try:
                user_min = int(f_user_min)
                self.statusbar.showMessage('최소 자릿수 설정 완료')
                return user_min

            except:
                QtWidgets.QMessageBox.warning(
                    MainWindow, "Zipker", "입력하신 것이 숫자가 아닌 것 같습니다.\n숫자 형식으로 입력하시기 바랍니다.\n\nError code: U-TYPE", QtWidgets.QMessageBox.Yes)
                self.min.setText("")

    # 최대 자릿수 설정

    def max_set(self):
        global user_max

        f_user_max = self.max.text()

        if f_user_max == "":
            self.statusbar.showMessage('최대 자릿수를 설정하여 주십시오.')
        else:
            try:
                user_max = int(f_user_max)
                self.statusbar.showMessage('최대 자릿수 설정 완료')
                return user_max

            except:
                QtWidgets.QMessageBox.warning(
                    MainWindow, "Zipker", "입력하신 것이 숫자가 아닌 것 같습니다.\n숫자 형식으로 입력하시기 바랍니다.\n\nError code: U-TYPE", QtWidgets.QMessageBox.Yes)
                self.max.setText("")

    # 파일 검색 시작

    def findpassword(self):
        global filename, user_max, user_min, string2

        if filename == "" or filename == 0:
            QtWidgets.QMessageBox.warning(
                MainWindow, "Zipker", "파일이 선택되지 않았습니다.\n선택하여 주시기 바랍니다.\n\nError code: U-NOINPUT", QtWidgets.QMessageBox.Yes)
        elif opnum == "" or opnum == 0:
            QtWidgets.QMessageBox.warning(
                MainWindow, "Zipker", "옵션이 선택되지 않았습니다.\n선택하여 주시기 바랍니다.\n\nError code: U-NOINPUT", QtWidgets.QMessageBox.Yes)
        elif user_min == "" or user_max == "" or user_min == 0 or user_max == 0:
            QtWidgets.QMessageBox.warning(
                MainWindow, "Zipker", "자릿수 설정이 완료되지 않았습니다.\n설정하여 주시기 바랍니다.\n\nError code: U-NOINPUT", QtWidgets.QMessageBox.Yes)
        else:
            end_password = zip_decrypt(filename, string2, user_min, user_max)

            if end_password == False:
                QtWidgets.QMessageBox.information(
                    MainWindow, "Zipker", "대입 결과 비밀번호를 찾아내지 못했습니다\n문자열 설정이 잘못되었거나 미지원 파일일 수 있습니다.\n\nError code: Z-UNKNOWN", QtWidgets.QMessageBox.Yes)
            else:
                QtWidgets.QMessageBox.information(
                    MainWindow, "Zipker", "대입 결과 비밀번호를 찾아내었습니다.\n본 프로그램은 압축 파일을 지원하지 않으므로 타사 프로그램으로 해제하십시오.\n\nPassword: " + end_password, QtWidgets.QMessageBox.Yes)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
