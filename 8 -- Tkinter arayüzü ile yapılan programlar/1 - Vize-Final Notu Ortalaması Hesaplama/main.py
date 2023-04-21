
import tkinter as tk
from tkinter import messagebox

frame=tk.Tk()
frame.title("Vize-Final Notu Ortalaması Hesaplama")
frame.geometry("450x350")
frame.resizable(False,False)


L1=tk.Label(frame,text="Vize-Final Notu Ortalaması Hesaplama",fg="orange",font="Arial 15 italic")
L1.place(x=55,y=40)
L2=tk.Label(frame,text="Vize Notu : ",font="Calibri 15 italic")
L2.place(x=30,y=120)
L3=tk.Label(frame,text="Final Notu : ",font="Calibri 15 italic")
L3.place(x=30,y=155)

L2_entry=tk.Entry(frame,width=20)
L2_entry.place(x=160,y=125)
L3_entry=tk.Entry(frame,width=20)
L3_entry.place(x=160,y=160)

L4=tk.Label(frame,text="Ortalama : ",font="Calibri 15 italic")
L4.place(x=30,y=190)
L4_entry=tk.Entry(frame,width=20)
L4_entry.place(x=160,y=196)


def calculate():
    L4_entry.delete(0,"end")
    try:
        vize_notu=int(L2_entry.get())
        final_notu=int(L3_entry.get())
        average=float((vize_notu*40/100)+(final_notu*60/100))   # girilen vize ve final notuna göre ortalamayı hesaplatır.
        L4_entry.insert(0,average)

        if float(L4_entry.get())>=60 and int(L3_entry.get())>=50:  
            messagebox.showinfo(title="message",message="Tebrikler geçtiniz  :) ")
        elif float(L4_entry.get())<60 and float(L4_entry.get())>=50 and int(L3_entry.get())>=50:   
            messagebox.showinfo(title="message",message="Koşullu geçtiniz.")
        else:
            messagebox.showinfo(title="message",message="Maalesef geçemediniz  :( ")
    except ValueError:
        messagebox.showerror(title="error message",message="Lütfen sayısal karakter girin !!")

    L2_entry.delete(0,"end")
    L3_entry.delete(0,"end")


def cancel():     # pencereyi kapatır.
    frame.quit()


B1=tk.Button(frame,text="Calculate",bg="orange",width=17,font="Times 10 italic",command=calculate)
B1.place(x=70,y=250)
B2=tk.Button(frame,text="Cancel",bg="orange",width=17,font="Times 10 italic",command=cancel)
B2.place(x=230,y=250)

frame.mainloop()