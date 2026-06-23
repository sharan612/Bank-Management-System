from tkinter import *
from PIL import Image,ImageTk
from connections import get_connection
from tkinter import messagebox
from dashboard import dashboard
 
def loginfn():
    loginwin=Toplevel()
    loginwin.title("Bank management")
    loginwin.state("zoomed")
    
    bg1=Image.open("images/bank1.png")
    bg1=bg1.resize((1400,710))
    bg1=ImageTk.PhotoImage(bg1)
    bglabel1=Label(loginwin,image=bg1)
    bglabel1.image=bg1
    bglabel1.place(x=0, y=0, relwidth=1, relheight=1)
        
    def placehold(entry, ph_text):
        entry.insert(0, ph_text)
        entry.config(fg='grey')
        def on_entry(event):
                if entry.get() == ph_text:
                    entry.delete(0, "end")
                    entry.config(fg='black')
        def on_focusout(event):
                if entry.get() == '':
                    entry.insert(0, ph_text)
                    entry.config(fg='grey')
        entry.bind('<FocusIn>', on_entry)
        entry.bind('<FocusOut>', on_focusout)

    def ph_password(entry, placeholder_text):
        entry.insert(0, placeholder_text)
        entry.config(fg='grey', show='')
        def entry1(event):
            if entry.get() == placeholder_text:
                entry.delete(0, "end")
                entry.config(fg='black', show='*')
        def focusout(event):
            if entry.get() == '':
                entry.insert(0, placeholder_text)
                entry.config(fg='grey', show='')
        entry.bind('<FocusIn>', entry1)
        entry.bind('<FocusOut>', focusout)

    def userlogin():
            username=un.get()
            password=pw.get()
            userdata=(username,password)
            try:
                con = get_connection()
                cur = con.cursor()
                query="select role from signup where username=? and password=?"
                cur.execute(query,userdata)
                res=cur.fetchone()
                if res:
                    role=res[0]
                    messagebox.showinfo("Success","Login Done",parent=loginwin)
                    loginwin.destroy()
                    dashboard(username,role)
                else:
                    messagebox.showwarning("Error","Inavalid username or password", parent=loginwin)
                con.close()
            except Exception as ex:
                print("Login Error:", ex)
                messagebox.showerror("Error","Error",parent=loginwin)

    def toggle_password():
        if pw.cget('show') == '':
            pw.config(show='*')
            toggle_btn.config(text="Show")
        else:
            pw.config(show='')
            toggle_btn.config(text="Hide")

    login = LabelFrame(loginwin, width=350, height=420, bg="#A3C9F9")
    login.place(x=500, y=120)

    Label(login, text="LOGIN", font=('Bahnschrift',18,"bold"),fg="#06112B", bg="#A3C9F9").place(x=20, y=20)

    # Label(login, text="Username",font=("Bahnschrift",13),bg="snow").place(x=20, y=90)
    un=Entry(login, font=("Bahnschrift", 13), bd=0, bg="#AFD2FC")
    un.place(x=20, y=120, height=30, width=305)
    underline = Frame(login, height=2, width=305, bg="#06112B")
    underline.place(x=20, y=150)
    placehold(un, "Username")

    # Label(login, text="Password",font=("Bahnschrift",13),bg="snow").place(x=20, y=170)
    pw=Entry(login,  font=("Bahnschrift", 13), bd=0, bg="#AFD2FC", show="*")
    pw.place(x=20, y=200, height=30, width=305)
    passline = Frame(login, height=2, width=305, bg="#06112B")
    passline.place(x=20, y=230)
    # placeholder(pentry, "Password")
    ph_password(pw, "Password")

    toggle_btn = Button(login, text="Show",font=("Bahnschrift",10), command=toggle_password, bg="#06112B", fg="#E6F0FA")
    toggle_btn.place(x=20,y=240, height=20, width=50)

    Button(login, text="LOGIN",font=("Bahnschrift",14,"bold"), bg="#06112B", fg="#E6F0FA", command=userlogin).place(x=20, y=340, height=30, width=305)

    signbtn=Button(login, text="Don't have an account? SIGNUP", font=("Bahnschrift",10), command=loginwin.destroy)
    signbtn.place(x=65, y=380, height=25, width=210)