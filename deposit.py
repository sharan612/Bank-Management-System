from tkinter import *
from tkinter import messagebox
from connections import get_connection
# dep=Tk()
# dep.title("deposiit balance")
# dep.state("zoomed")
 
def dep_bal(parent):
    dep_frame=Frame(parent, width=1115, height=650, bg="#C2E1FF")
    dep_frame.place(x=0, y=0)

    Label(dep_frame, text="DEPOSIT BALANCE", font=("Bahnschrift",22, "bold"), fg="#070920", bg="#C2E1FF").place(relx=0.5, y=10, anchor="n")

    depbal=LabelFrame(dep_frame, width=570, height=380, bg="#A3C9F9")
    depbal.place(relx=0.5, y=140, anchor="n")

    Label(depbal, text="Account number", font=("Helvetica",15, "bold"), bg="#A3C9F9").place(x=25, y=35)
    acc_entry=Entry(depbal, font=("Bahnschrift",14), bg="#86BBFC")
    acc_entry.place(x=200, y=35, width=300)

    cbal_var = StringVar()
    Label(depbal, text="Current Balance", font=("Helvetica",15, "bold"), bg="#A3C9F9").place(x=25, y=85)
    Entry(depbal, font=("Bahnschrift",14), bg="#86BBFC", textvariable=cbal_var).place(x=200, y=85, width=300)

    Label(depbal, text="Amount", font=("Helvetica",15, "bold"), bg="#A3C9F9").place(x=25, y=135)
    amt_entry=Entry(depbal, font=("Bahnschrift",14), bg="#86BBFC")
    amt_entry.place(x=200, y=135, width=300)

    ubal_var=StringVar()
    Label(depbal, text="Updated Balance", font=("Helvetica",15, "bold"), bg="#A3C9F9").place(x=25, y=185)
    Entry(depbal, font=("Bahnschrift",14), bg="#86BBFC", textvariable=ubal_var).place(x=200, y=185, width=300)

    def fetch_balance():
        accno = acc_entry.get()
        if not accno:
            messagebox.showwarning("Missing", "Enter account number", parent=depbal)
            return
        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("SELECT iamount FROM accinfo WHERE accnum=?", (accno,))
            row = cur.fetchone()
            con.close()
            if row:
                cbal_var.set(f"{row[0]}")
            else:
                messagebox.showerror("Not Found", "Account not found", parent=depbal)
        except Exception as e:
            print("Fetch Error ❌:", e)

    Button(depbal, text="Submit", font=("Bahnschrift",13), bg="#040616", fg="#E6F0FA", command=fetch_balance).place(x=230, y=235, width=160, height=30)

    def deposit_amount():
        accno = acc_entry.get()
        amount = amt_entry.get()
        try:
            amt = float(amount)
            if amt <= 0:
                raise ValueError
        except:
            messagebox.showerror("Invalid", "Enter a valid positive amount", parent=depbal)
            return

        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("SELECT iamount FROM accinfo WHERE accnum=?", (accno,))
            row = cur.fetchone()
            if not row:
                messagebox.showerror("Error", "Account not found", parent=depbal)
                return
            new_balance = row[0] + amt
            cur.execute("UPDATE accinfo SET iamount=? WHERE accnum=?", (new_balance, accno))
            con.commit()
            con.close()
            messagebox.showinfo("Success", f"₹{amt} deposited successfully", parent=depbal)
            ubal_var.set(str(new_balance))
            cbal_var.set(str(new_balance))
        except Exception as e:
            print("Deposit Error ❌:", e)

    Button(depbal, text="Deposit", font=("Bahnschrift",13), bg="#040616", fg="#E6F0FA", command=deposit_amount).place(x=230, y=285, width=160, height=30)