import tkinter as tk
import time


frame=tk.Tk()                      
frame.title("clock app")
frame.geometry("300x250")
frame.config(bg="light blue")
frame.resizable(0,0)


L1=tk.Label(frame,text="Clock App",fg="blue",bg="light blue",font="Arial 20 italic")    
L1.place(x=80,y=20)


def clock():
    string=time.strftime("%H:%M:%S")    # string'e bilgisayarımızın şuan ki saat bilgisini atıyoruz.
    label.config(text=string)           # label'in içine stringi yaz.
    label.after(200,clock)              # hangi aralıklarla saati güncelleriz onu belirtiyoruz.


label=tk.Label(font="Times 35 bold")    # saatimizin ayarlarını yapacağımız label.
label.place(x=50,y=100)
clock()


frame.mainloop()