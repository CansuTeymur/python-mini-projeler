

"""
Pizza sipariş programı.
İşlem yapabilmek için  "password=software" olmalı.
"""


import tkinter as tk
from tkinter import messagebox

frame1=tk.Tk()                              # pencere oluşturulur.
frame1.title("pizza ordering program")
frame1.geometry("500x400+400+100")
frame1.resizable(False,False)


lbl_title=tk.Label(frame1,text="Welcome to Pizza Order Program",bg="pink",font="Times 17 italic")
lbl_title.pack()

mail=tk.Label(frame1,text="Mail : ",fg="blue",font="15")
mail.place(x=20,y=60)
password=tk.Label(frame1,text="Password : ",fg="blue",font="15")
password.place(x=20,y=90)

mail_entry=tk.Entry(frame1)
mail_entry.place(x=124,y=63)
password_entry=tk.Entry(frame1,show="*")         # show="*" ile girilen şifre ***** olarak gösterilir.
password_entry.place(x=124,y=95)



def register():       # kayıt olma kısmı.

    L1=tk.Label(frame1,text="Name : ",fg="blue",font="15")
    L1.place(x=24,y=190)
    L2=tk.Label(frame1,text="Password : ",fg="blue",font="15")
    L2.place(x=24,y=220)
    L3=tk.Label(frame1,text="Mail : ",fg="blue",font="15")
    L3.place(x=24,y=250)
    L1_entry=tk.Entry(frame1)
    L1_entry.place(x=124,y=190)
    L2_entry=tk.Entry(frame1,show="*")
    L2_entry.place(x=124,y=220)
    L3_entry=tk.Entry(frame1)
    L3_entry.place(x=124,y=250)

    def registration_is_over():
        password=L2_entry.get()
        if password=="software":      # password=="software" ise kayıt tamamlanır.
            messagebox.showinfo(title="Info",message="Registration Completed")
            L2_entry.delete(0,"end")
            L1_entry.delete(0,"end")
            L3_entry.delete(0,"end")
        else:                         # değil ise hata mesajı verir ve kayıt tamamlanamaz.
            messagebox.showerror(title="error message",message="wrong password!!")
            L2_entry.delete(0,"end")
        
    B1=tk.Button(frame1,text="Registration Completed",fg="white",bg="blue",command=registration_is_over)
    B1.place(x=124,y=290)



def login():      # giriş yapma kısmı.   

    password=password_entry.get()      
    if password=="software":          # password=="software" ise giriş başarılı.
        messagebox.showinfo(title="Info",message="Login successful.")
        password_entry.delete(0,"end")
        mail_entry.delete(0,"end")
        
        frame2=tk.Toplevel()          # ikinci pencere oluşturulur.
        frame2.geometry("450x250+450+100")
        frame2.resizable(False,False)
        frame2.config(bg="pink")
        
        #Giriş yaptıktan sonra sipariş vermek için aşağıdaki kısımlar doldurulur.
        L4=tk.Label(frame2,text="Name-Surname:",fg="blue",bg="orange",font="Times 12 italic")
        L4.place(x=10,y=40)
        L5=tk.Label(frame2,text="Dimension:",fg="blue",bg="orange",font="Times 12 italic")
        L5.place(x=10,y=70)
        L6=tk.Label(frame2,text="Contents:",fg="blue",bg="orange",font="Times 12 italic")
        L6.place(x=10,y=100)
        L7=tk.Label(frame2,text="Address:",fg="blue",bg="orange",font="Times 12 italic")
        L7.place(x=10,y=130)

        entr=tk.StringVar()      
        entr1=tk.StringVar()

        L4_entry=tk.Entry(frame2,textvariable=entr)
        L4_entry.place(x=140,y=42)
        L7_entry=tk.Entry(frame2,textvariable=entr1)
        L7_entry.place(x=140,y=135)

        dimension=tk.StringVar()       # pizza büyüklüğünü seçin.

        R1=tk.Radiobutton(frame2,text="Small ",bg="pink",activebackground="yellow",value="Small",variable=dimension)
        R1.place(x=136,y=70)
        R2=tk.Radiobutton(frame2,text="Medium ",bg="pink",activebackground="yellow",value="Medium",variable=dimension)
        R2.place(x=225,y=70)
        R3=tk.Radiobutton(frame2,text="Large ",bg="pink",activebackground="yellow",value="Large",variable=dimension)
        R3.place(x=322,y=70)

        value1=tk.StringVar()
        value2=tk.StringVar()
        value3=tk.StringVar()          # pizzanın içindekilerini seçin.

        C1=tk.Checkbutton(frame2,text="With Sausage",bg="pink",variable=value1,onvalue="With Sausage")
        C1.place(x=136,y=100) 
        C2=tk.Checkbutton(frame2,text="Egyptian",bg="pink",variable=value2,onvalue="Egyptian")
        C2.place(x=240,y=100)
        C3=tk.Checkbutton(frame2,text="Hot Sauce",bg="pink",variable=value3,onvalue="Hot Sauce")
        C3.place(x=324,y=100)

        def order():                  # sipariş verme kısmı.
            frame3=tk.Toplevel()
            frame3.geometry("450x250+450+100")    # üçüncü pencere oluşturulur.
            frame3.resizable(False,False)
            frame3.config(bg="pink")

            # Sipariş verildikten sonra sipariş bilgilerini getirir.
            L8=tk.Label(frame3,text="Order İnformation",bg="light blue",font="Times 16 italic")
            L8.place(x=140,y=10)
            L9=tk.Label(frame3,text="Name-Surname :",bg="light blue",font="Times 12 italic")
            L9.place(x=10,y=65)
            L10=tk.Label(frame3,text="Dimension :",bg="light blue",font="Times 12 italic")
            L10.place(x=10,y=95)
            L11=tk.Label(frame3,text="Contents :",bg="light blue",font="Times 12 italic")
            L11.place(x=10,y=125)
            L12=tk.Label(frame3,text="Address :",bg="light blue",font="Times 12 italic")
            L12.place(x=10,y=155)

            
            L9_name=tk.Entry(frame3,bg="pink",font="Times 12 italic")
            L9_name.place(x=140,y=65)
            L9_name.insert(0,entr.get())
            L10_dimension=tk.Label(frame3,text=dimension.get(),bg="pink",font="Times 12 italic")
            L10_dimension.place(x=140,y=95)
            L11_contents=tk.Label(frame3,text=value1.get()+" , "+value2.get()+" , "+value3.get(),bg="pink",font="Times 12 italic")
            L11_contents.place(x=140,y=125)
            L12_address=tk.Entry(frame3,bg="pink",font="Times 12 italic")
            L12_address.place(x=140,y=155)
            L12_address.insert(0,entr1.get())

            L4_entry.delete(0,"end")
            L7_entry.delete(0,"end")

            def back():           # sipariş bilgileri kısmını kapatır ve sipariş verme kısmına döner.
                frame3.destroy()

            B7=tk.Button(frame3,text="Back",bg="light blue",width=20,activebackground="green",command=back)
            B7.place(x=130,y=200)

            frame3.mainloop()
        
        def back():             # sipariş verme kısmını kapatır ve giriş kısmına döner.
            frame2.destroy()

        B2=tk.Button(frame2,text="Order",activebackground="green",command=order)  # sipariş ver butonu.
        B2.place(x=150,y=170)
        B3=tk.Button(frame2,text="Back",activebackground="green",command=back)    
        B3.place(x=220,y=170)

        frame2.mainloop()

    else:          # password=="software" değil ise hata mesajı verir ve giriş yapılamaz. 
        messagebox.showerror(title="error message",message="wrong password!!")
        password_entry.delete(0,"end")
    
 
def exit():      # giriş kısmından çıkış yapmak için.
    answer=messagebox.askyesno("Hi","Are you sure to exit? ")
    if answer == 1:         
        frame1.destroy()
    else:
        return

B4=tk.Button(frame1,text="Register ",fg="white",bg="blue",command=register)  # kayıt olma butonu.
B4.place(x=124,y=133)
B5=tk.Button(frame1,text="Login ",fg="white",bg="blue",command=login)        # giriş yapma butonu.
B5.place(x=194,y=133)
B6=tk.Button(frame1,text="Exit ",fg="white",bg="blue",width=4,command=exit)      # çıkış yapma butonu.
B6.place(x=254,y=133)


frame1.mainloop()
