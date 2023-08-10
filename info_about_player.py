import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Form2(object):
    def open_Prices(self):
        from prices import Ui_Form5
        self.window8 = QtWidgets.QMainWindow()
        self.ui = Ui_Form5()
        self.ui.setupUi(self.window8)
        self.window8.show()
    def open_Captains(self):
        from captains import Ui_Form4
        self.window7 = QtWidgets.QMainWindow()
        self.ui = Ui_Form4()
        self.ui.setupUi(self.window7)
        self.window7.show()
    def open_New_Player(self):
        from inter_the_info import Ui_Form3
        self.window6 = QtWidgets.QMainWindow()
        self.ui = Ui_Form3()
        self.ui.setupUi(self.window6)
        self.window6.show()
    def delete_player(self):
        db = sqlite3.connect("app_db.db")
        cur = db.cursor()
        cur.execute("SELECT * FROM cache WHERE cache_name='inf'")
        get_data = cur.fetchone()
        clmn2 = get_data[1]
        db = sqlite3.connect("app_db.db")
        c = db.cursor()
        c.execute("DELETE FROM players_datas WHERE name=?", (clmn2,))
        print("deleted")
        db.commit()
    def times_players(self):
        self.times =self.lineEdit.text()
        self.times_lift= self.lineEdit_3.text()
        conn = sqlite3.connect("app_db.db")
        c = conn.cursor()
        c.execute("SELECT * FROM cache WHERE cache_name='inf'")
        get_data = c.fetchone()
        clmn2 = get_data[1]
        c.execute(
            f"update players_datas set times = '{self.times}' , times_lift = '{self.times_lift}'  where name='{clmn2}'")
        print("the table update")
        conn.commit()
        conn.close()

    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(776, 717)
        Form2.setMaximumSize(776, 717)
        Form2.setWindowIcon(QtGui.QIcon("gym-icon_30328.ico"))
        Form2.setStyleSheet("background-color: rgb(248, 147, 31);")
        f1 = Form2.menuBar().addMenu("Options")
        f1.setStyleSheet("background-color:  rgb(248, 132, 31);")
        e = QtWidgets.QAction(QIcon('football_player_sport_olympic_player_icon_123803.ico')," New Player ", Form2)
        #e1 = QtWidgets.QAction(" Info Player", Form2)
        e2 = QtWidgets.QAction(QIcon('medal_champion_award_winner_olympic_icon_207819.ico'), " Captains   ", Form2)
        e3 = QtWidgets.QAction(QIcon('usdpricetag_5102.ico'), " Prices    ", Form2)

        #def ff():
            #print("new")

        e.triggered.connect(self.open_New_Player)
        e.triggered.connect(Form2.close)
        #e1.triggered.connect(ff)
        e2.triggered.connect(self.open_Captains)
        e2.triggered.connect(Form2.close)
        e3.triggered.connect(self.open_Prices)
        e3.triggered.connect(Form2.close)
        f1.addAction(e)
        #f1.addAction(e1)
        f1.addAction(e2)
        f1.addAction(e3)
        self.label = QtWidgets.QLabel(Form2)# هنا تظهر صوره الاعب
        self.label.setGeometry(QtCore.QRect(420, 80, 350, 400))
        self.label.setStyleSheet("background-color: rgb(238, 233, 233);")
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(Form2)
        self.label_8.setGeometry(QtCore.QRect(60, 300, 71, 20))
        self.label_8.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Form2)# ده لما يدوس عليه ينقص من المرات اللي ليه و يزود ف اللي حضرها
        self.pushButton.clicked.connect(self.times_players)
        self.pushButton.setGeometry(QtCore.QRect(150, 490, 41, 23))
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(238, 233, 230);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "\n}"
                                      "QPushButton:hover{background-color: rgb(238, 233, 230);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "\n}"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form2)# عدد الحصص اللي حضرها
        self.lineEdit.setGeometry(QtCore.QRect(100, 490, 31, 20))
        self.lineEdit.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_12 = QtWidgets.QLabel(Form2)
        self.label_12.setGeometry(QtCore.QRect(60, 100, 71, 20))
        self.label_12.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form2)
        self.label_13.setGeometry(QtCore.QRect(60, 140, 111, 20))
        self.label_13.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form2)
        self.label_14.setGeometry(QtCore.QRect(60, 180, 71, 20))
        self.label_14.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form2)
        self.label_15.setGeometry(QtCore.QRect(60, 260, 71, 20))
        self.label_15.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form2)
        self.label_16.setGeometry(QtCore.QRect(60, 340, 101, 20))
        self.label_16.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form2)
        self.label_17.setGeometry(QtCore.QRect(60, 380, 91, 20))
        self.label_17.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form2)
        self.label_18.setGeometry(QtCore.QRect(60, 460, 51, 20))
        self.label_18.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form2)
        self.label_19.setGeometry(QtCore.QRect(60, 530, 81, 20))
        self.label_19.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form2)
        self.label_20.setGeometry(QtCore.QRect(60, 600, 61, 20))
        self.label_20.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form2)# عدد الحصص اللي ليه
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 560, 31, 20))
        self.lineEdit_3.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_21 = QtWidgets.QLabel(Form2)# هنا يظهر اسم الاعب
        self.label_21.setGeometry(QtCore.QRect(110, 100, 270, 20))
        self.label_21.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Form2)# هنا يظهر ال ID
        self.label_22.setGeometry(QtCore.QRect(90, 180, 120, 20))
        self.label_22.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form2)# تاريخ التجديد
        self.label_23.setGeometry(QtCore.QRect(150, 380, 81, 20))
        self.label_23.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form2)# تاريخ الدفع
        self.label_24.setGeometry(QtCore.QRect(170, 340, 101, 20))
        self.label_24.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_24.setObjectName("label_24")
        self.label_9 = QtWidgets.QLabel(Form2)# نوع الاشتراك حسب جدول الاسعار
        self.label_9.setGeometry(QtCore.QRect(140, 300, 180, 20))
        self.label_9.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_25 = QtWidgets.QLabel(Form2)#رقم التليفون
        self.label_25.setGeometry(QtCore.QRect(170, 140, 111, 20))
        self.label_25.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Form2)# العنوان
        self.label_26.setGeometry(QtCore.QRect(130, 260, 190, 20))
        self.label_26.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(Form2)
        self.label_28.setGeometry(QtCore.QRect(60, 420, 61, 20))
        self.label_28.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(Form2)
        self.label_29.setGeometry(QtCore.QRect(270, 20, 251, 41))
        self.label_29.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
                                    "font: 24pt \"MS Shell Dlg 2\";")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(Form2)
        self.label_30.setGeometry(QtCore.QRect(60, 220, 90, 20))
        self.label_30.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Form2)# العمر
        self.label_31.setGeometry(QtCore.QRect(120, 220, 290, 20))
        self.label_31.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(Form2)# المبلغ المدفوع
        self.label_32.setGeometry(QtCore.QRect(120, 420, 61, 20))
        self.label_32.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_32.setObjectName("label_32")
        self.pushButton_2 = QtWidgets.QPushButton(Form2)#زرار ال DELETE
        self.pushButton_2.clicked.connect(self.delete_player)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 640, 131, 31))
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
        self.pushButton_3 = QtWidgets.QPushButton(Form2)# زرار ال UPDATE
        self.pushButton_3.clicked.connect(self.open_New_Player)
        self.pushButton_3.clicked.connect(Form2.close)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 640, 131, 31))
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
        self.pushButton_3.setObjectName("pushButton_2")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        db = sqlite3.connect("app_db.db")
        cur = db.cursor()
        cur.execute("SELECT * FROM cache WHERE cache_name='inf'")
        get_data=cur.fetchone()
        print(get_data)
        clmn2 = get_data[1]

        clmn3 = get_data[2]

        clmn4 = get_data[3]

        clmn5 = get_data[4]

        clmn6 = get_data[5]

        clmn7 = get_data[6]

        clmn8 = get_data[7]

        clmn9 = get_data[8]

        clmn11 = get_data[9]

        clmn12 = get_data[10]

        clmn13 = get_data[11]

        clmn14 = get_data[12]

        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Info"))
        self.label.setScaledContents(True)
        image = QtGui.QPixmap()
        image.loadFromData(clmn12,'png')
        self.label.setPixmap(image)
        self.label.setText(_translate("Form2", ""))
        self.label_8.setText(_translate("Form2", "Sub Type:"))
        self.pushButton.setText(_translate("Form2", "Add"))
        self.label_12.setText(_translate("Form2", "Name:"))
        self.label_13.setText(_translate("Form2", "Phone Number:"))
        self.label_14.setText(_translate("Form2", "ID:"))
        self.label_15.setText(_translate("Form2", "Address:"))
        self.label_16.setText(_translate("Form2", "Payment Date:"))
        self.label_17.setText(_translate("Form2", "Renew Date:"))
        self.label_18.setText(_translate("Form2", "Times:"))
        self.label_19.setText(_translate("Form2", "Times Left:"))
        self.label_21.setText(_translate("Form2", clmn2))
        self.label_22.setText(_translate("Form2", clmn4))
        self.label_23.setText(_translate("Form2", clmn8))
        self.label_24.setText(_translate("Form2", clmn7))
        self.label_9.setText(_translate("Form2", clmn11))
        self.label_25.setText(_translate("Form2",clmn3))
        self.label_26.setText(_translate("Form2", clmn5))
        self.label_28.setText(_translate("Form2", "Paid Up:"))
        self.label_29.setText(_translate("Form2", "Info About Player"))
        self.label_30.setText(_translate("Form2", "E-MAIL:"))
        self.label_31.setText(_translate("Form2",clmn9))
        self.label_32.setText(_translate("Form2",clmn6))
        self.lineEdit.setText(clmn13)
        self.lineEdit_3.setText(clmn14)
        self.pushButton_2.setText(_translate("Form2", "Delete"))
        self.pushButton_3.setText(_translate("Form2", "Update"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QMainWindow()
    ui = Ui_Form2()
    ui.setupUi(Form2)
    Form2.show()
    sys.exit(app.exec_())
