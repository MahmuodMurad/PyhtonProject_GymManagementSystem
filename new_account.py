from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_widget(object):

    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(776, 717)
        widget.setFixedWidth(776)
        widget.setFixedHeight(717)
        widget.setWindowIcon(QtGui.QIcon("gym-icon_30328.ico"))
        widget.setStyleSheet("background-color: rgb(248, 147, 31);")
        #f1 = widget.menuBar().addMenu("Options")
        #e = QtWidgets.QAction(" New Player ", widget)
        #e1 = QtWidgets.QAction(" Info Player", widget)
        #e2 = QtWidgets.QAction(" Captains   ", widget)
        #e3 = QtWidgets.QAction(" Prices     ", widget)

        #def ff():
            #print("new")

        #e.triggered.connect(ff)
        #e1.triggered.connect(ff)
        #e2.triggered.connect(ff)
        #e3.triggered.connect(ff)
        #f1.addAction(e)
        #f1.addAction(e1)
        #f1.addAction(e2)
        #f1.addAction(e3)
        self.lineEdit_3 = QtWidgets.QLineEdit(widget)# field of first name
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 170, 251, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(widget)#ده زرار ال CREATE
        self.pushButton_3.setGeometry(QtCore.QRect(380, 540, 131, 31))
        self.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.get_text)
        self.label_9 = QtWidgets.QLabel(widget)
        self.label_9.setGeometry(QtCore.QRect(220, 40, 371, 61))
        self.label_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                   "font: 26pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_19 = QtWidgets.QLabel(widget)
        self.label_19.setGeometry(QtCore.QRect(290, 490, 450, 50))
        self.label_19.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                   "font: 12pt \"MS Shell Dlg 2\";"
                                    "color:black;")
        self.label_19.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(widget)#field of last name
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 220, 251, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(widget)# field of email
        self.lineEdit_5.setGeometry(QtCore.QRect(320, 270, 251, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(widget)# field of confirm password ولازم يكون مطابق ل الpassword
        self.lineEdit_6.setGeometry(QtCore.QRect(320, 470, 251, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                      "border-radius: 8px;")
        self.lineEdit_6.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(widget)#field of ID لازم يكون PRAIMRY KEY OUTO INCREMNT
        self.lineEdit_7.setGeometry(QtCore.QRect(320, 370, 251, 31))
        self.lineEdit_7.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit_7.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(widget)#field of passowrd
        self.lineEdit_8.setGeometry(QtCore.QRect(320, 420, 251, 31))
        self.lineEdit_8.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit_8.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(widget)#field of phone والزم يكون حداشر رقم
        self.lineEdit_9.setGeometry(QtCore.QRect(320, 320, 251, 31))
        self.lineEdit_9.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit_9.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(widget)
        self.label_10.setGeometry(QtCore.QRect(170, 170, 91, 31))
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(widget)
        self.label_11.setGeometry(QtCore.QRect(170, 220, 81, 31))
        self.label_11.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(widget)
        self.label_12.setGeometry(QtCore.QRect(170, 268, 76, 31))
        self.label_12.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(widget)
        self.label_13.setGeometry(QtCore.QRect(170, 370, 21, 31))
        self.label_13.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(widget)
        self.label_14.setGeometry(QtCore.QRect(170, 325, 121, 31))
        self.label_14.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(widget)
        self.label_15.setGeometry(QtCore.QRect(170, 420, 81, 31))
        self.label_15.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(widget)
        self.label_16.setGeometry(QtCore.QRect(170, 470, 141, 31))
        self.label_16.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(widget)
        self.label_17.setGeometry(QtCore.QRect(580, 430, 81, 16))
        self.label_17.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
                                    "")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(widget)
        self.label_18.setGeometry(QtCore.QRect(520, 550, 71, 16))
        self.label_18.setStyleSheet("color: rgb(238, 233, 233);\n"
                                    "font: 8pt \"MS Shell Dlg 2\";\n"
                                    "text-decoration: underline;")
        self.label_18.setObjectName("label_18")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def get_text(self):  # الفانكشن ديه بترن لما تدوس علي الزرار
        # كل واحد هنا بياخد قيمته من البارات بعد ماليوزر كتب وداس الزرار
        db = sqlite3.connect("app_db.db")
        print("the connect is successfully")

        cur = db.cursor()
        #cur.execute("delete from create_account ")
        #print("deleted")
        self.firstname = self.lineEdit_3.text()
        self.lastname = self.lineEdit_4.text()
        self.username = self.lineEdit_5.text()
        self.confirm_password = self.lineEdit_6.text()
        self.id = self.lineEdit_7.text()
        self.password = self.lineEdit_8.text()
        self.phoneNumber = self.lineEdit_9.text()
        SpecialSym = ['$', '@', '&', '#', '%']
        if len(self.password) <= 3 and len(self.password) >= 12:
            self.label_19.setText(" \U0001F600 password in range 3:12")
        elif not any(char in SpecialSym for char in self.password):
                self.label_19.setText(" \U0001F600 Password should have at least one of the symbols %$@#")
        elif (self.password != self.confirm_password):
            self.label_19.setText(" \U0001F600 please check the password")
        elif len(self.phoneNumber) != 11:
            self.label_19.setText(" \U0001F600 Phone Number must equal to 11 number")
        elif len(self.id) != 14:
            self.label_19.setText(" \U0001F600 ID must equal to 14 number")
        else:
            self.label_19.setText("Enter other person information")
            import welcome
            self.window2 = QtWidgets.QMainWindow()
            self.ui = welcome.Ui_Form()
            self.ui.setupUi(self.window2)
            self.window2.show()

            cur.execute(
                "CREATE TABLE if not exists create_account( firstname text not null , lastname text not null , username text not null , confirm_password text not null,id integer PRIMARY KEY  not null , phoneNumber text not null ,password text not null )")
            print("THe table create")
            cur.execute("insert into create_account VALUES(?,?,?,?,?,?,?)", (
            self.firstname, self.lastname, self.username, self.confirm_password, self.id, self.phoneNumber, self.password))
            print("the data insert")

            print("ok")

            db.commit()
            db.close()

        # انت بعد كدا بقا تاخد المتغيرات دول وتحطهم عندك في الداتا بيز
    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Creating New Account"))
        self.pushButton_3.setText(_translate("widget", "Create"))
        self.label_9.setText(_translate("widget", "Creating New Account"))
        self.label_10.setText(_translate("widget", "<html><head/><body><p>First name:</p><p><br/></p></body></html>"))
        self.label_11.setText(_translate("widget", "<html><head/><body><p>Last name:</p><p><br/></p></body></html>"))
        self.label_12.setText(_translate("widget", "<html><head/><body><p>Username:</p></body></html>"))
        self.label_13.setText(_translate("widget", "<html><head/><body><p>ID:</p></body></html>"))
        self.label_14.setText(_translate("widget", "<html><head/><body><p>Phone Number:</p><p><br/></p></body></html>"))
        self.label_15.setText(_translate("widget", "<html><head/><body><p>Password:</p></body></html>"))
        self.label_16.setText(_translate("widget", "<html><head/><body><p>Confirm Password:</p></body></html>"))
        self.label_17.setText(_translate("widget", "(min 3,max :12)"))
        self.label_18.setText(_translate("widget", "for admin only"))
        self.label_19.setText(_translate("widget", " "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
