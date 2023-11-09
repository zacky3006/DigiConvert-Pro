
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets


class us_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ทำนายราคาUSD")
        MainWindow.resize(736, 526)
        MainWindow.setMinimumSize(QtCore.QSize(736, 526))
        MainWindow.setMaximumSize(QtCore.QSize(736, 526))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 741, 501))
        self.textBrowser.setStyleSheet("background-image: url(:/newPrefix/480884275026329649.png);")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 120, 211, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 150, 211, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 180, 211, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(230, 120, 121, 31))
        self.textBrowser_2.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.168, y2:0.32, stop:0 rgba(221, 195, 93, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(230, 150, 121, 31))
        self.textBrowser_3.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.168, y2:0.32, stop:0 rgba(221, 195, 93, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(230, 180, 121, 31))
        self.textBrowser_4.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.168, y2:0.32, stop:0 rgba(221, 195, 93, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 210, 331, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(204, 204, 204);")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(350, 270, 211, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(230, 270, 121, 41))
        self.textBrowser_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 26))
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
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">CPI</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Nonfarm</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Dollar Index</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Process"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">ราคาที่ทำนาย =</span></p></body></html>"))
    def predict_price(self):
        # Read the CSV file
        file_path = r'C:\Users\66930\Desktop\projact\indexUsd.csv'
        df = pd.read_csv(file_path)

        # Create X and y variables
        X = df[['CPI', 'Nonfarm', 'DXY']]
        y = df['price']

        # Get user input
        cpi = float(self.lineEdit.text())
        nonf = int(self.lineEdit_2.text())
        dxy = float(self.lineEdit_3.text())

        # Create a Linear Regression model
        lrm = LinearRegression()
        lrm.fit(X, y)

        # Make predictions
        new_data = [[cpi, nonf, dxy]]
        predicted_price = lrm.predict(new_data)

        # Calculate Mean Absolute Error
        predictions = lrm.predict(X)
        mae = metrics.mean_absolute_error(y, predictions)

        # Display results in textBrowser_5
        predicted_price_dollars = "${:.2f}".format(predicted_price[0])
        mae_dollars = "{:.2f}".format(mae)
        result_text = f'Predicted Price: {predicted_price_dollars}\nMean Absolute Error: {mae_dollars}'
        self.textBrowser_5.setPlainText(result_text)
import usuid_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = us_ui()
    ui.setupUi(MainWindow)

    # Connect the predict_price function to the pushButton
    ui.pushButton.clicked.connect(ui.predict_price)

    MainWindow.show()
    sys.exit(app.exec_()) 



