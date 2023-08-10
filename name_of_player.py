import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon



class Ui_Form1(object):
    def search(self):
        try:
            db = sqlite3.connect("app_db.db")

            print("the connect is successfully")
            # c=db.cursor()
            # c.execute(
            #     "CREATE TABLE IF NOT EXISTS cache ( id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,phone TEXT,i_d TEXT,address TEXT,paidUp TEXT,paymentDate TEXT,renewDate TEXT,email TEXT,tyPe TEXT,subtype TEXT)")
            # db.commit()
            name = self.lineEdit.text()
            cur = db.cursor()
            cur.execute("SELECT name FROM players_datas WHERE name = ?", (name,))
            clmn2 = cur.fetchone()[0]
            print(clmn2)
            cur.execute("SELECT phone FROM players_datas WHERE name = ?", (name,))
            clmn3 = cur.fetchone()[0]
            print(clmn3)
            cur.execute("SELECT i_d FROM players_datas WHERE name = ?", (name,))
            clmn4 = cur.fetchone()[0]
            print(clmn4)
            cur.execute("SELECT address FROM players_datas WHERE name = ?", (name,))
            clmn5 = cur.fetchone()[0]
            print(clmn5)
            cur.execute("SELECT paidUp FROM players_datas WHERE name = ?", (name,))
            clmn6 = cur.fetchone()[0]
            print(clmn6)
            cur.execute("SELECT paymentDate FROM players_datas WHERE name = ?", (name,))
            clmn7 = cur.fetchone()[0]
            print(clmn7)
            cur.execute("SELECT renewDate FROM players_datas WHERE name = ?", (name,))
            clmn8 = cur.fetchone()[0]
            print(clmn8)
            cur.execute("SELECT email FROM players_datas WHERE name = ?", (name,))
            clmn9 = cur.fetchone()[0]
            print(clmn9)
            cur.execute("SELECT subtype FROM players_datas WHERE name = ?", (name,))
            clmn11 = cur.fetchone()[0]
            print(clmn11)
            cur.execute("SELECT image FROM players_datas WHERE name = ?", (name,))
            clmn12 = cur.fetchone()[0]
            print(clmn12)
            cur.execute("SELECT times FROM players_datas WHERE name = ?", (name,))
            clmn13 = cur.fetchone()[0]
            print(clmn13)
            cur.execute("SELECT times_lift FROM players_datas WHERE name = ?", (name,))
            clmn14 = cur.fetchone()[0]
            print(clmn14)
            # db.commit()
            # db.close()
            # dbs = sqlite3.connect("app_db.db")
            c=db.cursor()
            c.execute("UPDATE cache SET name = ?, phone = ?, i_d = ?, address = ?, paidUp = ?, paymentDate = ?, renewDate = ?,email = ?,subtype = ?, image = ?, times = ?, times_lift = ?  WHERE cache_name = 'inf' ",
                (clmn2, clmn3, clmn4, clmn5, clmn6, clmn7, clmn8, clmn9, clmn11, clmn12, clmn13,clmn14))

            db.commit()
            from info_about_player import Ui_Form2
            self.window5 = QtWidgets.QMainWindow()
            self.ui = Ui_Form2()
            self.ui.setupUi(self.window5)
            self.window5.show()
            self.label_9.setText(" ")
        except:
            self.label_9.setText("This Player is not Signing")

    def Logout(self):
        from logo import Ui_welcome
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_welcome()
        self.ui.setupUi(self.window1)
        self.window1.show()
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
    #def open_Info(self):
        #from info_about_player import Ui_Form2
        #self.window5 = QtWidgets.QMainWindow()
        #self.ui = Ui_Form2()
        #self.ui.setupUi(self.window5)
        #self.window5.show()

    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(776, 717)
        Form1.move(200,100)
        Form1.setMaximumSize(776, 717)
        Form1.setWindowIcon(QtGui.QIcon("gym-icon_30328.ico"))
        Form1.setStyleSheet("background-color: rgb(248, 147, 31);")
        f1 = Form1.menuBar().addMenu("Options")
        f1.setStyleSheet("background-color: rgb(248, 132, 31);")
        e = QtWidgets.QAction(QIcon('football_player_sport_olympic_player_icon_123803.ico')," New Player ", Form1)
        #e1 = QtWidgets.QAction(" Info Of Player", Form1)
        e2 = QtWidgets.QAction(QIcon('medal_champion_award_winner_olympic_icon_207819.ico')," Captains   ", Form1)
        e3 = QtWidgets.QAction(QIcon('usdpricetag_5102.ico')," Prices     ", Form1)
        e4 = QtWidgets.QAction(QIcon('logout_icon-icons.com_51025.ico')," Logout     ", Form1)

        #def ff():
           #print("new")

        e.triggered.connect(self.open_New_Player)
        #e1.triggered.connect(ff)
        e2.triggered.connect(self.open_Captains)
        e3.triggered.connect(self.open_Prices)
        e4.triggered.connect(self.Logout)
        e4.triggered.connect(Form1.close)
        f1.addAction(e)
        #f1.addAction(e1)
        f1.addAction(e2)
        f1.addAction(e3)
        f1.addAction(e4)
        self.label_9 = QtWidgets.QLabel(Form1)
        self.label_9.setGeometry(QtCore.QRect(340, 250, 281, 31))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                   "color:red;")
        self.pushButton = QtWidgets.QPushButton(Form1)# ده الزرار اللي اول ما يدوس عليه يعرض كل بيانات اللاعب في الصفحه اللي بعد دي
        self.pushButton.clicked.connect(self.search)
        #self.pushButton.clicked.connect(self.open_Info)
        self.pushButton.setGeometry(QtCore.QRect(350, 280, 161, 31))
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
        self.lineEdit = QtWidgets.QLineEdit(Form1)# ده الfield بتاع السيرش اللي هيدخل فيه الاسم او ال id شوف الاسهل و اعمله
        self.lineEdit.setGeometry(QtCore.QRect(310, 190, 261, 31))
        self.lineEdit.setStyleSheet("QLineEdit{background-color: rgb(238, 233, 233);\n"
                                    "border:2px solid rgb(238, 233, 233);"
                                    "border-radius: 8px;}"
                                    "QLineEdit:focus{border: 2px solid black}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form1)
        self.label.setGeometry(QtCore.QRect(170, 190, 121, 21))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_27 = QtWidgets.QLabel(Form1)
        self.label_27.setGeometry(QtCore.QRect(200, 30, 381, 41))
        self.label_27.setStyleSheet("\n"
                                    "font: 24pt \"MS Shell Dlg 2\";")
        self.label_27.setObjectName("label_27")

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "Enter The Name Of Player"))
        self.pushButton.setText(_translate("Form1", "Get Info"))
        self.label.setText(_translate("Form1", "Name Of Player:"))
        self.label_27.setText(_translate("Form1", "Enter The Name Of Player"))
        self.label_9.setText(_translate("Form1", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QMainWindow()
    ui = Ui_Form1()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())

