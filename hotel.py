from tkinter import *
from PIL import Image,ImageTk
import ttkbootstrap as tb
import connections
from tkinter import messagebox
win=Tk()
# win=tb.Window(themename="morph")
win.title("Bank management")
win.state("zoomed")
win.config(bg="white")

bg=Image.open("images/bank1.png")
bg=bg.resize((1400,700))
bg=ImageTk.PhotoImage(bg)
bglabel=Label(win,image=bg)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

def register():
    firstname=fentry.get()
    lastname=lentry.get()
    email=eentry.get()
    password=passentry.get()
    data=(firstname, lastname, email, password)
    # print(data)
    try:
        q="insert into signup2(firstname, lastname, email,  password) values (?,?,?,?)"
        connections.cur.execute(q,data)
        connections.con.commit()
        messagebox.showinfo("Success","Signup successful")
    except Exception as e:
        print(e)
        messagebox.showerror("Error","Error in signup")

def toggle_password():
    if pentry.cget('show') == '':
        pentry.config(show='*')
        toggle_btn.config(text="Show")
    else:
        pentry.config(show='')
        toggle_btn.config(text="Hide")

def show_password():
    if passentry.cget('show') == '':
        passentry.config(show='*')
        show_btn.config(text="Show")
    else:
        passentry.config(show='')
        show_btn.config(text="Hide")


    # LOGIN
    login = LabelFrame(win, width=350, height=500, bg="snow")
    login.place(x=250, y=100)

    heading=Label(login, text="Login form", font=('Arial',13))
    heading.place(x=20, y=20)

    username=Label(login, text="username",font=("Arial",13))
    username.place(x=20, y=95)

    uentry=Entry(login, font=("Arial", 13))
    uentry.place(x=20, y=120, height=30, width=300)

    password=Label(login, text="Password",font=("Arial",13))
    password.place(x=20, y=180)

    pentry=Entry(login,  font=("Arial", 13), show="*")
    pentry.place(x=20, y=205, height=30, width=300)

    toggle_btn = Button(login, text="Show",font=("Arial",10), bg="black", fg="snow", command=toggle_password)
    toggle_btn.place(x=25,y=240, height=22, width=40)

    loginbtn=Button(login, text="LOGIN",font=("Arial",13))
    loginbtn.place(x=20, y=285)

# SIGNUP
    signup = LabelFrame(win, width=350, height=500, bg="white")
    signup.place(x=700, y=100)

    heading=Label(signup, text="SIGNUP", font=("Arial",13))
    heading.place(x=25, y=10)

    firstname=Label(signup, text="firstname",font=("Arial",13))
    firstname.place(x=20, y=80)
    fentry=Entry(signup, font=("Arial", 13))
    fentry.place(x=20, y=110, height=30, width=300)

    lastname=Label(signup, text="Username",font=("Arial",13),bg="snow")
    lastname.place(x=20, y=150)
    lentry=Entry(signup, bg="snow", font=("Arial", 13))
    lentry.place(x=20, y=175, height=30, width=300)

    email=Label(signup, text="Email",font=("Arial",13))
    email.place(x=20, y=215)
    eentry=Entry(signup,  font=("Arial", 13))
    eentry.place(x=20, y=240, height=30, width=305)

    password=Label(signup, text="Password",font=("Arial",13))
    password.place(x=20, y=280)
    passentry=Entry(signup,  font=("Arial", 13), show="*")
    passentry.place(x=20, y=305, height=30, width=300)

    show_btn = Button(signup, text="Show",font=("Arial",10), command=show_password, bg="black", fg="snow")
    show_btn.place(x=25,y=340, height=22, width=40)

    signbtn=Button(signup, text="SIGNUP",font=("Arial",14), bg="black", fg="snow", command=register)
    signbtn.place(x=20, y=380, height=30, width=305)

    win.mainloop()