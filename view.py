from tkinter import *
from connections import get_connection
from tkinter import messagebox
# view=Tk()
# view.title("view")
# view.state("zoomed")
 
def view_acc(parent):
    view_frame=Frame(parent, width=1115, height=650, bg="#C2E1FF")
    view_frame.place(x=0, y=0)

    Label(view_frame, text="VIEW ACCOUNT", font=("Bahnschrift",22, "bold"), fg="#070920", bg="#C2E1FF").place(relx=0.5, y=10, anchor="n")

    def fetch_account():
        acc_num = acc_entry.get()
        if not acc_num:
            messagebox.showwarning("Empty", "Please enter an account number.", parent=viewacc)
            return
        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("SELECT fname, acctype, email, phnum, do_b, gendr, iamount FROM accinfo WHERE accnum = ?", (acc_num,))
            row = cur.fetchone()
            if row:
                name_val.config(text=row[0])
                acctype_val.config(text=row[1])
                email_val.config(text=row[2])
                phone_val.config(text=row[3])
                dob_val.config(text=row[4])
                gndr_val.config(text=row[5])
                balance_val.config(text=row[6])
            else:
                messagebox.showwarning("Not Found", "No account found with this account number.", parent=viewacc)
                reset_fields()
            con.close()
        except Exception as e:
            print("Database Error:", e)

    Label(view_frame, text="Enter Account Number", font=("Bahnschrift", 14), fg="#070920", bg="#C2E1FF").place(x=290, y=119)
    acc_entry = Entry(view_frame, font=("Bahnschrift", 14), bg="#86BBFC")
    acc_entry.place(x=500, y=120, width=225)

    Button(view_frame, text="Search", font=("Bahnschrift", 12), bg="#070920", fg="#C2E1FF", command=fetch_account).place(x=730, y=120, height=26, width=100)

    viewacc=LabelFrame(view_frame, width=570, height=380, bg="#A3C9F9")
    viewacc.place(relx=0.5, y=170, anchor="n")

    Label(viewacc, text="Name : ", font=("Helvetica",15, "bold"), fg="#070920", bg="#A3C9F9").place(x=25, y=20)
    name_val = Label(viewacc, font=("Bahnschrift", 14), bg="#A3C9F9", fg="#070920")
    name_val.place(x=200, y=20)

    Label(viewacc, text="Account type : ", font=("Helvetica",15, "bold"), fg="#070920", bg="#A3C9F9").place(x=25, y=70)
    acctype_val = Label(viewacc, font=("Bahnschrift", 14), bg="#A3C9F9", fg="#070920")
    acctype_val.place(x=200, y=70)

    Label(viewacc, text="Email : ", font=("Helvetica",15, "bold"), fg="#070920", bg="#A3C9F9").place(x=25, y=120)
    email_val = Label(viewacc, font=("Bahnschrift", 14), bg="#A3C9F9", fg="#070920")
    email_val.place(x=200, y=120)

    Label(viewacc, text="Phone Number : ", font=("Helvetica",15, "bold"), fg="#070920", bg="#A3C9F9").place(x=25, y=170)
    phone_val = Label(viewacc, font=("Bahnschrift", 14), bg="#A3C9F9", fg="#070920")
    phone_val.place(x=200, y=170)

    Label(viewacc, text="Date of birth : ", font=("Helvetica",15, "bold"), fg="#070920", bg="#A3C9F9").place(x=25, y=220)
    dob_val = Label(viewacc, font=("Bahnschrift", 14), bg="#A3C9F9", fg="#070920")
    dob_val.place(x=200, y=220)

    Label(viewacc, text="Gender : ", font=("Helvetica",15, "bold"), fg="#070920", bg="#A3C9F9").place(x=25, y=270)
    gndr_val = Label(viewacc, font=("Bahnschrift", 14), bg="#A3C9F9", fg="#070920")
    gndr_val.place(x=200, y=270)

    Label(viewacc, text="Balance : ", font=("Helvetica",15, "bold"), fg="#070920", bg="#A3C9F9").place(x=25, y=320)
    balance_val = Label(viewacc, font=("Bahnschrift", 14), bg="#A3C9F9", fg="#070920")
    balance_val.place(x=200, y=320)

    def reset_fields():
        acc_entry.delete(0, END)
        name_val.config(text="")
        acctype_val.config(text="")
        email_val.config(text="")
        phone_val.config(text="")
        dob_val.config(text="")
        gndr_val.config(text="")
        balance_val.config(text="")

    Button(view_frame, text="Reset", font=("Bahnschrift", 12), command=reset_fields).place(x=350, y=650)