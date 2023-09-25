import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates


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
root = tk.Tk()
root.title("แปลงสกุลเงิน")

#widget ต่าง ๆ

#เลือกสกุลเงินที่ต้องการแปลง
label_from_currency = tk.Label(root, text="From Currency:")
label_from_currency.pack()

combo_from_currency = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY"])
combo_from_currency.set('USD') #สกุลเงินเริ่มต้น
combo_from_currency.pack()

#ใส่จำนวนเงินที่ต้องการแปลง
label_amount = tk.Label(root, text="Amount:")
label_amount.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

#เลือกสกุลเงินที่ต้องการจะรู้   
label_to_currency = tk.Label(root, text="To Currency:")
label_to_currency.pack()

combo_to_currency = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY"])
combo_to_currency.set('EUR') #สกุลเงินเริ่มต้น
combo_to_currency.pack()

#ปุ่ม"Convert"
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack()

#แสดงผลเงินตามอัตราแลกเปลี่ยนจริงที่ได้ออกมา
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
