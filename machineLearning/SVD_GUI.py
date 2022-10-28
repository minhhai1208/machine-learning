from tkinter import *
from tkinter import filedialog as fdl
from tkinter.messagebox import showerror
from skimage import img_as_ubyte
import imageio as imageio
import numpy as np
from PIL import Image, ImageTk
from svd import *
from tkinter import filedialog

root = Tk()
root.title('SVD')
root.state('zoomed')
root.resizable()
root.configure(background='black')

# Declare
fb = Button()
rb = Button()

# get screen size
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# boder
boder_x = 25
boder_y = 20

# build frame
frame_width = screen_width/2-boder_x*6
frame_height = screen_height-60
bt_size = int(frame_width/3)


# Left frame
left_frame = Frame(root, bg='gray')
left_frame.place(height=frame_height, width=frame_width, x=boder_x, y=boder_y)


# Right frame
right_frame = Frame(root, bg='white')
right_frame.place(height=frame_height, width=frame_width, x=screen_width-(frame_width+boder_x), y=boder_y)

zoom_frame = Frame()

# Close symbol
cl_symbol = Image.open("C:\\Users\\user\\Downloads\\Project 1\\picture/download.png")
cl_symbol = cl_symbol.resize((20, 20))
cl_symbol = ImageTk.PhotoImage(cl_symbol)
cl_button = Button(left_frame, image=cl_symbol, height=20, width=20, relief=SUNKEN, command=lambda: close_file())
cl_button.place(relx=1, x=-2, y=2, anchor=NE)

lst = []
a = 1
count = -1
# Option frame
def state(choice):
    if value_inside.get() in option_lists:
        textbox.config(state=NORMAL)



option_frame = Frame(root, height=250, width=150)


option_frame.pack(side=BOTTOM)
option_lists = ["RANK", "ERROR"]
value_inside = StringVar()
value_inside.set("Approximation image")
question_menu = OptionMenu(option_frame, value_inside, *option_lists, command=state)
question_menu.pack()


# Text box
text_value = StringVar()
textbox = Entry(option_frame, width=len("Approximation image")+10, state=DISABLED, textvariable=text_value)

textbox.pack(pady=5)


# Submit button
submit_button = Button(option_frame, text="Submit", command=lambda: check_error())
submit_button.pack(pady=10)

save_button = Button(option_frame,text="Save",command=lambda : save())
save_button.pack(pady=10)

def left_upload_file():
    global raw_img, l_photo, l_img, lb

    f_type = [('JPG Files', '*.jpg'), ('PNG Files', '*.png')]
    filename = fdl.askopenfilename(
            title='Open a file',
            filetypes=f_type
        )
    if filename is not None:
        lf_button.pack_forget()
    raw_img = Image.open(filename)
    raw_img = raw_img.convert('L')

    l_img = resize(raw_img, left_frame.winfo_width(), left_frame.winfo_height())
    l_photo = ImageTk.PhotoImage(l_img)

    print("----------------------------------------------------------")
    print("File link:", filename)

    lb = Button(left_frame, image=l_photo, command=lambda: zoom_in(l_img))
    lb.pack(expand=True, side=TOP)


def right_upload_file(img=None):
    global r_photo, r_img, rb
    rb.pack_forget()
    rf_button.pack_forget()
    r_img = resize(img, right_frame.winfo_width(), right_frame.winfo_height())
    r_photo = ImageTk.PhotoImage(r_img)
    rb = Button(right_frame, image=r_photo, command=lambda: zoom_in(r_img))
    rb.pack(expand=True, side=TOP)


def check_error():
    global l_photo, l_img , count

    if l_photo is None:
        showerror(title="Error", message="Image not found")
    else:
        t = 0
        try:
            value = int(textbox.get())
            app_matrix = None
            if value < 0:
                t = 1
                showerror(title="Error", message="Positive Integer request")
            elif value_inside.get() == "RANK":
                t = 2
                app_matrix = svd_rank(value, l_img, square=False)
            else:
                t = 3
                if value < 0 or value > 100:
                    showerror(title="Error", message="Range: 0 -> 100 percent")

                app_matrix = svd_error(value, l_img, square=False)
        except:
            if t == 1:
                print("Error: value < 0")
            elif t == 2:
                print("Error: rank option")
            else:
                print("Error: error option ")

            showerror(title="Error", message="Positive Integer request")

        print(app_matrix)


        app_image = Image.fromarray(app_matrix.real)
        matrx = matrix(app_image)
        lst.append(matrx)

        print("Check:")
        for i in range(0, len(lst)):
            print(i)
            print(lst[i].get_matrix())
        right_upload_file(app_image)

class matrix:
    def __init__(self,matrix):
        self.matrix = matrix

    def print(self):
        print(self.matrix)

    def get_matrix(self):
        return self.matrix

def save():
    global count
    toSave = fdl.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),('PNG', '*.png'),('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))
    # Image.open(r_img).save(toSave)
    imageio.imwrite(toSave + ".jpeg", (lst[count].get_matrix()))
    # app_image.save(toSave + ".jpeg")




# Close left image
def close_file():
    global rb

    lb.destroy()
    rb.destroy()
    rf_button.pack_forget()
    right_symbol()


def left_symbol():
    global l_symbol, lf_button
    l_symbol = Image.open("C:\\Users\\user\\Downloads\\Project 1\\picture/download.png")
    l_symbol = l_symbol.resize((bt_size, bt_size))
    l_symbol = ImageTk.PhotoImage(l_symbol)
    lf_button = Button(left_frame, image=l_symbol, height=bt_size, width=bt_size, relief=SUNKEN,
                       command=lambda: left_upload_file())
    lf_button.place(relx=0.5, rely=0.5, anchor=CENTER)


left_symbol()


def right_symbol():
    global r_symbol, rf_button
    r_symbol = Image.open("C:\\Users\\user\\Downloads\\Project 1\\picture/dow1.png")
    r_symbol = r_symbol.resize((bt_size, bt_size))
    r_symbol = ImageTk.PhotoImage(r_symbol)
    rf_button = Button(right_frame, image=r_symbol, height=bt_size, width=bt_size, relief=SUNKEN)
    rf_button.pack(pady=int(screen_height/3))


right_symbol()


def resize(item, fw, fh):
    if item is not None:
        lf_button.pack_forget()
    w, h = item.width, item.height
    if (h/w) > (fh/fw):
        w_resize = int(frame_height * (w / h))
        h_resize = int(frame_height)
    else:
        h_resize = int(frame_width*(h/w))
        w_resize = int(frame_width)
    item = item.resize((w_resize, h_resize))
    return item


def zoom_in(img):
    global zm_img, zoom_frame

    zoom_frame = Frame(root, bg='#252525')
    b_height, b_width = screen_height-150, screen_width-40
    zm_img = resize(img, b_width, b_height)
    zoom_frame.place(height=screen_height, width=screen_width)
    zm_img = ImageTk.PhotoImage(zm_img)
    zm_button = Button(zoom_frame, image=zm_img, command=lambda: zoom_out())
    zm_button.pack(pady=40)


def zoom_out():
    zoom_frame.destroy()


root.mainloop()


