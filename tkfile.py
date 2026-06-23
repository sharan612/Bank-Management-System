from tkinter import *
from tkinter import ttk

# Create main window
root = Tk()
root.title("Basic Treeview Example")
root.geometry("600x300")
# style = ttk.Style()
# style.configure("Treeview", 
#                 background="#f1d7d7", 
#                 foreground="black", 
#                 rowheight=25, 
#                 fieldbackground="#f5d9d9",
#                 font=("Helvetica", 10))

# style.map('Treeview', background=[('selected', "#3C9DBB")])

# Create Treeview widget
tree = ttk.Treeview(root)

# Define columns
tree['columns'] = ("ID", "Name", "Balance")

yscroll = Scrollbar(root, orient=VERTICAL, command=tree.yview)
yscroll.pack(side=RIGHT, fill=Y)
tree.configure(yscrollcommand=yscroll.set)

# Format columns
tree.column("#0", width=0, stretch=NO)  # Ghost column
tree.column("ID", anchor=CENTER, width=100)
tree.column("Name", anchor=W, width=200)
tree.column("Balance", anchor=E, width=100)

# Create headings
tree.heading("#0", text="", anchor=W)
tree.heading("ID", text="Account No", anchor=CENTER)
tree.heading("Name", text="Name", anchor=W)
tree.heading("Balance", text="Balance", anchor=E)

# Insert dummy data
tree.insert("", END, values=("1001", "Gursharan Kaur", "₹12,000"), tags=("oddrow",))
tree.insert("", END, values=("1002", "Simran Gill", "₹15,500"), tags=("evenrow",))
tree.insert("", END, values=("1003", "Navdeep Singh", "₹7,800"), tags=("oddrow",))

tree.tag_configure("oddrow", background="#f1d7d7")
tree.tag_configure("evenrow", background="lightblue")


# Pack Treeview
tree.pack(pady=20)

# Run app
root.mainloop()
