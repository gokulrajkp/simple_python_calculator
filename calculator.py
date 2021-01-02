from tkinter import *
#creating windoe
window = Tk()
window.geometry("400x400")
window.title("CALCULATOR")
window.configure(bg="#FFE5B4")
#text feild creating
text_field= Entry(window,bd="5", width="43",)
#define buttons
btn_7=Button(window,text="7",padx=20,pady=10,command=lambda :btn_clicked(7))
btn_8=Button(window,text="8",padx=20,pady=10,command=lambda :btn_clicked(8))
btn_9=Button(window,text="9",padx=20,pady=10,command=lambda :btn_clicked(9))
btn_div=Button(window,text="/",padx=20,pady=10,command=lambda :btn_clicked("/"))

btn_4=Button(window,text="4",padx=20,pady=10,command=lambda :btn_clicked(4))
btn_5=Button(window,text="5",padx=20,pady=10,command=lambda :btn_clicked(5))
btn_6=Button(window,text="6",padx=20,pady=10,command=lambda :btn_clicked(6))
btn_mul=Button(window,text="*",padx=20,pady=10,command=lambda :btn_clicked("*"))

btn_1=Button(window,text="1",padx=20,pady=10,command=lambda :btn_clicked(1))
btn_2=Button(window,text="2",padx=20,pady=10,command=lambda :btn_clicked(2))
btn_3=Button(window,text="3",padx=20,pady=10,command=lambda :btn_clicked(3))
btn_min=Button(window,text="-",padx=20,pady=10,command=lambda :btn_clicked("-"))

btn_0=Button(window,text="0",padx=20,pady=10,command=lambda :btn_clicked(0))
btn_dot=Button(window,text=".",padx=20,pady=10,command=lambda :btn_clicked("."))
btn_equal=Button(window,text="=",padx=20,pady=10,command=lambda :evaluate())
btn_plus=Button(window,text="+",padx=20,pady=10,command=lambda :btn_clicked("+"))

btn_clear=Button(window,text="c",padx=20,pady=10,command=lambda :btn_clear())

##assign button positions
btn_7.grid(row="2",column='0',pady=22)
btn_8.grid(row="2",column='1')
btn_9.grid(row="2",column='2')
btn_div.grid(row="2",column='3')

btn_4.grid(row="3",column='0',)
btn_5.grid(row="3",column='1',)
btn_6.grid(row="3",column='2')
btn_mul.grid(row="3",column='3')

btn_1.grid(row="4",column='0',pady=22)
btn_2.grid(row="4",column='1')
btn_3.grid(row="4",column='2')
btn_min.grid(row="4",column='3')

btn_0.grid(row="5",column='0',)
btn_dot.grid(row="5",column='1')
btn_equal.grid(row="5",column='2')
btn_plus.grid(row="5",column='3')

btn_clear.grid(row="1",column='0')

text_field.grid(row="0",column="0",columnspan="4",padx=(20),pady=(15))

#defining functions
def btn_clicked(num):
    old_val=text_field.get()
    text_field.delete(0,END)
    operation=str(old_val)+str(num)
    text_field.insert(0,operation)

def btn_clear():
    text_field.delete(0,END)

def evaluate():
    rslt=str(eval(text_field.get()))
    text_field.delete(0,END)
    text_field.insert(0,rslt)

window.mainloop()