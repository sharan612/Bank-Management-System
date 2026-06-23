from tkinter import *
from PIL import Image,ImageTk
from connections import get_connection
from tkinter import messagebox
from banklogin import loginfn
 
win=Tk()
win.title("Bank management")
win.state("zoomed") 
win.config()

bg_img=Image.open("images/bank1.png")
bg_img=bg_img.resize((1400,710))
bg_img=ImageTk.PhotoImage(bg_img)
bglabel=Label(win,image=bg_img)
bglabel.image=bg_img
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

def register():
    fullname=fentry.get()
    username=uentry.get()
    email=eentry.get()
    password=pentry.get()
    role=role_var.get()
    data=(fullname, username, email, password, role)
    # print(data)
    try:
        con = get_connection()
        cur = con.cursor()
        q="insert into signup(fullname, username, email, password, role) values (?,?,?,?,?)"
        cur.execute(q,data)
        con.commit()
        messagebox.showinfo("Success","Signup successful")
        con.close()
    except Exception as e:
        print(e)
        messagebox.showerror("Error","Error in signup")

def placeholder(entry, ph_text):
    entry.insert(0, ph_text)
    entry.config(fg='grey')
    def on_entry(event):
        if entry.get() == ph_text:
            entry.delete(0, "end")
            entry.config(fg='#F5F5F5')
    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, ph_text)
            entry.config(fg='grey')
    entry.bind('<FocusIn>', on_entry)
    entry.bind('<FocusOut>', on_focusout)

def ph_pass(pentry, placeholder_text):
    pentry.insert(0, placeholder_text)
    pentry.config(fg='grey', show='')
    def focusin(event):
        if pentry.get() == placeholder_text:
            pentry.delete(0, "end")
            pentry.config(fg='#F5F5F5', show='*')
    def focusout(event):
        if pentry.get() == '':
            pentry.insert(0, placeholder_text)
            pentry.config(fg='grey', show='')
    pentry.bind('<FocusIn>', focusin)
    pentry.bind('<FocusOut>', focusout)

def show_password():
    if pentry.cget('show') == '':
        pentry.config(show='*')
        show_btn.config(text="Show")
    else:
        pentry.config(show='')
        show_btn.config(text="Hide")

signup = LabelFrame(win, width=350, height=500, bg="#06021F")
signup.place(x=500, y=100)

Label(signup, text="BANK SIGNUP", font=("Bahnschrift",18,"bold"), bg="#06021F", fg="#BAD7FA").place(x=15, y=15)

# Label(signup, text="Fullname",font=("Bahnschrift",13), bg="#070920", fg="#F5F5F5").place(x=20, y=80)
fentry=Entry(signup, font=("Bahnschrift", 13), bd=0, bg="#080325", fg="gray", insertbackground='#E6F0FA')
fentry.place(x=20, y=100, height=30, width=305)
fline = Frame(signup, height=2, width=305, bg="#E6F0FA")
fline.place(x=20, y=130)
placeholder(fentry, "Fullname")

# Label(signup, text="Username",font=("Bahnschrift",13), bg="#070920", fg="#F5F5F5").place(x=20, y=145)
uentry=Entry(signup, font=("Bahnschrift", 13), bd=0, bg="#080325", fg="#E6F0FA", insertbackground='#E6F0FA')
uentry.place(x=20, y=160, height=30, width=305)
uline = Frame(signup, height=2, width=305, bg="#F5F5F5")
uline.place(x=20, y=190)
placeholder(uentry, "Username")

# Label(signup, text="Email",font=("Bahnschrift",13), bg="#070920", fg="#F5F5F5").place(x=20, y=205)
eentry=Entry(signup,  font=("Bahnschrift", 13), bd=0, bg="#080325", fg="#E6F0FA", insertbackground='#E6F0FA')
eentry.place(x=20, y=220, height=30, width=305)
eline = Frame(signup, height=2, width=305, bg="#E6F0FA")
eline.place(x=20, y=250)
placeholder(eentry, "Email")

# Label(signup, text="Password",font=("Bahnschrift",13), bg="#070920", fg="#F5F5F5").place(x=20, y=265)
pentry=Entry(signup, font=("Bahnschrift", 13), bd=0, bg="#080325", fg="#E6F0FA", insertbackground='#E6F0FA', show="*")
pentry.place(x=20, y=280, height=30, width=305)
pline = Frame(signup, height=2, width=305, bg="#F5F5F5")
pline.place(x=20, y=310)
# placeholder(pentry, "Password")
ph_pass(pentry, "Password")

show_btn = Button(signup, text="Show",font=("Bahnschrift",10), bg="#1E90FF", fg="#E6F0FA", command=show_password)
show_btn.place(x=20,y=320, height=20, width=50)

role_var = StringVar()
role_var.set(None)
Radiobutton(signup, text="Staff", variable=role_var, value="staff", font=("Bahnschrift",12,"bold"), bg="#06021F", fg="#E6F0FA").place(x=20, y=350)
Radiobutton(signup, text="Customer", variable=role_var, value="customer",font=("Bahnschrift",12,"bold"), bg="#06021F", fg="#E6F0FA").place(x=100, y=350)

Button(signup, text="SIGNUP",font=("Bahnschrift",14,"bold"), bg="#4169E1", fg="#E6F0FA", command=register).place(x=20, y=420, height=32, width=305)

logbtn=Button(signup, text="Already a user? LOGIN", font=("Bahnschrift",10), command=loginfn)
logbtn.place(x=80, y=460, height=25, width=170)

win.mainloop()