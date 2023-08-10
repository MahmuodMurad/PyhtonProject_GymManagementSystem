from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_welcome(object):
    def open_Welcome(self):# function بتفتح الصفحه اللي بعدها
        from welcome import Ui_Form
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.resize(776, 717)
        welcome.setFixedWidth(776)
        welcome.setFixedHeight(717)
        welcome.setWindowIcon(QtGui.QIcon("gym-icon_30328.ico"))
        welcome.setStyleSheet("background-color: rgb(255, 119, 0);\n"
                              "background-color: rgb(255, 170, 0);\n"
                              "background-color: rgb(248, 147, 31);")
        self.label = QtWidgets.QLabel(welcome)
        self.label.setGeometry(QtCore.QRect(140, 70, 481, 411))
        self.label.setStyleSheet("background-image: url(p1.jpeg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("p1.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(welcome)
        self.pushButton.clicked.connect(self.open_Welcome)# الbutton اللي هيفتح الصفحه
        self.pushButton.clicked.connect(welcome.close)#علشان يقفل الصفحه اول ما التانيه تفتح
        self.pushButton.setGeometry(QtCore.QRect(650, 520, 101, 41))
        self.pushButton.setStyleSheet("border-radius: 8px;\n"
                                      "background-color: rgb(248, 147, 31);\n"
                                      "  font-size: 16px;\n"
                                      "box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "Logo"))
        self.pushButton.setText(_translate("welcome", "continue>>>"))





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    welcome = QtWidgets.QWidget()
    ui = Ui_welcome()
    ui.setupUi(welcome)
    welcome.show()
    sys.exit(app.exec_())
