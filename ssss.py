from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import  re
from PyQt5.QtGui import QPixmap, QIcon
from os.path import isfile
import sqlite3


class Ui_Form3(object):
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

    def open_Info_Of_Player(self):
        from info_about_player import Ui_Form2
        self.window9 = QtWidgets.QMainWindow()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.window9)
        self.window9.show()

    def open_Camera(self):
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                break
            elif k % 256 == 32:
                # SPACE pressed
                global count
                count = 1
                img_name = f"E:/Dr_Amr_Project_2/Images/{count}.png"
                while isfile(img_name) == True:
                    count += 1
                    img_name = f"E:/Dr_Amr_Project_2/Images/{count}.png"

                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
           # img_counter += 1

        cam.release()

        cv2.destroyAllWindows()

    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(776, 717)
        Form3.setMaximumSize(776, 717)
        Form3.setWindowIcon(QtGui.QIcon("gym-icon_30328.ico"))
        Form3.setStyleSheet("background-color: rgb(248, 147, 31);")
        f1 = Form3.menuBar().addMenu("Options")
        f1.setStyleSheet("background-color:  rgb(248, 132, 31);")
        # e = QtWidgets.QAction(" New Player ", Form3)
        e1 = QtWidgets.QAction(QIcon('new_add_user_info_16706.ico'), " Info Of Player", Form3)
        e2 = QtWidgets.QAction(QIcon('medal_champion_award_winner_olympic_icon_207819.ico'), " Captains   ", Form3)
        e3 = QtWidgets.QAction(QIcon('usdpricetag_5102.ico'), " Prices     ", Form3)

        # def ff():
        # print("new")

        # e.triggered.connect(ff)
        e1.triggered.connect(self.open_Info_Of_Player)
        e1.triggered.connect(Form3.close)
        e2.triggered.connect(self.open_Captains)
        e2.triggered.connect(Form3.close)
        e3.triggered.connect(self.open_Prices)
        e3.triggered.connect(Form3.close)
        # f1.addAction(e)
        f1.addAction(e1)
        f1.addAction(e2)
        f1.addAction(e3)
        self.label_12 = QtWidgets.QLabel(Form3)
        self.label_12.setGeometry(QtCore.QRect(30, 300, 71, 20))
        self.label_12.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Form3)
        self.label_14.setGeometry(QtCore.QRect(30, 370, 71, 20))
        self.label_14.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(Form3)
        self.label_17.setGeometry(QtCore.QRect(370, 510, 83, 20))
        self.label_17.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(Form3)
        self.label_16.setGeometry(QtCore.QRect(370, 440, 101, 20))
        self.label_16.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.label_13 = QtWidgets.QLabel(Form3)
        self.label_13.setGeometry(QtCore.QRect(370, 300, 111, 20))
        self.label_13.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(Form3)
        self.label_15.setGeometry(QtCore.QRect(370, 370, 71, 20))
        self.label_15.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.lineEdit = QtWidgets.QLineEdit(Form3)  # name
        self.lineEdit.setGeometry(QtCore.QRect(100, 300, 221, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                    "border-radius: 8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form3)  # phone number
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 300, 221, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                      "border-radius: 8px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form3)  # address
        self.lineEdit_3.setGeometry(QtCore.QRect(490, 370, 221, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                      "border-radius: 8px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form3)  # ID
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 370, 221, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                      "border-radius: 8px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_28 = QtWidgets.QLabel(Form3)
        self.label_28.setGeometry(QtCore.QRect(30, 440, 61, 20))
        self.label_28.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_28.setObjectName("label_28")
        self.label_8 = QtWidgets.QLabel(Form3)
        self.label_8.setGeometry(QtCore.QRect(300, 575, 71, 20))
        self.label_8.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(Form3)
        self.comboBox.setGeometry(QtCore.QRect(390, 575, 141, 22))
        self.comboBox.setStyleSheet("background-color: rgb(238, 233, 233);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_32 = QtWidgets.QLabel(Form3)
        self.label_32.setGeometry(QtCore.QRect(600, 555, 141, 22))
        self.label_32.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_32.setObjectName("label_32")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form3)
        self.lineEdit_12.setGeometry(QtCore.QRect(680, 555, 31, 20))
        self.lineEdit_12.setStyleSheet("background-color: rgb(238, 233, 233);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_33 = QtWidgets.QLabel(Form3)
        self.label_33.setGeometry(QtCore.QRect(600, 595, 141, 22))
        self.label_33.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_33.setObjectName("label_33")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form3)
        self.lineEdit_13.setGeometry(QtCore.QRect(680, 595, 31, 20))
        self.lineEdit_13.setStyleSheet("background-color: rgb(238, 233, 233);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_27 = QtWidgets.QLabel(Form3)
        self.label_27.setGeometry(QtCore.QRect(240, 30, 361, 41))
        self.label_27.setStyleSheet("\n"
                                    "font: 24pt \"MS Shell Dlg 2\";")
        self.label_27.setObjectName("label_27")
        self.radioButton = QtWidgets.QRadioButton(Form3)
        self.radioButton.setGeometry(QtCore.QRect(190, 575, 82, 17))
        self.radioButton.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form3)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 575, 82, 17))
        self.radioButton_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_29 = QtWidgets.QLabel(Form3)
        self.label_29.setGeometry(QtCore.QRect(30, 570, 61, 20))
        self.label_29.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_29.setObjectName("label_29")
        self.label = QtWidgets.QLabel(Form3)
        self.label.setGeometry(QtCore.QRect(40, 80, 170, 191))
        self.label.setStyleSheet("background-color: rgb(238, 233, 233);")
        self.label.setObjectName("label")
        self.label_30 = QtWidgets.QLabel(Form3)
        self.label_30.setGeometry(QtCore.QRect(30, 510, 61, 20))
        self.label_30.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Form3)
        self.label_31.setGeometry(QtCore.QRect(280, 610, 220, 31))
        self.label_31.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_31.setObjectName("label_31")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form3)  # renew date
        self.lineEdit_7.setGeometry(QtCore.QRect(490, 510, 221, 31))
        self.lineEdit_7.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                      "border-radius: 8px;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form3)  # payment date
        self.lineEdit_10.setGeometry(QtCore.QRect(490, 440, 221, 31))
        self.lineEdit_10.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                       "border-radius: 8px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form3)  # paid up
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 440, 221, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                      "border-radius: 8px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form3)  # E-mail
        self.lineEdit_11.setGeometry(QtCore.QRect(100, 510, 221, 31))
        self.lineEdit_11.setStyleSheet("background-color: rgb(238, 233, 233);\n"
                                       "border-radius: 8px;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton = QtWidgets.QPushButton(Form3)
        self.pushButton.clicked.connect(self.update)
        self.pushButton.setGeometry(QtCore.QRect(250, 640, 131, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(238, 233, 233);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "border-radius: 8px;\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form3)
        self.pushButton_2.clicked.connect(self.get_data)
        #self.pushButton_2.clicked.connect(self.when_create_clicked)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 640, 131, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(238, 233, 233);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";\n"
                                        "border-radius: 8px;\n"
                                        "\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form3)
        self.pushButton_3.clicked.connect(self.open_Camera)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 120, 131, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(238, 233, 233);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";\n"
                                        "border-radius: 8px;\n"
                                        "\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_4 = QtWidgets.QPushButton(Form3)
        # self.pushButton_4.clicked.connect(self.Take_Shoot)
        # self.pushButton_4.setGeometry(QtCore.QRect(250, 190, 131, 51))
        # self.pushButton_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
        # "color: rgb(238, 233, 233);\n"
        # "font: 12pt \"MS Shell Dlg 2\";\n"
        # "border-radius: 8px;\n"
        # "\n"
        # "")
        # self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    # def when_create_clicked(self):
        #name = self.lineEdit.text()
        #phone = self.lineEdit_2.text()
        #i_d = self.lineEdit_4.text()
        #address = self.lineEdit_3.text()
        #paidUp = self.lineEdit_5.text()
        #paymentDate = self.lineEdit_10.text()
        #renewDate = self.lineEdit_7.text()
        #email = self.lineEdit_11.text()
        #tyPe = self.radioButton.text()
        #subtype = self.comboBox.itemText(self.comboBox.currentIndex())



    def get_data(self):
        #name = ""
        #phone = ""
        #i_d = ""
        #address = ""
        #paidUp = ""
        #paymentDate = ""
        #email = ""
        #renewDate = ""
        #tyPe = ""
        #subType = ""



        name = self.lineEdit.text()
        phone = self.lineEdit_2.text()
        i_d = self.lineEdit_4.text()
        address = self.lineEdit_3.text()
        paidUp = self.lineEdit_5.text()
        paymentDate = self.lineEdit_10.text()
        renewDate = self.lineEdit_7.text()
        email = self.lineEdit_11.text()
        tyPe = self.radioButton.text()
        times =self.lineEdit_12.text()
        times_lift = self.lineEdit_13.text()

        subtype = self.comboBox.itemText(self.comboBox.currentIndex())
        conn = sqlite3.connect("app_db.db")
        c = conn.cursor()

        #regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        if len(name) == 0:
            self.label_31.setText(" \U0001F600 Enter The Name")
        elif len(phone) == 0:
            self.label_31.setText(" \U0001F600 Enter The phone")
        elif len(phone) != 11:
            self.label_31.setText(" \U0001F600 The phone Must equal to 11")
        elif len(i_d) == 0:
            self.label_31.setText(" \U0001F600 Enter The ID")
        elif len(i_d) != 14:
            self.label_31.setText(" \U0001F600 ID Must equal to 14")
        elif len(address) == 0:
            self.label_31.setText(" \U0001F600 Enter The address")
        elif len(paidUp) == 0:
            self.label_31.setText(" \U0001F600 Enter The paidUp")
        elif len(paymentDate) == 0:
            self.label_31.setText(" \U0001F600 Enter The paymentDate")
        elif len(renewDate) == 0:
            self.label_31.setText(" \U0001F600 Enter The renewDate")
        elif len(email) == 0:
            self.label_31.setText(" \U0001F600 Enter The E-mail")
        #elif re.fullmatch(regex,email):
            #self.label_31.setText(" \U0001F600 E-mail be like (name@gmail.com)")
        else:

            img_name = f"E:/Dr_Amr_Project_2/Images/{count}.png"

            with open(img_name , 'rb') as binary_image:
                binary_code=binary_image.read()
            print(binary_code)
            c.execute(
                "CREATE TABLE IF NOT EXISTS players_datas( id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT NOT NULL,phone TEXT NOT NULL,i_d TEXT NOT NULL,address TEXT NOT NULL,paidUp TEXT NOT NULL,paymentDate TEXT NOT NULL,renewDate TEXT NOT NULL,email TEXT NOT NULL UNIQUE,tyPe TEXT NOT NULL, subtype TEXT NOT NULL , image BLOB, times TEXT NOT NULL , times_lift TEXT)")
            c.execute(
                "INSERT INTO players_datas (name,phone,i_d,address,paidUp,paymentDate,renewDate,email,tyPe,subtype,image,times,times_lift) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (name, phone, i_d, address, paidUp, paymentDate, renewDate, email, tyPe, subtype,binary_code,times,times_lift))
            conn.commit()
            print('data inserted to db')
            conn.close()
            if self.pushButton_2.clicked.connect(self.get_data):
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_4.clear()
                self.lineEdit_3.clear()
                self.lineEdit_5.clear()
                self.lineEdit_10.clear()
                self.lineEdit_7.clear()
                self.lineEdit_11.clear()
                self.lineEdit_12.clear()
                #self.radioButton.clear()
                self.comboBox.clear()
    def update(self):

        self.name = self.lineEdit.text()
        #phone = self.lineEdit_2.text()
        #i_d = self.lineEdit_4.text()
        #address = self.lineEdit_3.text()
        self.paidUp = self.lineEdit_5.text()
        self.paymentDate = self.lineEdit_10.text()
        self.renewDate = self.lineEdit_7.text()
        #email = self.lineEdit_11.text()
        #tyPe = self.radioButton.text()
        self.subtype = self.comboBox.itemText(self.comboBox.currentIndex())

        conn = sqlite3.connect("app_db.db")
        c = conn.cursor()
        # print('Successful','player is added successfully to the database.')
        #c.execute(
            #"CREATE TABLE IF NOT EXISTS players_datas( id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,phone TEXT,i_d TEXT,address TEXT,paidUp TEXT,paymentDate TEXT,renewDate TEXT,email TEXT,tyPe TEXT,subtype TEXT)")
        #query = "UPDATE players_datas SET paidUp = ?, paymentDate = ?, renewDate = ?,subtype =?  WHERE name = ?"
        #c.execute(query,(self.name,self.paidUp, self.paymentDate, self.renewDate,self.subtype))

        c.execute(f"update players_datas set paidUp = '{self.paidUp}' , paymentDate = '{self.paymentDate}' ,renewDate = '{self.renewDate}',subtype ='{self.subtype}' where name='{self.name}'")
        print("the table update")
        conn.commit()
        conn.close()

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "New Player"))
        self.label_12.setText(_translate("Form3", "Name:"))
        self.label_14.setText(_translate("Form3", "ID:"))
        self.label_17.setText(_translate("Form3", "Renew Date:"))
        self.label_16.setText(_translate("Form3", "Payment Date:"))
        self.label_13.setText(_translate("Form3", "Phone Number:"))
        self.label_15.setText(_translate("Form3", "Address:"))
        self.label_28.setText(_translate("Form3", "Paid Up:"))
        self.label_32.setText(_translate("Form3", "Times: "))
        self.label_33.setText(_translate("Form3", "Times Left: "))
        self.label_8.setText(_translate("Form3", "Sub Type:"))
        self.comboBox.setItemText(0, _translate("Form3", "silver1 : 8times (150)"))
        self.comboBox.setItemText(1, _translate("Form3", "silver2 :12times(190)"))
        self.comboBox.setItemText(2, _translate("Form3", "gold1 : 16times(225)"))
        self.comboBox.setItemText(3, _translate("Form3", "gold2 : everyday(265)"))
        self.comboBox.setItemText(4, _translate("Form3", "diamond1 : 3month(20%)"))
        self.comboBox.setItemText(5, _translate("Form3", "diamond2 :  6months(30%)"))
        self.comboBox.setItemText(6, _translate("Form3", "premium : 1year(40%)"))
        self.label_27.setText(_translate("Form3", "Entre The Info Of Player"))
        self.radioButton.setText(_translate("Form3", "Male"))
        self.radioButton_2.setText(_translate("Form3", "Female"))
        self.label_29.setText(_translate("Form3", "Gender:"))
        self.label.setText(
            _translate("Form3", "Kindly Press Open Camera to Show\nThen Press Space\nTo Take a Shoot and Save Image"))
        # self.pixmap = QPixmap('E:/Dr_Amr_Project_2/Images/{count}.png')
        # self.label.setPixmap(self.pixmap)
        self.label_30.setText(_translate("Form3", "E-mail:"))
        self.label_31.setText(_translate("Form3", "qwertyuiopqwertyuioqqwertyuio"))
        self.pushButton.setText(_translate("Form3", "Update"))
        self.pushButton_2.setText(_translate("Form3", "Create"))
        self.pushButton_3.setText(_translate("Form3", "Open Camera"))
        # self.pushButton_4.setText(_translate("Form3", "Take a Shoot"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form3 = QtWidgets.QMainWindow()
    ui = Ui_Form3()
    ui.setupUi(Form3)
    Form3.show()
    sys.exit(app.exec_())
