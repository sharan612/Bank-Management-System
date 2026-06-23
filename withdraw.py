from tkinter import *
from tkinter import messagebox
from connections import get_connection
# wd=Tk()
# wd.title("withdraw balance")
# wd.state("zoomed")
 
def wd_bal(parent):
    wd_frame=Frame(parent, width=1115, height=650, bg="#C2E1FF")
    wd_frame.place(x=0, y=0)

    Label(wd_frame, text="WITHDRAW BALANCE", font=("Bahnschrift",22, "bold"), fg="#070920", bg="#C2E1FF").place(relx=0.5, y=10, anchor="n")

    wdbal=LabelFrame(wd_frame, width=570, height=380, bg="#A3C9F9")
    wdbal.place(relx=0.5, y=140, anchor="n")

    Label(wdbal, text="Account number", font=("Helvetica",15, "bold"), bg="#A3C9F9").place(x=25, y=35)
    accentry=Entry(wdbal, font=("Bahnschrift",14), bg="#86BBFC")
    accentry.place(x=200, y=35, width=300)

    crbal_var=StringVar()
    Label(wdbal, text="Current Balance", font=("Helvetica",15, "bold"), bg="#A3C9F9").place(x=25, y=85)
    Entry(wdbal, font=("Bahnschrift",14), bg="#86BBFC", textvariable=crbal_var).place(x=200, y=85, width=300)

    Label(wdbal, text="Amount", font=("Helvetica",15, "bold"), bg="#A3C9F9").place(x=25, y=135)
    amtentry=Entry(wdbal, font=("Bahnschrift",14), bg="#86BBFC")
    amtentry.place(x=200, y=135, width=300)

    upbal_var=StringVar()
    Label(wdbal, text="Updated Balance", font=("Helvetica",15, "bold"), bg="#A3C9F9").place(x=25, y=185)
    Entry(wdbal, font=("Bahnschrift",14), bg="#86BBFC", textvariable=upbal_var).place(x=200, y=185, width=300)

    def fetch_balance():
            accno = accentry.get()
            if not accno:
                messagebox.showwarning("Missing", "Enter account number", parent=wdbal)
                return
            try:
                con = get_connection()
                cur = con.cursor()
                cur.execute("SELECT iamount FROM accinfo WHERE accnum=?", (accno,))
                row = cur.fetchone()
                con.close()
                if row:
                    crbal_var.set(f"{row[0]}")
                else:
                    messagebox.showerror("Not Found", "Account not found", parent=wdbal)
            except Exception as e:
                print("Fetch Error ❌:", e)

    Button(wdbal, text="Submit", font=("Bahnschrift",13), bg="#040616", fg="#E6F0FA", command=fetch_balance).place(x=230, y=235, width=160, height=30)

    def withdraw_amount():
        accno = accentry.get()
        amount = amtentry.get()
        try:
            amt = float(amount)
            if amt <= 0:
                raise ValueError
        except:
            messagebox.showerror("Invalid", "Enter a valid positive amount", parent=wdbal)
            return

        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("SELECT iamount FROM accinfo WHERE accnum=?", (accno,))
            row = cur.fetchone()
            if not row:
                messagebox.showerror("Error", "Account not found", parent=wdbal)
                return
            
            current_bal = row[0]
            if amt > current_bal:
                messagebox.showerror("Insufficient Funds", "Not enough balance to withdraw", parent=wdbal)
                return

            new_balance = current_bal - amt
            cur.execute("UPDATE accinfo SET iamount=? WHERE accnum=?", (new_balance, accno))
            con.commit()
            con.close()

            messagebox.showinfo("Success", f"₹{amt} withdrawn successfully", parent=wdbal)
            crbal_var.set(str(new_balance))
            upbal_var.set(str(new_balance))
        except Exception as e:
            print("Withdraw Error ❌:", e)

    Button(wdbal, text="Withdraw", font=("Bahnschrift",13), bg="#040616", fg="#E6F0FA", command=withdraw_amount).place(x=230, y=285, width=160, height=30)