from lib2to3.pgen2.token import PERCENT
from tkinter import *
from tkinter.messagebox import showerror
from tokenize import String
from tkinter import END
from turtle import dot

kunal_root = Tk()
kunal_root.geometry("200x400")
kunal_root.resizable(False , False)

kunal_root.title("Calculator")

canvas=Canvas(kunal_root , width=200 , height=500 , bg="orange")
canvas.pack()

txt = Text(kunal_root , width=15 , height=2 , font=(14))

button9 = Button(kunal_root , text="9" , width=5 , height=2)

button8 = Button(kunal_root,text="8" , width=5 , height=2)

button7 = Button(kunal_root,text="7" , width=5 , height=2 ) 

button6 = Button(kunal_root,text="6" , width=5 , height=2)

button5 = Button(kunal_root,text="5" , width=5 , height=2)

button4 = Button(kunal_root,text="4" , width=5 , height=2)

button3 = Button(kunal_root,text="3" , width=5 , height=2)

button2 = Button(kunal_root,text="2" , width=5 , height=2)

button1 = Button(kunal_root,text="1" , width=5 , height=2)

button0 = Button(kunal_root,text="0" , width=5 , height=2)

buttonp = Button(kunal_root , text='+' , width=5 , height=2)

buttonmi = Button(kunal_root , text='-' , width=5 , height=2)

buttonmp=Button(kunal_root , text='*' , width=5 , height=2)

buttondv=Button(kunal_root , text='/' , width=5 , height=2)

buttoneq = Button(kunal_root , text='=' , width=5 , height=2)

buttondot=Button(kunal_root , text='.' , width=5 , height=2)

buttonpercent=Button(kunal_root , text='%' , width=5 , height=2)

buttonclear=Button(kunal_root , text='C' , width=5 , height=2)







canvas.create_window(100 , 40 , window=txt)
canvas.create_window(50 , 100, window=button9)
canvas.create_window(100 , 100, window=button8)
canvas.create_window(150 , 100, window=button7)
canvas.create_window(50 , 150, window=button6)
canvas.create_window(100 , 150, window=button5)
canvas.create_window(150 , 150, window=button4)
canvas.create_window(50 , 200, window=button3)
canvas.create_window(100 , 200, window=button2)
canvas.create_window(150 , 200, window=button1)
canvas.create_window(150 , 250, window=button0)
canvas.create_window(50 , 250, window=buttonp)
canvas.create_window(100 , 250 , window=buttonmi)
canvas.create_window(50 , 300, window=buttonmp)
canvas.create_window(100 , 300, window=buttondv)
canvas.create_window(150 , 300, window=buttoneq)
canvas.create_window(100 , 350 , window=buttondot)
canvas.create_window(50 , 350, window=buttonpercent)
canvas.create_window(150 , 350, window=buttonclear)


class ButtonNum():
    def one_f():
        txt.insert(END , "1")

    def two_f():
        txt.insert(END ,"2")

    def three_f():
        txt.insert(END , "3")

    def four_f():
        txt.insert(END , "4")

    def five_f():
        txt.insert(END , "5")

    def six_f():
        txt.insert(END , "6")

    def seven_f():
        txt.insert(END , "7")

    def eight_f():
        txt.insert(END , "8")

    def nine_f():
        txt.insert(END , "9")
       
    def zero_f():
        txt.insert(END , "0")

    def clear_f():
        txt.delete(1.0 , END)

    def percent_f():
        txt.insert(END , "%")

    def dot_f():
        txt.insert(END , ".")

class Operators():
    def add_f():
        txt.insert(END , "+")

    def sub_f():
        txt.insert(END , "-")

    def mul_f():
        txt.insert(END , "*")

    def div_f():
        txt.insert(END , "/")
        
def equal():
    try:
	    y = str(eval(txt.get(1.0 , END)))
	    txt.delete(1.0, END)
	    txt.insert(1.0, y)
    except Exception:
        showerror("Error" , "ArithmeticError generated")

button1.configure(command=ButtonNum.one_f)
button2.configure(command=ButtonNum.two_f)
button3.configure(command=ButtonNum.three_f)
button4.configure(command=ButtonNum.four_f)
button5.configure(command=ButtonNum.five_f)
button6.configure(command=ButtonNum.six_f)
button7.configure(command=ButtonNum.seven_f)
button8.configure(command=ButtonNum.eight_f)
button9.configure(command=ButtonNum.nine_f)
button0.configure(command=ButtonNum.zero_f)
buttonp.configure(command=Operators.add_f)
buttondv.configure(command=Operators.div_f)
buttonmi.configure(command=Operators.sub_f)
buttonmp.configure(command=Operators.mul_f)
buttoneq.configure(command=equal)
buttonclear.configure(command=ButtonNum.clear_f)
buttondot.configure(command=ButtonNum.dot_f)


kunal_root.mainloop() 