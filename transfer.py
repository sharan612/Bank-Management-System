from tkinter import *
from tkinter import messagebox
from connections import get_connection
# tr_bal=Tk()
# tr_bal.title("transfer balance")
# tr_bal.state("zoomed")
 
def tr_bal(parent):
    tr_bal=Frame(parent, width=1115, height=650, bg="#C2E1FF")
    tr_bal.place(x=0, y=0)

    Label(tr_bal, text="TRANSFER BALANCE", font=("Bahnschrift",22, "bold"), fg="#070920", bg="#C2E1FF").place(relx=0.5, y=10, anchor="n")

    transfr=LabelFrame(tr_bal, width=570, height=350, bg="#A3C9F9")
    transfr.place(relx=0.5, y=140, anchor="n")

    Label(transfr, text="Sender Acc Number", font=("Helvetica",14, "bold"), bg="#A3C9F9").place(x=25, y=35)
    sender_entry = Entry(transfr, font=("Bahnschrift",14), bg="#86BBFC")
    sender_entry.place(x=245, y=35, width=300)

    Label(transfr, text="Receiver Acc Number", font=("Helvetica",14, "bold"), bg="#A3C9F9").place(x=25, y=85)
    receiver_entry = Entry(transfr, font=("Bahnschrift",14), bg="#86BBFC")
    receiver_entry.place(x=245, y=85, width=300)

    Label(transfr, text="Amount to Transfer", font=("Helvetica",14, "bold"), bg="#A3C9F9").place(x=25, y=135)
    amount_entry = Entry(transfr, font=("Bahnschrift",14), bg="#86BBFC")
    amount_entry.place(x=245, y=135, width=300)

    def transfer_amount():
        sender = sender_entry.get()
        receiver = receiver_entry.get()
        amount = amount_entry.get()
        if not (sender and receiver and amount):
            messagebox.showerror("Input Error", "All fields are required", parent=transfr)
            return
        try:
            amount = float(amount)
        except:
            messagebox.showerror("Amount Error", "Amount must be a number", parent=transfr)
            return
        try:
            con = get_connection()
            cur = con.cursor()
            cur.execute("SELECT iamount FROM accinfo WHERE accnum=?", (sender,))
            sender_data = cur.fetchone()
            if not sender_data:
                messagebox.showerror("Error", "Sender account not found", parent=transfr)
                return
            if sender == receiver:
                messagebox.showerror("Error", "Cannot transfer to same account", parent=transfr)
                return
            if sender_data[0] < amount:
                messagebox.showerror("Error", "Insufficient balance", parent=transfr)
                return
            cur.execute("SELECT * FROM accinfo WHERE accnum=?", (receiver,))
            if not cur.fetchone():
                messagebox.showerror("Error", "Receiver account not found", parent=transfr)
                return
            # Perform transfer
            cur.execute("UPDATE accinfo SET iamount = iamount - ? WHERE accnum=?", (amount, sender))
            cur.execute("UPDATE accinfo SET iamount = iamount + ? WHERE accnum=?", (amount, receiver))
            con.commit()
            messagebox.showinfo("Success", "Amount transferred successfully", parent=transfr)
            sender_entry.delete(0, END)
            receiver_entry.delete(0, END)
            amount_entry.delete(0, END)
        except Exception as e:
            print("Transfer Error:", e)
            messagebox.showerror("Error", "Something went wrong", parent=transfr)
        finally:
            if con:
                con.close()

    Button(transfr, text="Transfer", font=("Bahnschrift",13), bg="#040616", fg="#E6F0FA", command=transfer_amount).place(x=250, y=230, width=160, height=30)