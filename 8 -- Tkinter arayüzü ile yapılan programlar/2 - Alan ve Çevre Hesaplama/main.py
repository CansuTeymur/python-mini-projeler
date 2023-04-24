

"""
kare,dikdörtgen,daire ve üçgenin  alanını,çevresini hesaplayan program.

"""

import tkinter as tk
from tkinter.ttk import Combobox 
import math

frame=tk.Tk()
frame.title("Area and Perimeter Calculation")
frame.geometry("400x250")
frame.resizable(False,False)


label_choice=tk.Label(frame,text="Your Choice : ",fg="green",font="consoles 14 bold")
label_choice.place(x=20,y=70)

x=tk.StringVar()

a=["area of the square","perimeter of the square","area of rectangle","perimeter of rectangle","area of the circle","perimeter of the circle","area of triangle","perimeter of triangle"]
box=Combobox(frame,values=a,height=3,textvariable=x)
box.place(x=180,y=74)


def show():
    frame2=tk.Toplevel()
    frame2.geometry("320x300")
    frame2.title("Area and Perimeter Calculation")
    frame2.resizable(False,False)

    if x.get()=="area of the square" or x.get()=="perimeter of the square":

        L2=tk.Label(frame2,text="enter an edge : ",font="Vergana 10 bold")
        L2.place(x=10,y=100)
        entry_edge=tk.Entry(frame2,width=20)
        entry_edge.place(x=130,y=104)
        L3=tk.Label(frame2,text="result : ",font="Vergana 10 bold")
        L3.place(x=10,y=134)
        entry_result=tk.Entry(frame2,width=20)
        entry_result.place(x=130,y=134)

        def back():
            frame2.destroy()

        if x.get()=="area of the square":        # karenin alanı
            L1=tk.Label(frame2,text="area of the square ",fg="blue",width=18,font="Vergana 15 bold")
            L1.place(x=36,y=40)
        
            def calculate():
                entry_result.delete(0,"end")
                rslt=(int(entry_edge.get()))*(int(entry_edge.get()))
                entry_result.insert(0,rslt)
                entry_edge.delete(0,"end")

        if x.get()=="perimeter of the square":       # karenin çevresi
            L4=tk.Label(frame2,text="perimeter of the square",fg="blue",width=18,font="Vergana 15 bold")
            L4.place(x=34,y=40)

            def calculate():
                entry_result.delete(0,"end")
                rslt=(int(entry_edge.get()))*4
                entry_result.insert(0,rslt)
                entry_edge.delete(0,"end")

        B1=tk.Button(frame2,text="calculate",fg="blue",bg="orange",width=9,command=calculate)
        B1.place(x=110,y=170)
        B2=tk.Button(frame2,text="back",fg="blue",bg="orange",width=9,command=back)
        B2.place(x=190,y=170)

    elif x.get()=="area of rectangle" or x.get()=="perimeter of rectangle": 
        
        L5=tk.Label(frame2,text="short edge : ",font="Vergana 10 bold")
        L5.place(x=10,y=100)
        L6=tk.Label(frame2,text="long edge : ",font="Vergana 10 bold")
        L6.place(x=10,y=125)
        short_entry=tk.Entry(frame2,width=17)
        short_entry.place(x=120,y=100)
        long_entry=tk.Entry(frame2,width=17)
        long_entry.place(x=120,y=125)
        L7=tk.Label(frame2,text="result : ",font="Vergana 10 bold")
        L7.place(x=10,y=150)
        entry_result=tk.Entry(frame2,width=17)
        entry_result.place(x=120,y=150)

        def back():
            frame2.destroy()

        if x.get()=="area of rectangle":          # dikdörtgenin alanı
            L8=tk.Label(frame2,text="area of rectangle",fg="blue",width=18,font="Vergana 15 bold")
            L8.place(x=30,y=40)
            
            def calculate():
                entry_result.delete(0,"end")
                rslt=(int(short_entry.get()))*(int(long_entry.get()))
                entry_result.insert(0,rslt)
                short_entry.delete(0,"end")
                long_entry.delete(0,"end")

        if x.get()=="perimeter of rectangle":       # dikdörtgenin çevresi
            L9=tk.Label(frame2,text="perimeter of rectangle",fg="blue",width=18,font="Vergana 15 bold")
            L9.place(x=35,y=40)

            def calculate():
                entry_result.delete(0,"end")
                rslt=((int(short_entry.get()))+(int(long_entry.get())))*2
                entry_result.insert(0,rslt)
                short_entry.delete(0,"end")
                long_entry.delete(0,"end")

        B3=tk.Button(frame2,text="calculate",fg="blue",bg="orange",width=9,command=calculate)
        B3.place(x=110,y=180)
        B4=tk.Button(frame2,text="back",fg="blue",bg="orange",width=9,command=back)
        B4.place(x=190,y=180)   

    elif x.get()=="area of the circle" or x.get()=="perimeter of the circle":

        L10=tk.Label(frame2,text="enter the radius : ",font="Vergana 10 bold")
        L10.place(x=10,y=100)
        entry_radius=tk.Entry(frame2,width=20)
        entry_radius.place(x=130,y=104)
        L11=tk.Label(frame2,text="result : ",font="Vergana 10 bold")
        L11.place(x=10,y=134)
        entry_result=tk.Entry(frame2,width=20)
        entry_result.place(x=130,y=134)

        def back():
            frame2.destroy()

        if x.get()=="area of the circle":          # dairenin alanı
            L12=tk.Label(frame2,text="area of the circle",fg="blue",width=18,font="Vergana 15 bold")
            L12.place(x=35,y=40)

            def calculate():
                entry_result.delete(0,"end")
                rslt=((float(entry_radius.get()))**2)*math.pi
                entry_result.insert(0,rslt)
                entry_radius.delete(0,"end")        
        
        if x.get()=="perimeter of the circle":        # dairenin çevresi
            L13=tk.Label(frame2,text="perimeter of the circle",fg="blue",width=18,font="Vergana 15 bold")
            L13.place(x=35,y=40)
        
            def calculate():
                entry_result.delete(0,"end")
                rslt=(float(entry_radius.get()))*math.pi*2
                entry_result.insert(0,rslt)
                entry_radius.delete(0,"end")        

        B5=tk.Button(frame2,text="calculate",fg="blue",bg="orange",width=9,command=calculate)
        B5.place(x=110,y=180)
        B6=tk.Button(frame2,text="back",fg="blue",bg="orange",width=9,command=back)
        B6.place(x=190,y=180) 

    elif x.get()=="area of triangle" or x.get()=="perimeter of triangle":

        def back():
            frame2.destroy()

        if x.get()=="area of triangle":    # üçgenin alanı

            L14=tk.Label(frame2,text="area of triangle",fg="blue",width=20,font="Vergana 15 bold")
            L14.place(x=34,y=40)
            L15=tk.Label(frame2,text="base : ",font="Vergana 10 bold")
            L15.place(x=10,y=110)
            base_entry=tk.Entry(frame2,width=17)
            base_entry.place(x=120,y=110)
            L16=tk.Label(frame2,text="height : ",font="Vergana 10 bold")
            L16.place(x=10,y=135)
            height_entry=tk.Entry(frame2,width=17)
            height_entry.place(x=120,y=135)
            L17=tk.Label(frame2,text="result : ",font="Vergana 10 bold")
            L17.place(x=10,y=160)
            entry_result=tk.Entry(frame2,width=17)
            entry_result.place(x=120,y=160)

            def calculate():
                entry_result.delete(0,"end")
                rslt=((int(base_entry.get()))*(int(height_entry.get())))/2
                entry_result.insert(0,rslt)
                base_entry.delete(0,"end")
                height_entry.delete(0,"end")


        if x.get()=="perimeter of triangle":      # üçgenin çevresi

            L18=tk.Label(frame2,text="perimeter of triangle",fg="blue",width=18,font="Vergana 15 bold")
            L18.place(x=37,y=40)
            L19=tk.Label(frame2,text="edge 1 : ",font="Vergana 10 bold")
            L19.place(x=10,y=100)
            edge1_entry=tk.Entry(frame2,width=17)
            edge1_entry.place(x=120,y=100)
            L20=tk.Label(frame2,text="edge 2 : ",font="Vergana 10 bold")
            L20.place(x=10,y=125)
            edge2_entry=tk.Entry(frame2,width=17)
            edge2_entry.place(x=120,y=125)
            L21=tk.Label(frame2,text="edge 3 : ",font="Vergana 10 bold")
            L21.place(x=10,y=150)
            edge3_entry=tk.Entry(frame2,width=17)
            edge3_entry.place(x=120,y=150)
            L22=tk.Label(frame2,text="result : ",font="Vergana 10 bold")
            L22.place(x=10,y=175)
            entry_result=tk.Entry(frame2,width=17)
            entry_result.place(x=120,y=175)

            def calculate():
                entry_result.delete(0,"end")
                rslt=(int(edge1_entry.get()))+(int(edge2_entry.get()))+(int(edge3_entry.get()))
                entry_result.insert(0,rslt)
                edge1_entry.delete(0,"end")
                edge2_entry.delete(0,"end")
                edge3_entry.delete(0,"end")


        B7=tk.Button(frame2,text="calculate",fg="blue",bg="orange",width=9,command=calculate)
        B7.place(x=110,y=205)
        B8=tk.Button(frame2,text="back",fg="blue",bg="orange",width=9,command=back)
        B8.place(x=190,y=205) 

    frame2.mainloop()

def close():
    frame.destroy()

B9=tk.Button(frame,text="Show",fg="blue",bg="orange",width=19,command=show)
B9.place(x=180,y=100)
B10=tk.Button(frame,text="Close",fg="blue",bg="orange",width=19,command=close)
B10.place(x=180,y=130)

frame.mainloop()
