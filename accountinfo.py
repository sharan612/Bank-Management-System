from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connections import get_connection
from update import update_acc
# info=Tk()
# info.title("acc info")
# info.state("zoomed")
 
tree = None

def account_info(parent):
    global tree

    acc_info=Frame(parent, width=1115, height=650, bg="#C2E1FF")
    acc_info.place(x=0, y=0)

    style=ttk.Style()
    style.theme_use("alt")

    Label(acc_info, text="ACCOUNT INFO", font=("Bahnschrift",22, "bold"), fg="#070920", bg="#C2E1FF").place(relx=0.5, y=10, anchor="n")
        
    cols = ("Account number", "Firstname", "Lastname", "Account type", "Phone number", "Gender", "Date of birth", "Email", "Initial amount")
    tree = ttk.Treeview(acc_info, columns=cols, show="headings", height=20, style="Treeview")
    for col in cols:
        tree.heading(col, text=col)
        # tree.column(col, width=100, anchor=CENTER)
    tree.place(x=5, y=120, width=1105, height=400)

    tree.column("Account number", anchor=CENTER, width=120)
    tree.column("Firstname", anchor=CENTER, width=150)
    tree.column("Lastname", anchor=CENTER, width=100)
    tree.column("Account type", anchor=CENTER, width=140)
    tree.column("Phone number", anchor=CENTER, width=120)
    tree.column("Gender", anchor=CENTER, width=80)
    tree.column("Date of birth", anchor=CENTER, width=120)
    tree.column("Email", anchor=CENTER, width=180)
    tree.column("Initial amount", anchor=CENTER, width=100)

    def populate_tree():
            global tree
            tree.delete(*tree.get_children())
            try:
                con = get_connection()
                cur = con.cursor()
                qy="select accnum, fname, lname, acctype, phnum, gendr, do_b, email, iamount FROM accinfo"
                result=cur.execute(qy)
                for row in result:
                    tree.insert("", END, iid=row[0], values=row)
                con.close()
            except Exception as e:
                    print("Error fetching data:", e)
    populate_tree()

    def search_tree():
        query = search_entry.get().lower()
        matches = []
        for row in tree.get_children():
            values = tree.item(row)['values']
            if any(query in str(v).lower() for v in values):
                matches.append(values)
        tree.delete(*tree.get_children())
        for row in matches:
            tree.insert("", END, values=row)
        if not matches:
            messagebox.showinfo("Not Found", "No match found", parent=acc_info)

    Label(acc_info, text="Search:", font=("Bahnschrift", 14, "bold"), fg="#07101A", bg="#C2E1FF").place(x=305, y=67)

    search_entry = Entry(acc_info, font=("Bahnschrift", 12), bg="#A3C9F9")
    search_entry.place(x=400, y=70, width=250, height=25)

    search_btn = Button(acc_info, text="Search", font=("Bahnschrift", 11), bg="#07101A", fg="#D3E5FA", command=search_tree)
    search_btn.place(x=670, y=70, width=100, height=25)

    def reset_treeview():
        populate_tree()

    reset_btn = Button(acc_info, text="Reset", font=("Bahnschrift", 11), bg="#07101A", fg="#D3E5FA", command=reset_treeview)
    reset_btn.place(x=780, y=70, width=100, height=25)

    def edit(parent):
        select_acc= tree.focus()
        if not select_acc:
            messagebox.showwarning("Select Row", "Please select a row to edit.", parent=acc_info)
            return
        row = tree.item(select_acc, "values")
        acc_info.destroy()
        update_acc(parent, row)

    edit_btn=Button(acc_info, text="Edit Customer", font=("Bahnschrift", 12), bg="#07101A", fg="#D3E5FA", command=lambda:edit(parent))
    edit_btn.place(x=370, y=550, height=30, width=170)

    def del_acc():
        selected = tree.focus()
        if selected:
            try:
                con = get_connection()
                cur = con.cursor()
                query="DELETE FROM accinfo where accnum=?"
                cur.execute(query, (selected,))
                con.commit()
                con.close()
                messagebox.showinfo("Deleted","Deleted Successfully", parent=acc_info)
                populate_tree()
            except Exception as e:
                print(e)
                messagebox.showerror("Error","Unable to delete", parent=acc_info)
        else:
            messagebox.showwarning("No selection","Please select a customer to delete", parent=acc_info)
    
    del_btn=Button(acc_info, text="Delete Customer", font=("Bahnschrift", 12), bg="#07101A", fg="#D3E5FA", command=del_acc)
    del_btn.place(x=560, y=550, height=30, width=180)

def insert_data(data):
    global tree     
    if tree:
        tree.insert("", "end", values=data)