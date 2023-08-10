from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Form4(object):
    def open_Prices(self):
                from prices import Ui_Form5
                self.window8 = QtWidgets.QMainWindow()
                self.ui = Ui_Form5()
                self.ui.setupUi(self.window8)
                self.window8.show()
    def open_New_Player(self):
                from inter_the_info import Ui_Form3
                self.window6 = QtWidgets.QMainWindow()
                self.ui = Ui_Form3()
                self.ui.setupUi(self.window6)
                self.window6.show()

    def open_Info(self):
                from info_about_player import Ui_Form2
                self.window5 = QtWidgets.QMainWindow()
                self.ui = Ui_Form2()
                self.ui.setupUi(self.window5)
                self.window5.show()
    def setupUi(self, Form4):
        Form4.setObjectName("Form4")
        Form4.resize(776, 704)
        Form4.setFixedWidth(776)
        Form4.setFixedHeight(704)
        Form4.setAcceptDrops(True)
        Form4.setStyleSheet("background-color: rgb(248, 147, 31);")
        Form4.setWindowIcon(QtGui.QIcon("gym-icon_30328.ico"))
        Form4.setStyleSheet("background-color: rgb(248, 147, 31);")
        f1 = Form4.menuBar().addMenu("Options")
        f1.setStyleSheet("background-color:  rgb(248, 132, 31);")
        e = QtWidgets.QAction(QIcon('football_player_sport_olympic_player_icon_123803.ico'), " New Player ", Form4)
        e1 = QtWidgets.QAction(QIcon('new_add_user_info_16706.ico'), " Info Player", Form4)
        # e2 = QtWidgets.QAction(" Captains   ", Form4)
        e3 = QtWidgets.QAction(QIcon('usdpricetag_5102.ico'), " Prices     ", Form4)

        # def ff():
        # print("new")

        e.triggered.connect(self.open_New_Player)
        e.triggered.connect(Form4.close)
        e1.triggered.connect(self.open_Info)
        e1.triggered.connect(Form4.close)
        # e2.triggered.connect(ff)
        e3.triggered.connect(self.open_Prices)
        e3.triggered.connect(Form4.close)
        f1.addAction(e)
        f1.addAction(e1)
        # f1.addAction(e2)
        f1.addAction(e3)

        self.label_13 = QtWidgets.QLabel(Form4)
        self.label_13.setGeometry(QtCore.QRect(280, 20, 131, 41))
        self.label_13.setStyleSheet("\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.tabWidget = QtWidgets.QTabWidget(Form4)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 50, 781, 771))
        self.tabWidget.setStyleSheet("background-color: rgb(248, 147, 31);\n"
"font: 75 10pt \"Yu Gothic UI Semibold\";\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(40, 30, 131, 31))
        self.label_14.setStyleSheet("color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(230, 76, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(0, 0, 0);")
        self.label_14.setObjectName("label_14")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 541, 91))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(40, 190, 131, 31))
        self.label_16.setStyleSheet("color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Yu Gothic UI Semibold\";")
        self.label_16.setObjectName("label_16")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 220, 541, 91))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 380, 541, 91))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 530, 541, 91))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(40, 350, 131, 31))
        self.label_17.setStyleSheet("color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Yu Gothic UI Semibold\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(50, 500, 121, 31))
        self.label_18.setStyleSheet("color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Yu Gothic UI Semibold\";")
        self.label_18.setObjectName("label_18")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 521, 71))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Yu Gothic UI Semibold\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 390, 521, 71))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Yu Gothic UI Semibold\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(50, 70, 501, 71))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Yu Gothic UI Semibold\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(180, 40, 71, 21))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(180, 200, 71, 21))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(180, 360, 81, 21))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(180, 510, 81, 21))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 540, 511, 71))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(40, 30, 121, 31))
        self.label_19.setStyleSheet("color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Yu Gothic UI Semibold\";")
        self.label_19.setObjectName("label_19")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_5.setGeometry(QtCore.QRect(40, 60, 531, 91))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(40, 190, 121, 31))
        self.label_20.setStyleSheet("color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Yu Gothic UI Semibold\";")
        self.label_20.setObjectName("label_20")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_6.setGeometry(QtCore.QRect(40, 220, 541, 91))
        self.textEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(40, 350, 121, 31))
        self.label_21.setStyleSheet("color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Yu Gothic UI Semibold\";")
        self.label_21.setObjectName("label_21")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_7.setGeometry(QtCore.QRect(40, 380, 541, 91))
        self.textEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(50, 390, 511, 71))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Yu Gothic UI Semibold\";")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(50, 230, 521, 71))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(50, 70, 511, 71))
        self.label_22.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(170, 40, 91, 21))
        self.label_23.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(170, 200, 91, 21))
        self.label_24.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(170, 360, 91, 21))
        self.label_25.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_25.setObjectName("label_25")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form4)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form4)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form4", "captains"))
        self.label_13.setText(_translate("Form4", "Captains"))
        self.label_14.setText(_translate("Form4", "Mohamed Essam"))
        self.label_16.setText(_translate("Form4", "Ahmed Ibrahim"))
        self.label_17.setText(_translate("Form4", "Omer Elsaid"))
        self.label_18.setText(_translate("Form4", "Hesham Negm"))
        self.label_2.setText(_translate("Form4", "Certified trainer and pharmacist\n"
"Professional equipment specialist according to the game or sport\n"
"Rehabilitation and post-traumatic sports specialist\n"
"It combines medical and sports methods."))
        self.label_3.setText(_translate("Form4", "Yoga Vinyasa Specialist, Boxing and Bodybuilding Coach\n"
"and physical rehabilitation\n"
"Dietitian with 5 years experience in the sports field"))
        self.label_4.setText(_translate("Form4", "A graduate of the Faculty of Physical Education and a certified trainer\n"
"from the International Gym Academy\n"
"He is a certified trainer from the Arab Federation for Bodybuilding and Sports\n"
"Fitness and bodybuilding specialist"))
        self.label_5.setText(_translate("Form4", "  12  :  6 PM"))
        self.label_6.setText(_translate("Form4", "  12  :  6 PM"))
        self.label_7.setText(_translate("Form4", "  6  :  10  PM"))
        self.label_8.setText(_translate("Form4", "  6  :  10  PM"))
        self.label.setText(_translate("Form4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic UI Semibold\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A bodybuilding coach with international certificates in training and sports nutrition.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Master\'s degree in physical education</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Eveninig Period"))
        self.label_19.setText(_translate("Form4", "Amr shalaby"))
        self.label_20.setText(_translate("Form4", "Tarek Eltaweel"))
        self.label_21.setText(_translate("Form4", "Samir Elshamy"))
        self.label_10.setText(_translate("Form4", "Graduated from the Faculty of Physiotherapy and an expert fitness trainer\n"
"And rehabilitation and holds a certificate from the Egyptian Federation of Sports"))
        self.label_12.setText(_translate("Form4", "Graduated from the Faculty of Physical Education\n"
"Certified coach by the International Federation\n"
"Boxing coach\n"
"Experience in dealing with accident cases"))
        self.label_22.setText(_translate("Form4", "Graduated from the Faculty of Physical Education Expert Specialist\n"
"Boxing and gymnastics coach\n"
"Experience in dealing with accident cases\n"
"and physical rehabilitation"))
        self.label_23.setText(_translate("Form4", " 7 AM : 12 PM"))
        self.label_24.setText(_translate("Form4", " 7 AM : 12 PM"))
        self.label_25.setText(_translate("Form4", " 7 AM : 12 PM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form4", "Morning Period"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form4 = QtWidgets.QMainWindow()
    ui = Ui_Form4()
    ui.setupUi(Form4)
    Form4.show()
    sys.exit(app.exec_())
