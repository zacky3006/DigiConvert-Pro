import tkinter as tk
from tkinter.constants import UNITS
import tkinter.font as font
from functools import partial
from tkinter import StringVar,messagebox
from tkinter import ttk 

# ขนาดหน้าจอ---------------------------------------------------------------------------------------------------------------
window = tk.Tk()
window.geometry('500x500')
window.title('Unit Convert')
window.configure(bg= 'peach puff2')

number_from = StringVar()

font1 = font.Font(family = 'helvetica',size = '40')
font2 = font.Font(family = 'helvetica',size = '10')
font3 = font.Font(family = 'helvetica',size = '20')

def fromfunc(event):
    global result_from
    result_from = event.widget.get()

def tofunc(event):
    global result_to
    result_to = event.widget.get()

def answer(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('ไม่สามารถหาค่าได้',message='กรุณากรอกตัวเลข') 
    if result_from == 'มิลลิเมตร (mm)' and result_to == 'มิลลิเมตร (mm)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิเมตร (mm)' and result_to == 'เซนติเมตร (cm)':
        calculate = number1*0.1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิเมตร (mm)' and result_to == 'เมตร (m)':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิเมตร (mm)' and result_to == 'กิโลเมตร (km)':
        calculate = number1*0.000001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิเมตร (mm)' and result_to == 'นิ้ว (in)':
        calculate = "%.4f" %(number1*0.0393700787)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิเมตร (mm)' and result_to == 'ฟุต (ft)':
        calculate = "%.4f" %(number1*0.0032808399)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิเมตร (mm)' and result_to == 'หลา (yd)':
        calculate = "%.8f" %(number1*0.00010936132983377)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซนติเมตร (cm)' and result_to == 'มิลลิเมตร (mm)':
        calculate = number1*10
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซนติเมตร (cm)' and result_to == 'เซนติเมตร (cm)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซนติเมตร (cm)' and result_to == 'เมตร (m)':
        calculate = number1*0.01
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซนติเมตร (cm)' and result_to == 'กิโลเมตร (km)':
        calculate = number1*0.00001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซนติเมตร (cm)' and result_to == 'นิ้ว (in)':
        calculate = "%.4f" %(number1*0.3937007874)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซนติเมตร (cm)' and result_to == 'ฟุต (ft)':
        calculate = "%.4f" %(number1*0.032808399)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซนติเมตร (cm)' and result_to == 'หลา (yd)':
        calculate = "%.4f" %(number1*0.010936133)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เมตร (m)' and result_to == 'มิลลิเมตร (mm)':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เมตร (m)' and result_to == 'เซนติเมตร (cm)':
        calculate = number1*100
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เมตร (m)' and result_to == 'เมตร (m)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เมตร (m)' and result_to == 'กิโลเมตร (km)':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เมตร (m)' and result_to == 'นิ้ว (in)':
        calculate = "%.4f" %(number1*39.3700787402)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เมตร (m)' and result_to == 'ฟุต (ft)':
        calculate = "%.4f" %(number1*3.280839895)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เมตร (m)' and result_to == 'หลา (yd)':
        calculate = "%.4f" %(number1*1.0936132983)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลเมตร (km)' and result_to == 'มิลลิเมตร (mm)':
        calculate = number1*1000000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลเมตร (km)' and result_to == 'เซนติเมตร (cm)':
        calculate = number1*100000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลเมตร (km)' and result_to == 'เมตร (m)':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลเมตร (km)' and result_to == 'กิโลเมตร (km)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลเมตร (km)' and result_to == 'นิ้ว (in)':
        calculate = "%.4f" %(number1*39370.078740157)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลเมตร (km)' and result_to == 'ฟุต (ft)':
        calculate = "%.4f" %(number1*3280.8398950131)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลเมตร (km)' and result_to == 'หลา (yd)':
        calculate = "%.4f" %(number1*1093.6132983377)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'นิ้ว (in)' and result_to == 'มิลลิเมตร (mm)':
        calculate = "%.4f" %(number1*25.4)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'นิ้ว (in)' and result_to == 'เซนติเมตร (cm)':
        calculate = "%.4f" %(number1*2.54)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'นิ้ว (in)' and result_to == 'เมตร (m)':
        calculate = "%.4f" %(number1*0.0254)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'นิ้ว (in)' and result_to == 'กิโลเมตร (km)':
        calculate = "%.8f" %(number1*0.0000254)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'นิ้ว (in)' and result_to == 'นิ้ว (in)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'นิ้ว (in)' and result_to == 'ฟุต (ft)':
        calculate = "%.4f" %(number1*0.0833333333)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'นิ้ว (in)' and result_to == 'หลา (yd)':
        calculate = "%.4f" %(number1*0.0277777778)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟุต (ft)' and result_to == 'มิลลิเมตร (mm)':
        calculate = "%.4f" %(number1*304.8)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟุต (ft)' and result_to == 'เซนติเมตร (cm)':
        calculate = "%.4f" %(number1*30.48)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟุต (ft)' and result_to == 'เมตร (m)':
        calculate = "%.4f" %(number1*0.3048)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟุต (ft)' and result_to == 'กิโลเมตร (km)':
        calculate = "%.6f" %(number1*0.0003048)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟุต (ft)' and result_to == 'นิ้ว (in)':
        calculate = number1*12
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟุต (ft)' and result_to == 'ฟุต (ft)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟุต (ft)' and result_to == 'หลา (yd)':
        calculate = "%.4f" %(number1*0.3333333333)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'หลา (yd)' and result_to == 'มิลลิเมตร (mm)':
        calculate = "%.4f" %(number1*914.4)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'หลา (yd)' and result_to == 'เซนติเมตร (cm)':
        calculate = "%.4f" %(number1*91.44)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'หลา (yd)' and result_to == 'เมตร (m)':
        calculate = "%.4f" %(number1*0.9144)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'หลา (yd)' and result_to == 'กิโลเมตร (km)':
        calculate = "%.6f" %(number1*0.0009144)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'หลา (yd)' and result_to == 'นิ้ว (in)':
        calculate = number1*36
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'หลา (yd)' and result_to == 'ฟุต (ft)':
        calculate = number1*3
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'หลา (yd)' and result_to == 'หลา (yd)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิกรัม (mg)' and result_to == 'มิลลิกรัม (mg)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิกรัม (mg)' and result_to == 'กรัม (g)':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิกรัม (mg)' and result_to == 'กิโลกรัม (kg)':
        calculate = number1*(10**-6)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิกรัม (mg)' and result_to == 'ตัน (t)':
        calculate = number1*(10**-9)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิกรัม (mg)' and result_to == 'ออนซ์ (oz)':
        calculate = "%.8f" %(number1*(3.527399619*(10**-5)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'มิลลิกรัม (mg)' and result_to == 'ปอนด์ (lb)':
        calculate = "%.9f" %(number1*(2.20462262*(10**-6)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กรัม (g)' and result_to == 'มิลลิกรัม (mg)':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กรัม (g)' and result_to == 'กรัม (g)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กรัม (g)' and result_to == 'กิโลกรัม (kg)':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กรัม (g)' and result_to == 'ตัน (t)':
        calculate = number1*0.000001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กรัม (g)' and result_to == 'ออนซ์ (oz)':
        calculate = "%.5f" %(number1*0.0352739619)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กรัม (g)' and result_to == 'ปอนด์ (lb)':
        calculate = "%.6f" %(number1*0.0022046226)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลกรัม (kg)' and result_to == 'มิลลิกรัม (mg)':
        calculate = number1*1000000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลกรัม (kg)' and result_to == 'กรัม (g)':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลกรัม (kg)' and result_to == 'กิโลกรัม (kg)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลกรัม (kg)' and result_to == 'ตัน (t)':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลกรัม (kg)' and result_to == 'ออนซ์ (oz)':
        calculate = "%.4f" %(number1*35.2739619496)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'กิโลกรัม (kg)' and result_to == 'ปอนด์ (lb)':
        calculate = "%.4f" %(number1*2.2046226218)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตัน (t)' and result_to == 'มิลลิกรัม (mg)':
        calculate = number1*1000000000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตัน (t)' and result_to == 'กรัม (g)':
        calculate = number1*1000000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตัน (t)' and result_to == 'กิโลกรัม (kg)':
        calculate = "%.4f" %(number1*1000)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตัน (t)' and result_to == 'ตัน (t)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตัน (t)' and result_to == 'ออนซ์ (oz)':
        calculate = "%.4f" %(number1*35273.96194958)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตัน (t)' and result_to == 'ปอนด์ (lb)':
        calculate = "%.4f" %(number1*2204.6226218488)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ออนซ์ (oz)' and result_to == 'มิลลิกรัม (mg)':
        calculate = "%.4f" %(number1*28349.5231)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ออนซ์ (oz)' and result_to == 'กรัม (g)':
        calculate = "%.4f" %(number1*28.349523125)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ออนซ์ (oz)' and result_to == 'กิโลกรัม (kg)':
        calculate = "%.4f" %(number1*0.0283495231)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ออนซ์ (oz)' and result_to == 'ตัน (t)':
        calculate = "%.8f" %(number1*0.0000283495)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ออนซ์ (oz)' and result_to == 'ออนซ์ (oz)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ออนซ์ (oz)' and result_to == 'ปอนด์ (lb)':
        calculate = "%.4f" %(number1*0.625)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ปอนด์ (lb)' and result_to == 'มิลลิกรัม (mg)':
        calculate = "%.4f" %(number1*453592.37)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ปอนด์ (lb)' and result_to == 'กรัม (g)':
        calculate = "%.4f" %(number1*453.52937)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ปอนด์ (lb)' and result_to == 'กิโลกรัม (kg)':
        calculate = "%.4f" %(number1*0.45359237)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ปอนด์ (lb)' and result_to == 'ตัน (t)':
        calculate = "%.6f" %(number1*0.0004535924)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ปอนด์ (lb)' and result_to == 'ออนซ์ (oz)':
        calculate = "%.4f" %(number1*16)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ปอนด์ (lb)' and result_to == 'ปอนด์ (lb)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางมิลลิเมตร (mm2)' and result_to == 'ตารางมิลลิเมตร (mm2)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางมิลลิเมตร (mm2)' and result_to == 'ตารางเซนติเมตร (cm2)':
        calculate = "%.4f" %(number1*0.01)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางมิลลิเมตร (mm2)' and result_to == 'ตารางนิ้ว (in2)':
        calculate = "%.6f" %(number1*0.0015500031000062)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางมิลลิเมตร (mm2)' and result_to == 'ตารางฟุต (ft2)':
        calculate = "%.8f" %(number1*(1.076391041671*(10**-5)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางมิลลิเมตร (mm2)' and result_to == 'ตารางเดซิเมตร (dm2)':
        calculate = "%.6f" %(number1*(1*(10**-4)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางมิลลิเมตร (mm2)' and result_to == 'ตารางเมตร (m2)':
        calculate = "%.8f" %(number1*(1*(10**-6)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางมิลลิเมตร (mm2)' and result_to == 'ตารางกิโลเมตร (km2)':
        calculate = (number1*(1*(10**-12)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเซนติเมตร (cm2)' and result_to == 'ตารางมิลลิเมตร (mm2)':
        calculate = "%.4f" %(number1*100)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเซนติเมตร (cm2)' and result_to == 'ตารางเซนติเมตร (cm2)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเซนติเมตร (cm2)' and result_to == 'ตารางนิ้ว (in2)':
        calculate = "%.4f" %(number1*0.15500031000062)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเซนติเมตร (cm2)' and result_to == 'ตารางฟุต (ft2)':
        calculate = "%.5f" %(number1*0.001076391041671)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเซนติเมตร (cm2)' and result_to == 'ตารางเดซิเมตร (dm2)':
        calculate = "%.4f" %(number1*0.01)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเซนติเมตร (cm2)' and result_to == 'ตารางเมตร (m2)':
        calculate = "%.4f" %number1*0.0001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเซนติเมตร (cm2)' and result_to == 'ตารางกิโลเมตร (km2)':
        calculate = (number1*(1*(10**-10)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางนิ้ว (in2)' and result_to == 'ตารางมิลลิเมตร (mm2)':
        calculate = "%.4f" %(number1*645.16)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางนิ้ว (in2)' and result_to == 'ตารางเซนติเมตร (cm2)':
        calculate = "%.4f" %(number1*6.4516)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางนิ้ว (in2)' and result_to == 'ตารางนิ้ว (in2)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางนิ้ว (in2)' and result_to == 'ตารางฟุต (ft2)':
        calculate = "%.6f" %(number1*0.0069444444444444)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางนิ้ว (in2)' and result_to == 'ตารางเดซิเมตร (dm2)':
        calculate = "%.4f" %(number1*0.064516)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางนิ้ว (in2)' and result_to == 'ตารางเมตร (m2)':
        calculate = "%.5f" %(number1*0.00064516)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางนิ้ว (in2)' and result_to == 'ตารางกิโลเมตร (km2)':
        calculate = (number1*(6.4516*(10**-10)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางฟุต (ft2)' and result_to == 'ตารางมิลลิเมตร (mm2)':
        calculate = "%.4f" %(number1*(9.290304*(10**4)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางฟุต (ft2)' and result_to == 'ตารางเซนติเมตร (cm2)':
        calculate = "%.4f" %(number1*929.0304)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางฟุต (ft2)' and result_to == 'ตารางนิ้ว (in2)':
        calculate = "%.4f" %(number1*144)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางฟุต (ft2)' and result_to == 'ตารางฟุต (ft2)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางฟุต (ft2)' and result_to == 'ตารางเดซิเมตร (dm2)':
        calculate = "%.4f" %(number1*9.290304)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางฟุต (ft2)' and result_to == 'ตารางเมตร (m2)':
        calculate = "%.4f" %(number1*0.09290304)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางฟุต (ft2)' and result_to == 'ตารางกิโลเมตร (km2)':
        calculate = (number1*(9.290304*(10**-8)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเดซิเมตร (dm2)' and result_to == 'ตารางมิลลิเมตร (mm2)':
        calculate = "%.4f" %(number1*(1*(10**4)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเดซิเมตร (dm2)' and result_to == 'ตารางเซนติเมตร (cm2)':
        calculate = "%.4f" %(number1*100)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเดซิเมตร (dm2)' and result_to == 'ตารางนิ้ว (in2)':
        calculate = "%.4f" %(number1*15.500031000062)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเดซิเมตร (dm2)' and result_to == 'ตารางฟุต (ft2)':
        calculate = "%.4f" %(number1*0.1076391041671)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเดซิเมตร (dm2)' and result_to == 'ตารางเดซิเมตร (dm2)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเดซิเมตร (dm2)' and result_to == 'ตารางเมตร (m2)':
        calculate = "%.4f" %(number1*0.01)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเดซิเมตร (dm2)' and result_to == 'ตารางกิโลเมตร (km2)':
        calculate = (number1*(1*(10**-8)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเมตร (m2)' and result_to == 'ตารางมิลลิเมตร (mm2)':
        calculate = "%.4f" %(number1*(1*(10**6)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเมตร (m2)' and result_to == 'ตารางเซนติเมตร (cm2)':
        calculate = "%.4f" %(number1*(1*(10**4)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเมตร (m2)' and result_to == 'ตารางนิ้ว (in2)':
        calculate = "%.4f" %(number1*1550.0031000062)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเมตร (m2)' and result_to == 'ตารางฟุต (ft2)':
        calculate = "%.4f" %(number1*10.76391041671)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเมตร (m2)' and result_to == 'ตารางเดซิเมตร (dm2)':
        calculate = "%.4f" %(number1*100)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเมตร (m2)' and result_to == 'ตารางเมตร (m2)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางเมตร (m2)' and result_to == 'ตารางกิโลเมตร (km2)':
        calculate = (number1*(1*(10**-6)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางกิโลเมตร (km2)' and result_to == 'ตารางมิลลิเมตร (mm2)':
        calculate = "%.2f" %(number1*(1*(10**12)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางกิโลเมตร (km2)' and result_to == 'ตารางเซนติเมตร (cm2)':
        calculate = "%.2f" %(number1*(1*(10**10)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางกิโลเมตร (km2)' and result_to == 'ตารางนิ้ว (in2)':
        calculate = (number1*(1.550003*(10**9)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางกิโลเมตร (km2)' and result_to == 'ตารางฟุต (ft2)':
        calculate = "%.4f" %(number1*(1.076391*(10**7)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางกิโลเมตร (km2)' and result_to == 'ตารางเดซิเมตร (dm2)':
        calculate = "%.4f" %(number1*(1*(10**8)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางกิโลเมตร (km2)' and result_to == 'ตารางเมตร (m2)':
        calculate = "%.4f" %(number1*(1*(10**6)))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ตารางกิโลเมตร (km2)' and result_to == 'ตารางกิโลเมตร (km2)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซลเซียส (C)' and result_to == 'เซลเซียส (C)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซลเซียส (C)' and result_to == 'ฟาเรนไฮต์ (F)':
        calculate = "%.4f" %((9/5*(number1))+32)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เซลเซียส (C)' and result_to == 'เคลวิน(K)':
        calculate = "%.4f" %(number1+273.15)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟาเรนไฮต์ (F)' and result_to == 'เซลเซียส (C)':
        calculate = "%.4f" %((5/9)*(number1-32))
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟาเรนไฮต์ (F)' and result_to == 'ฟาเรนไฮต์ (F)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'ฟาเรนไฮต์ (F)' and result_to == 'เคลวิน(K)':
        calculate = "%.4f" %((number1+459.67)/1.8)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เคลวิน(K)' and result_to == 'เซลเซียส (C)':
        calculate = "%.4f" %(number1-273.15)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เคลวิน(K)' and result_to == 'ฟาเรนไฮต์ (F)':
        calculate = "%.4f" %((number1*9/5)-459.67)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'เคลวิน(K)' and result_to == 'เคลวิน(K)':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

# หัวข้อ ห ย้ า ย ห ย้ า ย -------------------------------------------------------------------------------------------------
main = tk.Label(window,text = 'ตัวแปลงหน่วย', bg= 'peach puff2')
main['font'] = font1
main.place(relx = '0.50',rely = '0.1', anchor = 'center',)

# เลือกสิ่งที่ต้องการแปลง -------------------------------------------------------------------------------------------------
def on_meter_button_click():
    distances = ['มิลลิเมตร (mm)','เซนติเมตร (cm)','เมตร (m)','กิโลเมตร (km)','นิ้ว (in)','ฟุต (ft)','หลา (yd)']
    unitdd["values"] = distances
    fromdd["values"] = distances
    unitdd.current(0)
    fromdd.current(0)
metercon = tk.Button(window,text = 'แปลงหน่วยความยาว',bg= 'white', width=15 , command=on_meter_button_click)
metercon['font'] = font2
metercon.place(relx= '0.20',rely = '0.175')

def on_weight_button_click():
    weight = ['มิลลิกรัม (mg)','กรัม (g)','กิโลกรัม (kg)','ตัน (t)','ออนซ์ (oz)','ปอนด์ (lb)']
    unitdd["values"] = weight
    fromdd["values"] = weight
    unitdd.current(0)
    fromdd.current(0)
weightcon = tk.Button(window,text = 'แปลงหน่วยน้ำหนัก',bg= 'white', width=15 , command=on_weight_button_click)
weightcon['font'] = font2
weightcon.place(relx= '0.55',rely = '0.175')

def on_area_button_click():
    area = ['ตารางมิลลิเมตร (mm2)','ตารางเซนติเมตร (cm2)','ตารางนิ้ว (in2)','ตารางฟุต (ft2)','ตารางเดซิเมตร (dm2)','ตารางเมตร (m2)','ตารางกิโลเมตร (km2)']
    unitdd["values"] = area
    fromdd["values"] = area
    unitdd.current(0)
    fromdd.current(0)
areacon = tk.Button(window,text = 'แปลงหน่วยพื้นที่',bg= 'white', width=15 , command=on_area_button_click)
areacon['font'] = font2
areacon.place(relx= '0.20',rely = '0.24')

def on_temp_button_click():
    temp = ['เซลเซียส (C)','ฟาเรนไฮต์ (F)','เคลวิน(K)']
    unitdd["values"] = temp
    fromdd["values"] = temp
    unitdd.current(0)
    fromdd.current(0)
tempcon = tk.Button(window,text = 'แปลงหน่วยอุณหภูมิ',bg= 'white', width=15 , command=on_temp_button_click)
tempcon['font'] = font2
tempcon.place(relx= '0.55',rely = '0.24')

# ช่องกรอกตัวเลข ---------------------------------------------------------------------------------------------------------
unit = tk.Label(window,text = 'กรอกตัวเลข :',bg = 'peach puff2')
main['font'] = font2
unit.place(relx = '0.10',rely = '0.40')

num_from = tk.Entry(window,width=38 ,textvariable= number_from)
num_from.place(relx= '0.338',rely= '0.405')

answer = partial(answer ,num_from)

# ช่องหน่วยเริ่มต้น ---------------------------------------------------------------------------------------------------------
unit = tk.Label(window,text = 'หน่วยเริ่มต้น :',bg = 'peach puff2')
main['font'] = font2
unit.place(relx = '0.10',rely = '0.50')

n = StringVar()
unitdd = ttk.Combobox(window,width = '35',textvariable = n)

unitdd.place(relx = '0.57', rely = '0.52',anchor = 'center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',fromfunc)

# ช่องหน่วยที่ต้องการแปลง -----------------------------------------------------------------------------------------------------
unit = tk.Label(window,text = 'หน่วยที่ต้องการแปลง :',bg = 'peach puff2')
main['font'] = font2
unit.place(relx = '0.10',rely = '0.60')

f = StringVar()
fromdd = ttk.Combobox(window,width = '35',textvariable= f)

fromdd.place(relx = '0.57',rely = '0.62',anchor= 'center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',tofunc)

# ช่องผลลัพธ์ --------------------------------------------------------------------------------------------------
unit = tk.Label(window,text = 'ผลลัพธ์ :',bg = 'peach puff2')
main['font'] = font2
unit.place(relx = '0.17',rely = '0.76')

result = tk.Label(window,text = '',bg= 'white',width = 28)
result['font'] = font2
result.place(relx = '0.34',rely = '0.76')

# ปุ่มคำนวณ ---------------------------------------------------------------------------------------------------
get_answer = tk.Button(window,text = 'คำนวณ',bg= 'white' ,command=answer)
get_answer['font'] = font2
get_answer.place(relx= '0.46',rely = '0.67')

window.mainloop()
