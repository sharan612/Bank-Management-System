from tkinter import *
import time
from createacc import create_acc
from accountinfo import account_info
from view import view_acc
from deposit import dep_bal
from withdraw import wd_bal
from transfer import tr_bal
 
def dashboard(username, role):
    dash=Toplevel()
    dash.title("Dashboard")
    dash.state("zoomed")

    db_title=LabelFrame(dash, bg="#06112B", width=1370, height=60)
    db_title.place(x=0, y=0)

    Label(db_title, text=f"Welcome, {username.capitalize()}", font=("Bahnschrift",20,"bold"), bg="#06112B", fg="#E6F0FA").place(relx=0.5, y=10, anchor="n")

    sidebar=LabelFrame(dash, bg="#A3C9F9", width=250, height=650)
    sidebar.place(x=0, y=60)

    def show_page(func):
        for widget in db.winfo_children():
            widget.destroy()
        func(db)

    def logout():
        dash.destroy()

    if role == 'staff':
        Button(sidebar, text="Create account", font=("Bahnschrift",13,"bold"), bg="#06112B", fg="#E6F0FA", command=lambda: show_page(create_acc)).place(x=0, y=130, height=32, width=249)
        Button(sidebar, text="Account Info", font=("Bahnschrift",13,"bold"), bg="#06112B", fg="#E6F0FA", command=lambda: show_page(account_info)).place(x=0, y=170, height=32, width=249)
        Button(sidebar, text="Update account", font=("Bahnschrift",13,"bold"), bg="#06112B", fg="#E6F0FA").place(x=0, y=210, height=32, width=249)
        Button(sidebar, text="Logout", font=("Bahnschrift",13,"bold"), bg="#050D20", fg="#E6F0FA", command=logout).place(x=0, y=270, height=32, width=249)
    else:
        Button(sidebar, text="View Account", font=("Bahnschrift",13,"bold"), bg="#06112B", fg="#E6F0FA", command=lambda: show_page(view_acc)).place(x=0, y=120, height=32, width=249)
        Button(sidebar, text="Deposit Balance", font=("Bahnschrift",13,"bold"), bg="#06112B", fg="#E6F0FA", command=lambda: show_page(dep_bal)).place(x=0, y=160, height=32, width=249)
        Button(sidebar, text="Withdraw Balance", font=("Bahnschrift",13,"bold"), bg="#06112B", fg="#E6F0FA", command=lambda: show_page(wd_bal)).place(x=0, y=200, height=32, width=249)
        Button(sidebar, text="Transfer Balance", font=("Bahnschrift",13,"bold"), bg="#06112B", fg="#E6F0FA", command=lambda: show_page(tr_bal)).place(x=0, y=240, height=32, width=249)
        Button(sidebar, text="Logout", font=("Bahnschrift",13,"bold"), bg="#050D20", fg="#E6F0FA", command=logout).place(x=0, y=300, height=32, width=249)
        

    db=Frame(dash, bg="#C2E1FF", width=1120, height=650)
    db.place(x=249, y=60)

    card = Frame(db, bg="#06112B", bd=2, relief="groove")
    card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=200)

    def update_clock():
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%A, %d %B %Y")
        clock_label.config(text=current_time)
        date_label.config(text=current_date)
        clock_label.after(1000, update_clock)

    clock_label = Label(card, font=("Helvetica", 28, "bold"), fg="#EFEFFC", bg="#06112B")
    clock_label.pack(pady=20)
    date_label = Label(card, font=("Arial", 12,"bold"), fg="#FDE2E2", bg="#06112B")
    date_label.pack(pady=40)

    update_clock()