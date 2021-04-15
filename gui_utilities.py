from ttkthemes import ThemedStyle
from tkinter import messagebox


def Center_Window(win):
    win.update_idletasks()

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    return x, y


def Window_Style(top, title, geometry):
    top.title(title)
    top.geometry(geometry)
    top.resizable(width=False, height=False)
    w, h = Center_Window(top)
    top.geometry("+%d+%d" % (w, h))
    # ttk theme:
    style = ThemedStyle(top)
    style.set_theme('clam')


def Main_Theme_Color():
    return '#040404'


def Instance_Error(instance):
    messagebox.showerror("Error", f"Please insert a {instance}")

def Range_Error(min, max):
    messagebox.showerror("Error", f"The allowed range is: {min} - {max}")

def Empty_Error():
    messagebox.showerror("Error", "Please fill all the fields.")

def Empty_Database_Error(action):
    messagebox.showerror("Error", f"There are no templates to {action}.")

def Confirmation_Message():
    return messagebox.askyesno("Are you sure?", "Are you sure?")

