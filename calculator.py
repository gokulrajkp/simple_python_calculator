from tkinter import *
#creating windoe
window = Tk()
window.geometry("400x500")
window.title("CALCULATOR")
window.configure(bg="#FFE5B4")
#text feild creating
text_field= Entry(window,bd="5", width="43",)
#define buttons
btn_7=Button(window,text="7",padx=20,pady=10,command="btn_add")
btn_8=Button(window,text="8",padx=20,pady=10,command="btn_add")
btn_9=Button(window,text="9",padx=20,pady=10,command="btn_add")
btn_div=Button(window,text="/",padx=20,pady=10,command="btn_add")

btn_4=Button(window,text="4",padx=20,pady=10,command="btn_add")
btn_5=Button(window,text="5",padx=20,pady=10,command="btn_add")
btn_6=Button(window,text="6",padx=20,pady=10,command="btn_add")
btn_mul=Button(window,text="*",padx=20,pady=10,command="btn_add")

btn_1=Button(window,text="1",padx=20,pady=10,command="btn_add")
btn_2=Button(window,text="2",padx=20,pady=10,command="btn_add")
btn_3=Button(window,text="3",padx=20,pady=10,command="btn_add")
btn_min=Button(window,text="-",padx=20,pady=10,command="btn_add")

btn_0=Button(window,text="0",padx=20,pady=10,command="btn_add")
btn_dot=Button(window,text=".",padx=20,pady=10,command="btn_add")
btn_equal=Button(window,text="=",padx=20,pady=10,command="btn_add")
btn_plus=Button(window,text="+",padx=20,pady=10,command="btn_add")

##assign button positions
btn_7.grid(row="1",column='0',)
btn_8.grid(row="1",column='1')
btn_9.grid(row="1",column='2')
btn_div.grid(row="1",column='3')

btn_4.grid(row="2",column='0',)
btn_5.grid(row="2",column='1')
btn_6.grid(row="2",column='2')
btn_mul.grid(row="2",column='3')

btn_1.grid(row="3",column='0',)
btn_2.grid(row="3",column='1')
btn_3.grid(row="3",column='2')
btn_min.grid(row="3",column='3')

btn_0.grid(row="4",column='0',)
btn_dot.grid(row="4",column='1')
btn_equal.grid(row="4",column='2')
btn_plus.grid(row="4",column='3')

text_field.grid(row="0",column="0",columnspan="4",padx=(20),pady=(15))

window.mainloop()