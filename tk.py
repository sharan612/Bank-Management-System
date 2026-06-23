from tkinter import *
win=Tk()
win.geometry("600x400")
win.title("Python Program")
# win.state("zoomed")
win.config(bg="snow")

#WIDGETS(pack,place,grid)
# PACK(padding,side),side must be top, bottom, left, or right
# l1=Label(win,text="hello", font=('Arial',22),fg="red",bg="yellow")
# l1.pack(pady="10",side="left") 
# l2=Label(win,text="python",font=('Arial',22))
# l2.pack(pady="10",side="right")

# PLACE(x,y)coordinates
# l1=Label(win,text="hello", font=('Arial',22),fg="red",bg="yellow")
# l1.place(x=10,y=20)
# l2=Label(win,text="python",font=("Arial",22))
# l2.place(x=200,y=20)

# GRID(row,column)
# l1=Label(win,text="hello", font=('Arial',22))
# l1.grid(row=1,column=1)
# l2=Label(win,text="python",font=("Arial",22))
# l2.grid(row=2,column=1)

# FRAME
# f = Frame(win, bg="white", height=250, width=500)
# f.place(x=400, y=200)
# LABELFRAME for login section
lf= LabelFrame(win, text="Enter Details",bg="pale goldenrod",height=250,width=500)
lf.place(x=400, y=200)

heading=Label(lf, text="Login Form",font=('SimSun',18))
# heading.grid(row=0,column=0)
# heading.pack()
heading.place(x=10,y=10)
username=Label(lf,text="Username",font=('Arial',15)) #USERNAME
# username.grid(row=1,column=1,pady=5)
# username.pack()
username.place(x=100,y=50)
uentry=Entry(lf,font=("Arial",15))
# uentry.grid(row=1,column=2)
# uentry.pack()
uentry.place(x=200,y=50)
password=Label(lf,text="Password",font=("Arial",15)) #PASSWORD
# password.grid(row=2,column=1,pady=5)
# password.pack()
password.place(x=100,y=80)
pentry=Entry(lf,font=("Arial",15))
# pentry.grid(row=2,column=2)
# pentry.pack()
pentry.place(x=200,y=80)
loginbtn=Button(lf,text="LOGIN",font=("Arial",15,'bold')) #BUTTON
# loginbtn.grid(row=3,column=2)
# loginbtn.pack()
loginbtn.place(x=270,y=120)

win.mainloop()