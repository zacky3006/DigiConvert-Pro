from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QTextEdit, QPushButton
from googletrans import Translator
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import font
from cgitb import text
from googletrans import Translator
import pyqrcode
import png
from PIL import ImageTk,Image
from forex_python.converter import CurrencyRates
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from sklearn.linear_model import LinearRegression
import coco_rc 
from PyQt5.QtWidgets import QMainWindow, QApplication
import tkinter
import tkinter as tk
import math
from forex_python.converter import CurrencyRates

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 663)
        MainWindow.setMinimumSize(QtCore.QSize(841, 663))
        MainWindow.setMaximumSize(QtCore.QSize(841, 663))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\66930\\Desktop\\new00\\../projact/istockphoto-871024878-612x612.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 161, 61))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 24pt \"Snap ITC\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(430, 90, 391, 300))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.362, y2:1, stop:0.139303 rgba(0, 255, 255, 255), stop:0.701493 rgba(123, 255, 21, 255));\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setStyleSheet("\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"\n"
"background-color:qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.362, y2:1, stop:0.139303 rgba(0, 255, 255, 255), stop:0.701493 rgba(123, 255, 21, 255));")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.362, y2:1, stop:0.139303 rgba(0, 255, 255, 255), stop:0.701493 rgba(123, 255, 21, 255));\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.362, y2:1, stop:0.139303 rgba(0, 255, 255, 255), stop:0.701493 rgba(123, 255, 21, 255));\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.362, y2:1, stop:0.139303 rgba(0, 255, 255, 255), stop:0.701493 rgba(123, 255, 21, 255));\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";\n"
";background-color:qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.362, y2:1, stop:0.139303 rgba(0, 255, 255, 255), stop:0.701493 rgba(123, 255, 21, 255));")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_11.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";\n"
";background-color:qlineargradient(spread:repeat, x1:0.1, y1:0.25, x2:0.362, y2:1, stop:0.139303 rgba(0, 255, 255, 255), stop:0.701493 rgba(123, 255, 21, 255));")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 90, 361, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0.199826, y1:0.216, x2:0, y2:0.752, stop:0.0447761 rgba(0, 255, 0, 255), stop:0.492537 rgba(0, 255, 255, 255));\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0.199826, y1:0.216, x2:0, y2:0.752, stop:0.0447761 rgba(0, 255, 0, 255), stop:0.492537 rgba(0, 255, 255, 255));\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0.199826, y1:0.216, x2:0, y2:0.752, stop:0.0447761 rgba(0, 255, 0, 255), stop:0.492537 rgba(0, 255, 255, 255));\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";\n"
";background-color:qlineargradient(spread:repeat, x1:0.199826, y1:0.216, x2:0, y2:0.752, stop:0.0447761 rgba(0, 255, 0, 255), stop:0.492537 rgba(0, 255, 255, 255));")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";\n"
";background-color:qlineargradient(spread:repeat, x1:0.199826, y1:0.216, x2:0, y2:0.752, stop:0.0447761 rgba(0, 255, 0, 255), stop:0.492537 rgba(0, 255, 255, 255));")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";\n"
";background-color:qlineargradient(spread:repeat, x1:0.199826, y1:0.216, x2:0, y2:0.752, stop:0.0447761 rgba(0, 255, 0, 255), stop:0.492537 rgba(0, 255, 255, 255));")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, -19, 911, 661))
        self.textBrowser.setStyleSheet("\n"
"background-image: url(:/g/Screenshot 2023-11-09 033042.png);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, -10, 841, 631))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_4.clicked.connect(self.google_translate_en_th)
        self.pushButton_5.clicked.connect(self.google_translate_jp_th)
        self.pushButton_9.clicked.connect(self.google_translate_kr_th)
        self.pushButton_3.clicked.connect(self.google_translate_ch_th)
        self.pushButton.clicked.connect(self.google_translate_ge_th)
        self.pushButton_10.clicked.connect(self.google_translate_es_th)
        self.pushButton_11.clicked.connect(self.google_translate_ru_th)
        self.pushButton_7.clicked.connect(self.cal)
        self.pushButton_6.clicked.connect(self.mainc)
        self.pushButton_2.clicked.connect(self.moneyc)


    def google_translate_en_th(self):  # Make it an instance method
        self.gol = Tk()
        self.gol.title("Google Translate (EN-TH)")
        self.gol.geometry('530x300')
        self.gol.maxsize(500,300)
        self.gol.minsize(530,300)
        self.gol.configure(bg="cyan")
        label=Label(self.gol,text="English - Thai",font=('Arial',25,'bold'))
        label.place(x=120,y=20)
        #get massang eng
        text1=Text(self.gol,width=30,height=7,font=20)
        text1.place(x=10,y=70)
        #get thai
        text2=Text(self.gol,width=30,height=7,font=20)
        text2.place(x=260,y=70)

        def translate():
                message=text1.get('1.0','end-1c') #ดึงข้อความเก็บในตัวแปร -1c ชาเลจเจอลบช่องว่างติดมาหลังคำ
                translator=Translator()
                output=translator.translate(text=message,src='en',dest='th')  #ระบุข้อความดำเนินการ src ระบบว่าแปลงต้นทางเป็น destระบุไทย
                text2.insert('end',output.text)
        def reset():   
                text1.delete(1.0,'end')
                text2.delete(1.0,'end')
        #ปุ่ม
        translateBtn=Button(self.gol,text="แปลภาษา",command=translate,bg="blue",font=30)
        translateBtn.place(x=160,y=250)

        clearBtn= Button(self.gol,text="เคลียร์",command=reset,bg="red",font=30)
        clearBtn.place(x=260,y=250)

        self.gol.mainloop()
    def google_translate_jp_th(self):  # Make it an instance method
        self.gol = Tk()
        self.gol.title("Google Translate (JP-TH)")
        self.gol.geometry('530x300')
        self.gol.maxsize(500,300)
        self.gol.minsize(530,300)
        self.gol.configure(bg="cyan")
        label=Label(self.gol,text="Japan - Thai",font=('Arial',25,'bold'))
        label.place(x=120,y=20)
        #get massang eng
        text1=Text(self.gol,width=30,height=7,font=20)
        text1.place(x=10,y=70)
        #get thai
        text2=Text(self.gol,width=30,height=7,font=20)
        text2.place(x=260,y=70)

        def translate():
                message=text1.get('1.0','end-1c') #ดึงข้อความเก็บในตัวแปร -1c ชาเลจเจอลบช่องว่างติดมาหลังคำ
                translator=Translator()
                output=translator.translate(text=message,src='ja',dest='th')  #ระบุข้อความดำเนินการ src ระบบว่าแปลงต้นทางเป็น destระบุไทย
                text2.insert('end',output.text)
        def reset():   
                text1.delete(1.0,'end')
                text2.delete(1.0,'end')
        #ปุ่ม
        translateBtn=Button(self.gol,text="แปลภาษา",command=translate,bg="blue",font=30)
        translateBtn.place(x=160,y=250)

        clearBtn= Button(self.gol,text="เคลียร์",command=reset,bg="red",font=30)
        clearBtn.place(x=260,y=250)

        self.gol.mainloop()
    def google_translate_kr_th(self):  # Make it an instance method
        self.gol = Tk()
        self.gol.title("Google Translate (KR-TH)")
        self.gol.geometry('530x300')
        self.gol.maxsize(500,300)
        self.gol.minsize(530,300)
        self.gol.configure(bg="cyan")
        label=Label(self.gol,text="Korea - Thai",font=('Arial',25,'bold'))
        label.place(x=120,y=20)
        #get massang eng
        text1=Text(self.gol,width=30,height=7,font=20)
        text1.place(x=10,y=70)
        #get thai
        text2=Text(self.gol,width=30,height=7,font=20)
        text2.place(x=260,y=70)

        def translate():
                message=text1.get('1.0','end-1c') #ดึงข้อความเก็บในตัวแปร -1c ชาเลจเจอลบช่องว่างติดมาหลังคำ
                translator=Translator()
                output=translator.translate(text=message,src='ko',dest='th')  #ระบุข้อความดำเนินการ src ระบบว่าแปลงต้นทางเป็น destระบุไทย
                text2.insert('end',output.text)
        def reset():   
                text1.delete(1.0,'end')
                text2.delete(1.0,'end')
        #ปุ่ม
        translateBtn=Button(self.gol,text="แปลภาษา",command=translate,bg="blue",font=30)
        translateBtn.place(x=160,y=250)

        clearBtn= Button(self.gol,text="เคลียร์",command=reset,bg="red",font=30)
        clearBtn.place(x=260,y=250)

        self.gol.mainloop()
    def google_translate_ch_th(self):  # Make it an instance method
        self.gol = Tk()
        self.gol.title("Google Translate (CH-TH)")
        self.gol.geometry('530x300')
        self.gol.maxsize(500,300)
        self.gol.minsize(530,300)
        self.gol.configure(bg="cyan")
        label=Label(self.gol,text="Chaina - Thai",font=('Arial',25,'bold'))
        label.place(x=120,y=20)
        #get massang eng
        text1=Text(self.gol,width=30,height=7,font=20)
        text1.place(x=10,y=70)
        #get thai
        text2=Text(self.gol,width=30,height=7,font=20)
        text2.place(x=260,y=70)

        def translate():
                message=text1.get('1.0','end-1c') #ดึงข้อความเก็บในตัวแปร -1c ชาเลจเจอลบช่องว่างติดมาหลังคำ
                translator=Translator()
                output=translator.translate(text=message,src='zh-CN',dest='th')  #ระบุข้อความดำเนินการ src ระบบว่าแปลงต้นทางเป็น destระบุไทย
                text2.insert('end',output.text)
        def reset():   
                text1.delete(1.0,'end')
                text2.delete(1.0,'end')
        #ปุ่ม
        translateBtn=Button(self.gol,text="แปลภาษา",command=translate,bg="blue",font=30)
        translateBtn.place(x=160,y=250)

        clearBtn= Button(self.gol,text="เคลียร์",command=reset,bg="red",font=30)
        clearBtn.place(x=260,y=250)

        self.gol.mainloop()
    def google_translate_ge_th(self):  # Make it an instance method
        self.gol = Tk()
        self.gol.title("Google Translate (GE-TH)")
        self.gol.geometry('530x300')
        self.gol.maxsize(500,300)
        self.gol.minsize(530,300)
        self.gol.configure(bg="cyan")
        label=Label(self.gol,text="German - Thai",font=('Arial',25,'bold'))
        label.place(x=120,y=20)
        #get massang eng
        text1=Text(self.gol,width=30,height=7,font=20)
        text1.place(x=10,y=70)
        #get thai
        text2=Text(self.gol,width=30,height=7,font=20)
        text2.place(x=260,y=70)

        def translate():
                message=text1.get('1.0','end-1c') #ดึงข้อความเก็บในตัวแปร -1c ชาเลจเจอลบช่องว่างติดมาหลังคำ
                translator=Translator()
                output=translator.translate(text=message,src='de',dest='th')  #ระบุข้อความดำเนินการ src ระบบว่าแปลงต้นทางเป็น destระบุไทย
                text2.insert('end',output.text)
        def reset():   
                text1.delete(1.0,'end')
                text2.delete(1.0,'end')
        #ปุ่ม
        translateBtn=Button(self.gol,text="แปลภาษา",command=translate,bg="blue",font=30)
        translateBtn.place(x=160,y=250)

        clearBtn= Button(self.gol,text="เคลียร์",command=reset,bg="red",font=30)
        clearBtn.place(x=260,y=250)

        self.gol.mainloop()
    def cal(self):
        self.cal=Tk()
        self.cal.title("เครื่องคิดเลข ByKO")
        content=""
        txt_input = StringVar(self.cal,value="0",) #ผูกกับdisplay

        #7=+10 getin content  =set txtinput  command=lambda:btn7 ส่งเลข / "+/-/x"
        def btn(number):
                nonlocal content
                content = content+str(number)
                txt_input.set(content)
        def equal(): #ส่งมาแบบอิสระแปลงคำนวนได้เลย /7+10=
                nonlocal content
                try:
                        calculate = float(eval(content))
                        txt_input.set(calculate)
                        content = ""
                except Exception as e:
                        txt_input.set("Error")
        def claer():
                nonlocal content            #claer content
                content=""               #set ว่าง
                txt_input.set("")            #set ....
                display.insert(0,"0")    #display ใส่0 เริ่มต้น

        #output แสดงผล 5x4 justify="right" เลข0ขวา
        display = Entry(self.cal,font=('arial',33,'bold'),fg="white",bg="green",textvariable=txt_input,justify="right") #ชื่อฟ้อนarial 30 ตัวหนาbold
        display.grid(columnspan=4)                 #columnspan=4 4ช่อง






        #input รับค่าผ่านปุ่ม


        #row1    padx ขยายพื้นที่ด้านในแนวนอน    pady แนวตั้ง
        btn7=Button(self.cal,fg="black",font=('arial',30,'bold'),text="7",command=lambda:btn(7),padx=44,pady=10,bg="grey").grid(row=1,column=0)
        btn8=Button(self.cal,fg="black",font=('arial',30,'bold'),text="8",command=lambda:btn(8),padx=46,pady=10,bg="grey").grid(row=1,column=1)
        btn9=Button(self.cal,fg="black",font=('arial',30,'bold'),text="9",command=lambda:btn(9),padx=41,pady=10,bg="grey").grid(row=1,column=2)
        btnc=Button(self.cal,fg="black",font=('arial',30,'bold'),text="c",command=claer,padx=46,pady=10,bg="orange").grid(row=1,column=3)
        #row2 
        btn4=Button(self.cal,fg="black",font=('arial',30,'bold'),text="4",command=lambda:btn(4),padx=44,pady=10,bg="grey").grid(row=2,column=0)
        btn5=Button(self.cal,fg="black",font=('arial',30,'bold'),text="5",command=lambda:btn(5),padx=46,pady=10,bg="grey").grid(row=2,column=1)
        btn6=Button(self.cal,fg="black",font=('arial',30,'bold'),text="6",command=lambda:btn(6),padx=41,pady=10,bg="grey").grid(row=2,column=2)
        btnd=Button(self.cal,fg="black",font=('arial',30,'bold'),text="-",command=lambda:btn("-"),padx=50,pady=10,bg="orange").grid(row=2,column=3)
        #row3
        btn1=Button(self.cal,fg="black",font=('arial',30,'bold'),text="1",command=lambda:btn(1),padx=44,pady=10,bg="grey").grid(row=3,column=0)
        btn2=Button(self.cal,fg="black",font=('arial',30,'bold'),text="2",command=lambda:btn(2),padx=46,pady=10,bg="grey").grid(row=3,column=1)
        btn3=Button(self.cal,fg="black",font=('arial',30,'bold'),text="3",command=lambda:btn(3),padx=41,pady=10,bg="grey").grid(row=3,column=2)
        btnplus=Button(self.cal,fg="black",font=('arial',30,'bold'),text="+",command=lambda:btn("+"),padx=45,pady=10,bg="orange").grid(row=3,column=3)
        #row4
        btndot=Button(self.cal,fg="black",font=('arial',30,'bold'),text=".",command=lambda:btn("."),padx=50,pady=10,bg="orange").grid(row=4,column=0)
        btn0=Button(self.cal,fg="black",font=('arial',30,'bold'),text="0",command=lambda:btn(0),padx=46,pady=10,bg="grey").grid(row=4,column=1)
        btndivision=Button(self.cal,fg="black",font=('arial',30,'bold'),text="/",command=lambda:btn("/"),padx=46,pady=10,bg="orange").grid(row=4,column=2)
        btndmultiply=Button(self.cal,fg="black",font=('arial',30,'bold'),text="x",command=lambda:btn("*"),padx=46,pady=10,bg="orange").grid(row=4,column=3)

        #row5 
        btnope=Button(self.cal,fg="black",font=('arial',30,'bold'),text="(",command=lambda:btn("("),padx=50,pady=10,bg="orange").grid(row=5,column=0)
        btnclose=Button(self.cal,fg="black",font=('arial',30,'bold'),text=")",command=lambda:btn(")"),padx=53,pady=10,bg="orange").grid(row=5,column=1)
        btnequal=Button(self.cal,fg="black",font=('arial',30,'bold'),text="=",command=equal,padx=120,pady=10,bg="blue").grid(row=5,column=2,columnspan=2)

        self.cal.mainloop()
    def google_translate_es_th(self):  # Make it an instance method
        self.gol = Tk()
        self.gol.title("Google Translate (ES-TH)")
        self.gol.geometry('530x300')
        self.gol.maxsize(500,300)
        self.gol.minsize(530,300)
        self.gol.configure(bg="cyan")
        label=Label(self.gol,text="Spanish - Thai",font=('Arial',25,'bold'))
        label.place(x=120,y=20)
        #get massang eng
        text1=Text(self.gol,width=30,height=7,font=20)
        text1.place(x=10,y=70)
        #get thai
        text2=Text(self.gol,width=30,height=7,font=20)
        text2.place(x=260,y=70)

        def translate():
                message=text1.get('1.0','end-1c') #ดึงข้อความเก็บในตัวแปร -1c ชาเลจเจอลบช่องว่างติดมาหลังคำ
                translator=Translator()
                output=translator.translate(text=message,src='es',dest='th')  #ระบุข้อความดำเนินการ src ระบบว่าแปลงต้นทางเป็น destระบุไทย
                text2.insert('end',output.text)
        def reset():   
                text1.delete(1.0,'end')
                text2.delete(1.0,'end')
        #ปุ่ม
        translateBtn=Button(self.gol,text="แปลภาษา",command=translate,bg="blue",font=30)
        translateBtn.place(x=160,y=250)

        clearBtn= Button(self.gol,text="เคลียร์",command=reset,bg="red",font=30)
        clearBtn.place(x=260,y=250)

        self.gol.mainloop()
    def google_translate_ru_th(self):  # Make it an instance method
        self.gol = Tk()
        self.gol.title("Google Translate (RU-TH)")
        self.gol.geometry('530x300')
        self.gol.maxsize(500,300)
        self.gol.minsize(530,300)
        self.gol.configure(bg="cyan")
        label=Label(self.gol,text="Russia - Thai",font=('Arial',25,'bold'))
        label.place(x=120,y=20)
        #get massang eng
        text1=Text(self.gol,width=30,height=7,font=20)
        text1.place(x=10,y=70)
        #get thai
        text2=Text(self.gol,width=30,height=7,font=20)
        text2.place(x=260,y=70)

        def translate():
                message=text1.get('1.0','end-1c') #ดึงข้อความเก็บในตัวแปร -1c ชาเลจเจอลบช่องว่างติดมาหลังคำ
                translator=Translator()
                output=translator.translate(text=message,src='ru',dest='th')  #ระบุข้อความดำเนินการ src ระบบว่าแปลงต้นทางเป็น destระบุไทย
                text2.insert('end',output.text)
        def reset():   
                text1.delete(1.0,'end')
                text2.delete(1.0,'end')
        #ปุ่ม
        translateBtn=Button(self.gol,text="แปลภาษา",command=translate,bg="blue",font=30)
        translateBtn.place(x=160,y=250)

        clearBtn= Button(self.gol,text="เคลียร์",command=reset,bg="red",font=30)
        clearBtn.place(x=260,y=250)

        self.gol.mainloop()
    def mainc(self):
        def calculate_circle():
                radiance = float(entry_radiance.get())

                area = math.pi * (radiance**2)
                circumference = 2 * math.pi * radiance

                result_label.config(text=f"พื้นที่ของวงกลมคือ {area:.2f}")
                result_label2.config(text=f"เส้นรอบวงคือ {circumference:.2f}")

        self.root = tkinter.Tk()
        self.root.title("คำนวณวงกลม")
        self.root.geometry('300x200')
        self.root.configure(bg='#0000ff')

        label_radiance = tkinter.Label(self.root, text="คำนวณค่าวงกลม")
        label_radiance.pack()

        label_radiance = tkinter.Label(self.root, text="รัศมี:")
        label_radiance.pack()

        entry_radiance = tkinter.Entry(self.root)
        entry_radiance.pack()

        convert_button = tkinter.Button(self.root, text="คำนวณ", command=calculate_circle)
        convert_button.pack()

        result_label = tkinter.Label(self.root, text="")
        result_label.pack()

        result_label2 = tkinter.Label(self.root, text="")
        result_label2.pack()

        self.root.mainloop()
    def moneyc(self):
        def convert_currency():
                #รับข้อมูลจากช่องป้อนข้อมูล
                amount = float(entry_amount.get())
                from_currency = combo_from_currency.get()
                to_currency = combo_to_currency.get()

                #แปลงสกุลเงินตามอัตราแลกเปลี่ยนจริง
                c = CurrencyRates()
                converted_amount = c.convert(from_currency, to_currency, amount)
    
                result_label.config(text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')#เงินตามอัตราแลกเปลี่ยนจริงที่ได้ออกมา

        #ชื่อหน้าต่าง
        self.root = tk.Tk()
        self.root.title("แปลงสกุลเงิน")

        #widget ต่าง ๆ

        #เลือกสกุลเงินที่ต้องการแปลง
        label_from_currency = tk.Label(self.root, text="From Currency:")
        label_from_currency.pack()

        combo_from_currency = ttk.Combobox(self.root, values=[
        "USD", "EUR", "GBP", "JPY", "THB", "AUD", "CAD", "SGD", "CHF", "NZD",
        "HKD", "SEK", "NOK", "DKK", "KRW", "CNY", "INR", "BRL", "ZAR", "SAR"])
        combo_from_currency.set('USD') #สกุลเงินเริ่มต้น
        combo_from_currency.pack()

        #ใส่จำนวนเงินที่ต้องการแปลง
        label_amount = tk.Label(self.root, text="Amount:")
        label_amount.pack()

        entry_amount = tk.Entry(self.root)
        entry_amount.pack()

        #เลือกสกุลเงินที่ต้องการจะรู้   
        label_to_currency = tk.Label(self.root, text="To Currency:")
        label_to_currency.pack()

        combo_to_currency = ttk.Combobox(self.root, values=[
        "USD", "EUR", "GBP", "JPY", "THB", "AUD", "CAD", "SGD", "CHF", "NZD",
        "HKD", "SEK", "NOK", "DKK", "KRW", "CNY", "INR", "BRL", "ZAR", "SAR"])
        combo_to_currency.set('EUR') #สกุลเงินเริ่มต้น
        combo_to_currency.pack()

        #ปุ่ม"Convert"
        convert_button = tk.Button(self.root, text="Convert", command=convert_currency)
        convert_button.pack()

        #แสดงผลเงินตามอัตราแลกเปลี่ยนจริงที่ได้ออกมา
        result_label = tk.Label(self.root, text="")
        result_label.pack()

        self.root.mainloop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DigiConvert-Pro"))
        self.label.setText(_translate("MainWindow", "MENU"))
        self.pushButton_4.setText(_translate("MainWindow", "Google Translate (EN-TH)"))
        self.pushButton_5.setText(_translate("MainWindow", "Google Translate (JP-TH)"))
        self.pushButton_9.setText(_translate("MainWindow", "Google Translate (KR-TH)"))
        self.pushButton_3.setText(_translate("MainWindow", "Google Translate (CH-TH)"))
        self.pushButton.setText(_translate("MainWindow", "Google Translate (GE-TH)"))
        self.pushButton_10.setText(_translate("MainWindow", "Google Translate (ES-TH)"))
        self.pushButton_11.setText(_translate("MainWindow", "Google Translate (RU-TH)"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>โปรแกรมคำนวณพื้นที่วงกลม</p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Calculate area of circle"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>โปรแกรมแปลงสกุลเงิน</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "currency converter"))
        self.pushButton_7.setText(_translate("MainWindow", "Calculator"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>ทำนายราคามะพร้าว</p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "Coconut price prediction"))
        self.pushButton_12.setToolTip(_translate("MainWindow", "<html><head/><body><p>ทำนายราคาUSD</p></body></html>"))
        self.pushButton_12.setText(_translate("MainWindow", "Predict the dollar price"))
        self.pushButton_13.setText(_translate("MainWindow", "Unit Convert"))
    


import kk_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
