from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.geometry("600x400")
win.title("Image in LabelFrame")

# Create a Labelframe
lf = LabelFrame(win, text="Image Section", width=300, height=200)
lf.place(x=50, y=50)

# Load the image
img = Image.open("images/login.jpg")  # Replace with your image path
img = img.resize((200, 150))  # Resize if needed
photo = ImageTk.PhotoImage(img)

# Create a Label with the image
img_label = Label(lf, image=photo)
img_label.image = photo  # Keep a reference to avoid garbage collection
img_label.place(x=20, y=20)  # Or use .pack()/.grid() as needed

win.mainloop()
