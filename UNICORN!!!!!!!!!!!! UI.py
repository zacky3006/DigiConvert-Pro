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

# หัวข้อ ห ย้ า ย ห ย้ า ย -------------------------------------------------------------------------------------------------
main = tk.Label(window,text = 'ตัวแปลงหน่วย', bg= 'peach puff2')
main['font'] = font1
main.place(relx = '0.50',rely = '0.1', anchor = 'center',)

# เลือกสิ่งที่ต้องการแปลง -------------------------------------------------------------------------------------------------
metercon = tk.Button(window,text = 'แปลงหน่วยความยาว',bg= 'white', width=15)
metercon['font'] = font2
metercon.place(relx= '0.20',rely = '0.175')

weightcon = tk.Button(window,text = 'แปลงหน่วยน้ำหนัก',bg= 'white', width=15)
weightcon['font'] = font2
weightcon.place(relx= '0.55',rely = '0.175')

areacon = tk.Button(window,text = 'แปลงหน่วยพื้นที่',bg= 'white', width=15)
areacon['font'] = font2
areacon.place(relx= '0.20',rely = '0.24')

tempcon = tk.Button(window,text = 'แปลงหน่วยอุณหภูมิ',bg= 'white', width=15)
tempcon['font'] = font2
tempcon.place(relx= '0.55',rely = '0.24')

datacon = tk.Button(window,text = 'แปลงหน่วยข้อมูล',bg= 'white', width=15)
datacon['font'] = font2
datacon.place(relx= '0.367',rely = '0.305',)

# ช่องกรอกตัวเลข ---------------------------------------------------------------------------------------------------------
unit = tk.Label(window,text = 'กรอกตัวเลข :',bg = 'peach puff2')
main['font'] = font2
unit.place(relx = '0.10',rely = '0.40')
num_from = tk.Entry(window,width=38 ,textvariable= number_from)
num_from.place(relx= '0.338',rely= '0.405')

# ช่องหน่วยเริ่มต้น ---------------------------------------------------------------------------------------------------------
unit = tk.Label(window,text = 'หน่วยเริ่มต้น :',bg = 'peach puff2')
main['font'] = font2
unit.place(relx = '0.10',rely = '0.50')

n = StringVar()
unitdd = ttk.Combobox(window,width = '35',textvariable = n)

unitdd.place(relx = '0.57', rely = '0.52',anchor = 'center')
unitdd.current()

# ช่องหน่วยที่ต้องการแปลง -----------------------------------------------------------------------------------------------------
unit = tk.Label(window,text = 'หน่วยที่ต้องการแปลง :',bg = 'peach puff2')
main['font'] = font2
unit.place(relx = '0.10',rely = '0.60')

f = StringVar()
fromdd = ttk.Combobox(window,width = '35',textvariable= f)

fromdd.place(relx = '0.57',rely = '0.62',anchor= 'center')
fromdd.current()

# ช่องผลลัพธ์ --------------------------------------------------------------------------------------------------
unit = tk.Label(window,text = 'ผลลัพธ์ :',bg = 'peach puff2')
main['font'] = font2
unit.place(relx = '0.17',rely = '0.76')

result = tk.Label(window,text = '',bg= 'white',width = 28)
result['font'] = font2
result.place(relx = '0.34',rely = '0.76')

# ปุ่มคำนวณ ---------------------------------------------------------------------------------------------------
get_answer = tk.Button(window,text = 'คำนวณ',bg= 'white')
get_answer['font'] = font2
get_answer.place(relx= '0.46',rely = '0.67')

window.mainloop()
