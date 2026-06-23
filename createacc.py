import random
from tkinter import *
from connections import get_connection
from tkinter import messagebox
from tkcalendar import Calendar
# acc=Tk()
# acc.title("create acc")
# acc.state("zoomed")
 
def generate_acc_number():
    return "10" + str(random.randint(1000000000, 9999999999))

def create_acc(parent):
    accf=Frame(parent, width=1115, height=650, bg="#C2E1FF")
    accf.place(x=0, y=0)

    Label(accf, text="CREATE ACCOUNT", font=("Bahnschrift",22,"bold"), fg="#070920", bg="#C2E1FF").place(relx=0.5, y=10, anchor="n")

    def create():
        accnum=acc_num.get()
        fname=f_name.get()
        lname=l_name.get()
        acctype=acc_type.get()
        phnum=ph_num.get()
        gendr=gender.get()
        do_b=dob.get()
        email=mail.get()
        iamount=amount.get()
        udata=(accnum, fname, lname, acctype, phnum, gendr, do_b, email, iamount)
        try:
            con = get_connection()
            cur = con.cursor()
            qry="insert into accinfo(accnum, fname, lname, acctype, phnum, gendr, do_b, email, iamount) values (?,?,?,?,?,?,?,?,?)"
            cur.execute(qry,udata)
            con.commit()
            messagebox.showinfo("Success","Account created successfully", parent=accf)
            con.close()
        except Exception as e:
            print("Error❌:", e)
            messagebox.showerror("Error","Error in creating account", parent=accf)

    Label(accf, text="Account number", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=100)
    acc_num=Entry(accf, font=("Bahnschrift",14), bg="#A3C9F9")
    acc_num.place(x=520, y=100, width=300)

    def generate_num():
        acc_number = generate_acc_number()
        acc_num.delete(0, END)
        acc_num.insert(0, acc_number)

    Button(accf, text="Generate Acc Num", command=generate_num, font=("Bahnschrift", 10), bg="#070920", fg="#E6F0FA").place(x=850, y=100, width=150, height=26)

    Label(accf, text="Firstname", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=150)
    f_name=Entry(accf, font=("Bahnschrift",14), bg="#A3C9F9")
    f_name.place(x=520, y=150, width=300)

    Label(accf, text="Lastname", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=200)
    l_name=Entry(accf, font=("Bahnschrift",14), bg="#A3C9F9")
    l_name.place(x=520, y=200, width=300)

    Label(accf, text="Account type", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=250)
    acc_type = StringVar()
    acc_type.set("Savings account")
    r1 = Radiobutton(accf, text="Savings account", variable=acc_type, value="Savings account", font=("Bahnschrift", 12), bg="#C2E1FF")
    r2 = Radiobutton(accf, text="Current account", variable=acc_type, value="Current account", font=("Bahnschrift", 12), bg="#C2E1FF")
    r1.place(x=520, y=250)
    r2.place(x=680, y=250)

    Label(accf, text="Initial amount", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=300)
    amount=Entry(accf, font=("Bahnschrift",14), bg="#A3C9F9")
    amount.place(x=520, y=300, width=300)

    Label(accf, text="Phone number", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=350)
    ph_num=Entry(accf, font=("Bahnschrift",14), bg="#A3C9F9")
    ph_num.place(x=520, y=350, width=300)

    Label(accf, text="Gender", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=400)
    gender = StringVar()
    gender.set("Male")
    rb1 = Radiobutton(accf, text="Male", variable=gender, value="Male", font=("Bahnschrift", 12), bg="#C2E1FF")
    rb2 = Radiobutton(accf, text="Female", variable=gender, value="Female", font=("Bahnschrift", 12), bg="#C2E1FF")
    rb3 = Radiobutton(accf, text="Other", variable=gender, value="Other", font=("Bahnschrift", 12), bg="#C2E1FF")
    rb1.place(x=520, y=400)
    rb2.place(x=600, y=400)
    rb3.place(x=700, y=400)

    def open_calendar():
        def select_date():
            dob.delete(0, END)
            dob.insert(0, cal.get_date())
            cal_win.destroy()
        btn_x = calendar_btn.winfo_rootx()
        btn_y = calendar_btn.winfo_rooty()
        cal_win = Toplevel(accf)
        cal_win.overrideredirect(True)
        cal_win.title("Select DOB")
        cal_win.resizable(False, False)
        cal_win.geometry(f"+{btn_x + 5}+{btn_y - 30}")
        cal = Calendar(cal_win, selectmode='day',date_pattern='dd/mm/yyyy',background="white",foreground="black",headersbackground="#070920",headersforeground="#CFD3FD",normalbackground="#CFD3FD",weekendbackground="#ACB2FA")
        cal.pack(pady=5, padx=5)
        Button(cal_win, text="Select", font=("Segoe UI", 10), command=select_date).pack(pady=5)

    Label(accf, text="Date of birth", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=450)
    dob=Entry(accf, font=("Bahnschrift",14), bg="#A3C9F9")
    dob.place(x=520, y=450, width=300)

    calendar_btn = Button(accf, text="📆",font=(14), bg="#040616", fg="#DAEBFD", command=open_calendar)
    calendar_btn.place(x=790, y=450, height=26)

    Label(accf, text="Email", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=500)
    mail=Entry(accf, font=("Bahnschrift",14), bg="#A3C9F9")
    mail.place(x=520, y=500, width=300)

    Button(accf, text="Submit", font=("Bahnschrift",14), bg="#040616", fg="#E6F0FA", command=create).place(x=480, y=560, width=200, height=32)

    return accf