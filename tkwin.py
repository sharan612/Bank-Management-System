from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
win=Tk()
win.geometry("800x600") # small window size
win.title("Python Program") # window title
win.state("zoomed") # full screen window
win.config(bg="light cyan") #background window color

# BG IMAGE
bg=Image.open("images/login.jpg") 
bg=bg.resize((1400,750))
bg=ImageTk.PhotoImage(bg)
bglabel=Label(win,image=bg)
bglabel.place(x=0,y=0,relwidth=1, relheight=1)

# FRAME
# f = Frame(win, bg="sky")
# f.place(x=80, y=50)

# LABELFRAME for login section
lf = LabelFrame(win, text="Enter Details", bg="LightSkyBlue1", font=("Arial", 12),height=620,width=550)
lf.place(x=400, y=60)

# BG IMAGE in frame
img=Image.open("images/OIP.webp")
img=img.resize((50,50))
img=ImageTk.PhotoImage(img)
label=Label(win,image=img)
label.place(x=10,y=10)

# HEADING
heading=Label(lf, text="Login Form",font=('SimSun',18),bg="brown3",fg="white")
heading.place(x=200,y=10)

# USERNAME
username=Label(lf,text="Username",font=('Arial',15),bg="LightSkyBlue1") 
username.place(x=100,y=50)
uentry=Entry(lf,font=("Arial",15))
uentry.place(x=200,y=50)

# PASSWORD
password=Label(lf,text="Password",font=("Arial",15),bg="LightSkyBlue1") 
password.place(x=100,y=80)
pentry=Entry(lf,font=("Arial",15))
pentry.place(x=200,y=80)

# CHECKBUTTON
# check=IntVar() (win, text="show password", variable=check,font=(10), bg="lightblue")
check = Checkbutton(lf, text="show password",font=(10), bg="LightSkyBlue2")
check.place(x=220,y=110)

# RADIOBUTTONS
gender = Label(lf, text="Gender", font=("Arial", 13),bg="LightSkyBlue1")
gender.place(x=100, y=150)
gender = StringVar()
gender.set("Male")  # default value
r1 = Radiobutton(lf, text="Male", variable=gender, value="Male", bg="light cyan", font=("Arial", 10))
r2 = Radiobutton(lf, text="Female", variable=gender, value="Female", bg="light cyan", font=("Arial", 10))
r3 = Radiobutton(lf, text="Other", variable=gender, value="Other", bg="light cyan", font=("Arial", 10))
r1.place(x=200, y=150)
r2.place(x=270, y=150)
r3.place(x=360, y=150)

# SPINBOX
age = Label(lf, text="Age", font=("Arial", 13),bg="LightSkyBlue1")
age.place(x=100, y=190)
age_spin = Spinbox(lf, from_=14, to=100, font=("Arial", 12), width=5)
age_spin.place(x=200, y=190)  

# OPTIONMENU
course = Label(lf, text="Course", font=("Arial", 13),bg="LightSkyBlue1")
course.place(x=100, y=230)
course_var = StringVar()
course_var.set("Select Course")  # default option
course_options = ["Python", "Java", "C++", "Web Dev", "AI/ML","ReactJS"]
course_menu = OptionMenu(lf, course_var, *course_options) 
course_menu.config(font=("Arial", 12))
course_menu.place(x=200, y=230)

# TEXTBOX
feedback = Label(lf, text="Feedback", font=("Arial", 13),bg="LightSkyBlue1")
feedback.place(x=100, y=270)
feedback_text = Text(lf, height=2, width=30, font=("Arial", 10))
feedback_text.place(x=200, y=270)

# SCALE
scale = Label(lf, text="Rating", font=("Arial",13),bg="LightSkyBlue1") 
scale.place(x=100,y=320)
scale = Scale(lf, from_=0, to=10, orient=HORIZONTAL)
scale.place(x=200,y=310)

# LISTBOX
listbox=Label(lf,text="Listbox",font=("Arial",13),bg="LightSkyBlue1")
listbox.place(x=100,y=355)
lb = Listbox(lf,height=5)
lb.insert(1, "C")
lb.insert(2, "C++")
lb.insert(3, "Python")
lb.insert(4, "Java")
lb.insert(5,"html")
lb.place(x=200,y=355)

# CANVAS
canvas = Canvas(win, width=200, height=100)
canvas.place(x=1000, y=60)
canvas.create_rectangle(50, 20, 150, 80, fill="skyblue")

#COMBOBOX
combobox=Label(lf,text="Combobox",font=("Arial",13),bg="LightSkyBlue1")
combobox.place(x=100,y=450)
combo = ttk.Combobox(lf, values=["SC", "Gen", "OBC"])
combo.place(x=200, y=450)

#TREEVIEW
tree = ttk.Treeview(win, columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.place(x=960, y=180)

# MESSAGE
msg = Message(lf, text="Please fill all fields before logging in.", width=300, bg="LightSkyBlue2", font=("Arial", 11))
msg.place(x=170, y=520) #multiline without width mentioned,single line with width

# BUTTON
loginbtn=Button(lf,text="LOGIN",font=("Arial",15,'bold'),bg="red",fg="white")
loginbtn.place(x=250,y=550)


win.mainloop()