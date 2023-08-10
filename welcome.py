from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Ui_Form(object):
    def forget_password(self):
        msg = QMessageBox()
        msg.setWindowTitle("Forget Password")
        msg.setText("\U0001F44A \U0001F44A بتنساه ليه يا شاطر")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def open_name_of_player(self):  # function بتفتح صفحه الname
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()

        if len(self.username) == 0:
            self.label_9.setText("Please input username")
        elif len(self.password) == 0:
            self.label_9.setText("Please input password")
        elif len(self.password) < 3:
            self.label_9.setText("Password must be greater than 3")
        elif len(self.password) > 12:
            self.label_9.setText("Password must be less than 12")
        elif len(self.username) == 0 and len(self.password) == 0:
            self.label_9.setText("Please input all fields")
        else:
            conn = sqlite3.connect("app_db.db")
            curs = conn.cursor()
            query = 'SELECT *  FROM create_account WHERE username =? AND  password = ?'
            curs.execute(query, (self.username, self.password))
            result_pass = curs.fetchone()
            if not result_pass:
                self.label_9.setText("Invalid UserName or Password")
            else:
                from name_of_player import Ui_Form1
                self.window3 = QtWidgets.QMainWindow()
                self.ui = Ui_Form1()
                self.ui.setupUi(self.window3)
                self.window3.show()
                self.label_9.setText("")

    def open_new_account(self):#functon بتفتح صفحه ال new account
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if self.username == "admin" and self.password == "12345678910":
            from new_account import Ui_widget
            self.window4 = QtWidgets.QMainWindow()
            self.ui = Ui_widget()
            self.ui.setupUi(self.window4)
            self.window4.show()
        else:
            self.label_9.setText("Admin ONLY can creat new user")
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(776, 717)
        Form.setMaximumSize(776, 717)
        Form.setWindowIcon(QtGui.QIcon("gym-icon_30328.ico"))
        Form.setToolTip("")
        Form.setStyleSheet("background-color: rgb(248, 147, 31);\n""")
        Form.setWindowFilePath("")

        self.lineEdit = QtWidgets.QLineEdit(Form)#username field اللي هيدخل فيه ال داتا بتاعته
        self.lineEdit.setGeometry(QtCore.QRect(260, 240, 251, 31))
        self.lineEdit.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit.setPlaceholderText("Enter username")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 240, 101, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 280, 101, 31))
        self.label_3.setObjectName("label_3")
        #self.label_2 = QtWidgets.QLabel(Form)
        #self.label_2.setGeometry(QtCore.QRect(270, 330, 141, 16))
        #self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.clicked.connect(self.open_name_of_player)#login button
        #self.pushButton.clicked.connect(Form.close)
        self.pushButton.setGeometry(QtCore.QRect(320, 430, 131, 31))
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(238, 233, 230);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "border-radius: 8px;\n"
                                      "\n}"
                                      "QPushButton:hover{background-color: rgb(238, 233, 230);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "border-radius: 8px;\n"
                                      "\n}"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.clicked.connect(self.open_new_account)#new account button الادمن بس هو اللي مسموح ليه انه يدخل
        #self.pushButton_2.clicked.connect(Form.close)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 500, 131, 31))
        self.pushButton_2.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(238, 233, 230);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "border-radius: 8px;\n"
                                      "\n}"
                                      "QPushButton:hover{background-color: rgb(238, 233, 230);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "border-radius: 8px;\n"
                                      "\n}"
                                      "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.clicked.connect(self.forget_password)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 330, 141, 20))
        self.pushButton_3.setStyleSheet("border-radius: 8px;\n"
                                      "background-color: rgb(248, 147, 31);\n"
                                      "  font-size: 16px;\n"
                                      "box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(370, 470, 31, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 50, 381, 61))
        self.label_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                   "font: 26pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")


        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(480, 510, 71, 16))
        self.label_7.setStyleSheet("color: rgb(238, 233, 233);\n"
                                   "font: 8pt \"MS Shell Dlg 2\";\n"
                                   "text-decoration: underline;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(520, 300, 81, 16))
        self.label_8.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(280, 400, 240, 31))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                   "color:red;")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)#password field اللي هيدخل فيه ال داتا بتاعته
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 290, 251, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit_2.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText("Enter password")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Welcome"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:12pt;\">Username</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">Password</span></p></body></html>"))
        #self.label_2.setText(_translate("Form",
                                        #"<html><head/><body><p><span style=\" text-decoration: underline;\">Forget Password</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Log in"))
        self.pushButton_2.setText(_translate("Form", "New Account"))
        self.pushButton_3.setText(_translate("Form", "Forget Password"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>OR</p></body></html>"))
        self.label_5.setText(_translate("Form", "Welcome To Gorilla Gym"))
        self.label_7.setText(_translate("Form", "for admin only"))
        self.label_8.setText(_translate("Form", "(min 3,max :12)"))
        self.label_9.setText(_translate("Form", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())
