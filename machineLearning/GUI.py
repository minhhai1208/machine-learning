from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.title('SVD')
root.state('zoomed')
root.resizable()
root.configure(background='black')

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
print(screen_height)
frame = Frame(root, bg='#393939')
frame.place(height=1000 , width=800,x=screen_width/2-1000/2, y=0)




cl_symbol = Image.open("C:\\Users\\user\\Downloads\\Project 1\\picture/close_image2.png")
cl_symbol = cl_symbol.resize((20, 20))
cl_symbol = ImageTk.PhotoImage(cl_symbol)
cl_button = Button(frame, image=cl_symbol, height=0, width=0, relief=SUNKEN)
cl_button.place(relx=1, x=-2, y=2, anchor=NE)

def state(choice):
    if value_inside.get() in option_lists:
        textbox.config(state=NORMAL)


option_frame = Frame(root, height=250, width=300)
option_frame.pack(expand=True)
option_lists = ["RANK","ERROR"]
value_inside = StringVar()
value_inside.set("Approximation image")
question_menu = OptionMenu(option_frame, value_inside, *option_lists, command=state)
question_menu.pack()
option_frame.grid(column=100,row=100)

# Text box
text_value = StringVar()
textbox = Entry(option_frame, width=len("Approximation image")+10, state=DISABLED, textvariable=text_value)
textbox.pack(pady=5)

submit_button = Button(option_frame, text="Submit", command=lambda: check_error())
submit_button.pack(pady=10)


mainloop()