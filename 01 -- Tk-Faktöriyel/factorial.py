
# Tkinter kullanılarak basit bir arayüz ile faktöriyel hesaplama

import tkinter as tk
from tkinter import messagebox

frame=tk.Tk()
frame.title("factorial calculation")
frame.geometry("350x350")
frame.resizable(False,False)


def factorial():                                
    result.delete(0,"end")
    if int(number.get())==0:           
        result.insert(0,1)
    elif int(number.get())<0:               
        messagebox.showinfo(title="message 1",message="The number entered is negative.")
    else:                              
        fact=1
        for num in range(1,int(number.get())+1):
            fact=fact*num
        result.insert(0,fact)
    number.delete(0,"end")


label=tk.Label(frame,text="Factorial Calculation",fg="green",font="consoles 14 bold")
label.place(x=90,y=30)
lbl_number=tk.Label(frame,text="Enter a number :",font="8")
lbl_number.place(x=20,y=110)
lbl_result=tk.Label(frame,text="Result :",font="8")
lbl_result.place(x=20,y=140)

number=tk.Entry(frame,width=25)
number.place(x=150,y=112)
result=tk.Entry(frame,width=25)
result.place(x=150,y=142)

button=tk.Button(frame,text="Calculate",bg="green",width=15,font="15",command=factorial)
button.place(x=150,y=200)


frame.mainloop()
