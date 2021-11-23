from ttkthemes import ThemedStyle
from tkinter import messagebox


def center_window(win):
    win.update_idletasks()

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    return x, y


def window_style(top, title, geometry):
    top.title(title)
    top.geometry(geometry)
    top.resizable(width=False, height=False)
    w, h = center_window(top)
    top.geometry("+%d+%d" % (w, h))
    # ttk theme:
    style = ThemedStyle(top)
    style.set_theme('clam')


def main_theme_color():
    return '#040404'


def instance_error(instance):
    messagebox.showerror("Error", f"Please insert a {instance}")

def range_error(min, max):
    messagebox.showerror("Error", f"The allowed range is: {min} - {max}")

def empty_error():
    messagebox.showerror("Error", "Please fill all the fields.")

def empty_database_error(action):
    messagebox.showerror("Error", f"There are no templates to {action}.")

def confirmation_message():
    return messagebox.askyesno("Are you sure?", "Are you sure?")

