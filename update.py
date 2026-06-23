from tkinter import *
from tkinter import messagebox
from connections import get_connection
# upd=Tk()
# upd.title("update")
# upd.state("zoomed")
 
def update_acc(parent, data):

    upd=Frame(parent, width=1115, height=650, bg="#C2E1FF")
    upd.place(x=0, y=0)

    accn_var = StringVar(value=data[0])
    fn_var = StringVar(value=data[1])
    l_var = StringVar(value=data[2])
    acc_type = StringVar(value=data[3])
    ph_var = StringVar(value=data[4])
    gender = StringVar(value=data[5])
    dob_var = StringVar(value=data[6])
    mail_var = StringVar(value=data[7])
    amnt_var = StringVar(value=data[8])

    Label(upd, text="UPDATE ACCOUNT", font=("Bahnschrift",22, "bold"), fg="#070920", bg="#C2E1FF").place(relx=0.5, y=10, anchor="n")

    Label(upd, text="Account number", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=100)
    acc_num=Entry(upd, font=("Bahnschrift",14), bg="#A3C9F9", textvariable=accn_var, state="readonly")
    acc_num.place(x=520, y=100, width=300)

    Label(upd, text="Firstname", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=150)
    f_name=Entry(upd, font=("Bahnschrift",14), bg="#A3C9F9", textvariable=fn_var)
    f_name.place(x=520, y=150, width=300)

    Label(upd, text="Lastname", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=200)
    l_name=Entry(upd, font=("Bahnschrift",14), bg="#A3C9F9", textvariable=l_var)
    l_name.place(x=520, y=200, width=300)

    Label(upd, text="Account type", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=250)
    acc_type.set("Savings account")
    r1 = Radiobutton(upd, text="Savings account", variable=acc_type, value="Savings account", font=("Bahnschrift", 12), bg="#C2E1FF")
    r2 = Radiobutton(upd, text="Current account", variable=acc_type, value="Current account", font=("Bahnschrift", 12), bg="#C2E1FF")
    r1.place(x=520, y=250)
    r2.place(x=680, y=250)

    Label(upd, text="Initial amount", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=300)
    amount=Entry(upd, font=("Bahnschrift",14), bg="#A3C9F9", textvariable=amnt_var)
    amount.place(x=520, y=300, width=300)

    Label(upd, text="Phone number", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=350)
    ph_num=Entry(upd, font=("Bahnschrift",14), bg="#A3C9F9", textvariable=ph_var)
    ph_num.place(x=520, y=350, width=300)

    Label(upd, text="Gender", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=400)
    gender.set("Male")
    rb1 = Radiobutton(upd, text="Male", variable=gender, value="Male", font=("Bahnschrift", 12), bg="#C2E1FF")
    rb2 = Radiobutton(upd, text="Female", variable=gender, value="Female", font=("Bahnschrift", 12), bg="#C2E1FF")
    rb3 = Radiobutton(upd, text="Other", variable=gender, value="Other", font=("Bahnschrift", 12), bg="#C2E1FF")
    rb1.place(x=520, y=400)
    rb2.place(x=600, y=400)
    rb3.place(x=700, y=400)

    Label(upd, text="Date of birth", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=450)
    dob=Entry(upd, font=("Bahnschrift",14), bg="#A3C9F9", textvariable=dob_var)
    dob.place(x=520, y=450, width=300)

    Label(upd, text="Email", font=("Bahnschrift",14), bg="#C2E1FF").place(x=320, y=500)
    mail=Entry(upd, font=("Bahnschrift",14), bg="#A3C9F9", textvariable=mail_var)
    mail.place(x=520, y=500, width=300)

    def update():
        accnum=acc_num.get()
        fname=f_name.get()
        lname=l_name.get()
        acctype=acc_type.get()
        phnum=ph_num.get()
        gendr=gender.get()
        do_b=dob.get()
        email=mail.get()
        iamount=amount.get()
        udata=(fname, lname, acctype, phnum, gendr, do_b, email, iamount, accnum)
        try:
            con = get_connection()
            cur = con.cursor()
            qry="UPDATE accinfo SET fname=?, lname=?, acctype=?, phnum=?, gendr=?, do_b=?, email=?, iamount=? where accnum=?"
            cur.execute(qry,udata)
            con.commit()
            con.close()
            messagebox.showinfo("Success","Updated successfully", parent=upd)
        except Exception as e:
            print("Update Error❌:", e)
            messagebox.showerror("Error","Failed to update account", parent=upd)

    update_btn=Button(upd, text="Update", font=("Bahnschrift",14), bg="#040616", fg="#E6F0FA", command=update)
    update_btn.place(x=480, y=560, width=200, height=32)

    return upd