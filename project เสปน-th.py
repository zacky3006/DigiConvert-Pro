from tkinter import *
from tkinter import font
from cgitb import text
from googletrans import Translator

#ขนาดหน้าจอ
root = Tk()
root.title("Google Translate (EN-TH)")
root.geometry('530x300')
root.maxsize(500,300)
root.minsize(530,300)
root.configure(bg="cyan")


#widget
label=Label(text="Spanish - Thai",font=('Arial',25,'bold'))
label.place(x=120,y=20)
#get massang korean
text1=Text(root,width=30,height=7,font=20)
text1.place(x=10,y=70)
#get thai
text2=Text(root,width=30,height=7,font=20)
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
translateBtn=Button(root,text="แปลภาษา",command=translate,bg="blue",font=30)
translateBtn.place(x=160,y=250)

clearBtn= Button(root,text="เคลียร์",command=reset,bg="red",font=30)
clearBtn.place(x=260,y=250)

root.mainloop()