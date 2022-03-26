from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.geometry("700x700")
root.title("Credit Card")
root.config(background = "#FAF0CA")

ccimage = ImageTk.PhotoImage(Image.open("Credit Card.jpg"))

PinCode = Entry(root, background = "#FAF0CA", foreground="#0D3B66", font=("Comic Sans MS", "10", "bold"))
PinCode.place(relx=0.5, rely=0.4, anchor=CENTER)

image = Label(root, image=ccimage)
image.place(relx=0.5, rely=0.6, anchor=CENTER)

def auth():
    inputget = PinCode.get()
    print(inputget)
    inputtype = type(inputget)
    print(inputtype)
    try:
        integer = int(inputget)
        integertype = type(integer)
    except:
        messagebox.showinfo("Error", "Invalid Password")
    print(integertype)
    if integertype == int:
        messagebox.showinfo("Accepted", "Valid Password")
    if inputtype == str:
        messagebox.showinfo("Error", "Invalid Password")
btn = Button(root, text="Enter", background = "#FAF0CA", foreground="#0D3B66", font=("Comic Sans MS", "10", "bold"), command=auth)
btn.place(relx=0.46, rely=0.75)
root.mainloop()