from tkinter import *
from PIL import ImageTk, Image
import gui_utilities
from program import Program

def main():
  root = Tk()
  gui_utilities.Window_Style(root, "Tarkov Mouse Speed Templates", "954x612")

  image = Image.open('logos/logo.jpg')
  image.thumbnail((950, 950))
  resized_image = ImageTk.PhotoImage(image)
  img_label = Label(root, image=resized_image, bg=gui_utilities.Main_Theme_Color())
  img_label.grid(row=0, column=0, rowspan=4, columnspan=4)

  Program(root)

  root.mainloop()
 
if __name__ == '__main__':
  main()
