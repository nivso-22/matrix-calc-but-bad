from tkinter import Image, Label
import tkinter
from PIL import ImageTk, Image
from customtkinter import *

def show_about():
    about = CTk()
    Label(about, text="""About
its like the matrix calculator website, but bad"""). pack()
    about.mainloop()

def show_instructions():
    about = CTk()
    Label(about, text="""put the numbers in matrices and the shit"""). pack()
    about.mainloop()
def screen():
    root1 = CTk()
    img = ImageTk.PhotoImage(Image.open("matrix_pic.jpg"))
    CTkLabel(root1,text="", image=img).pack()

    bottom= CTkFrame(root1)
    CTkButton(bottom, text="", image=ImageTk.PhotoImage(Image.open("i_con.png").resize((25,25))), width=5, command=show_about).grid(row=0, column=0, sticky="e")
    CTkLabel(bottom, text="matrix \n calculator", font=(('arial', 24))).grid(row=0, column=1)
    CTkButton(bottom, text="", image=ImageTk.PhotoImage(Image.open("document.png").resize((25,25))), width=5, command=show_instructions).grid(row=0, column=2, sticky="w")

    bottom.pack()

    CTkButton(root1, text="->", command=root1.destroy).pack()

    root1.mainloop()