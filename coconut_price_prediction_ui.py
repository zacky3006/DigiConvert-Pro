from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import tkinter
import tkinter as tk
import math

class CoconutPricePredictionUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ทำนายราคมะพร้าว")
        MainWindow.resize(636, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 641, 361))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 381))
        self.label.setStyleSheet("background-image: url(:/ee/Downloads/pngtree-summer-sea-coconut-tree-background-image_1948422 (1).jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(240, 110, 221, 21))
        self.radioButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(216, 144, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 130, 221, 21))
        self.radioButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(216, 144, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 150, 221, 21))
        self.radioButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(216, 144, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_3.setObjectName("radioButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 80, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 170, 221, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 79, 81, 31))
        self.label_2.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(212, 212, 212);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 110, 81, 61))
        self.label_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(212, 212, 212);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 170, 81, 31))
        self.label_4.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(212, 212, 212);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 200, 301, 51))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(216, 144, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(160, 250, 301, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "    size 3(12-14นิ้ว)"))
        self.radioButton_2.setText(_translate("MainWindow", "    size 2(10-11นิ้ว)"))
        self.radioButton_3.setText(_translate("MainWindow", "    size 1(6-9นิ้ว)"))
        self.label_2.setText(_translate("MainWindow", "วันที่(Date)"))
        self.label_3.setText(_translate("MainWindow", "ขนาด(SIZE)"))
        self.label_4.setText(_translate("MainWindow", "น้ำหนัก(weight)"))
        self.pushButton.setText(_translate("MainWindow", "คำนวณราคา"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ราคาที่ทำนายว่าจะได้</span></p></body></html>"))


        self.pushButton.clicked.connect(self.predict_price)

    def predict_price(self):
        # Read user input from the UI
        date = int(self.textEdit.toPlainText())
        size = int(self.textEdit.toPlainText())  # You might need to change this to the appropriate widget.
        weight = float(self.textEdit_2.toPlainText())  # You might need to change this to the appropriate widget.
        
        # Read user input from the UI
        date = int(self.textEdit.toPlainText())
        size = 0  # Initialize size to 0
        if self.radioButton.isChecked():
            size = 1
        elif self.radioButton_2.isChecked():
            size = 2
        elif self.radioButton_3.isChecked():
            size = 3
        weight = float(self.textEdit_2.toPlainText())  # You might need to change this to the appropriate widget.

        # Load and preprocess your dataset
        file_path = r'C:\Users\66930\Desktop\projact\coco2.csv'
        df = pd.read_csv(file_path)
        X = df[['date', 'size', 'weight']]
        y = df['price']

        # Create a Linear Regression model
        lrm = LinearRegression()
        lrm.fit(X, y)

        # Make a prediction with user inputs
        new_data = [[date, size, weight]]
        predicted_price = lrm.predict(new_data)

        # Display the result in the QTextBrowser
        self.textBrowser_2.setPlainText(f'ราคาที่ทำนาย: {predicted_price[0]:.2f}')
        # Load and preprocess your dataset
        file_path = r'C:\Users\66930\Desktop\projact\coco2.csv'
        df = pd.read_csv(file_path)
        X = df[['date', 'size', 'weight']]
        y = df['price']

        # Create a Linear Regression model
        lrm = LinearRegression()
        lrm.fit(X, y)

        # Make a prediction with user inputs
        new_data = [[date, size, weight]]
        predicted_price = lrm.predict(new_data)

        # Display the result in the QTextBrowser
        self.textBrowser_2.setPlainText(f'ราคาที่ทำนาย: {predicted_price[0]:.2f}')
import coco_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CoconutPricePredictionUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
