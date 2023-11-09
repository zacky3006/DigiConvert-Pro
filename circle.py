import tkinter
import tkinter as tk
import math

def circle():
    radiance = float(entry_amount.get()) #รับข้อมูลจากช่องป้อนข้อมูล

    #หาพื้นที่และเส้นรอบวง
    area = (math.pi*(radiance**2))
    circumference = 2*math.pi*radiance

    result_label.config(text=f"พื้นที่ของวงกลมคือ {area:.2f}")
    result_label2.config(text=f"เส้นรอบวงคือ {circumference:.2f}")

#Window
root = tkinter.Tk()
root.title("คำนวณวงกลม")
root.geometry('300x200')
root.configure(bg= '#0000ff')

#widget ต่าง ๆ

label_radiance = tkinter.Label(root, text="คำนวณค่าวงกลม")
label_radiance.pack()

#ช่องใส่รัศมี
label_amount = tkinter.Label(root, text="radiance:")
label_amount.pack()

entry_amount = tkinter.Entry(root)
entry_amount.pack()

#ปุ่มConvert
convert_button = tkinter.Button(root, text="Convert", command=circle)
convert_button.pack()

#ช่องแสดงค่าพื้นที่และเส้นรอบวง
result_label = tk.Label(root, text="")
result_label.pack()

result_label2 = tk.Label(root, text="")
result_label2.pack()

root.mainloop()
