from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from cv2 import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Credits")
        
        #bg image.
        img2 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\black.jpg")
        img2 = img2.resize((1366,768)) #resize and converting high level img to low level img.
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root,image = self.photoimg2)
        bg_img.place(x=0,y=0,width = 1366, height = 768)

        main_frame = Frame(bg_img)
        main_frame.place(x=38,y=20,width=1280,height = 650)

        img3 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\Coder.png")
        img3 = img3.resize((1280,650)) #resize and converting high level img to low level img.
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img2 = Label(main_frame,image = self.photoimg3)
        bg_img2.place(x=0,y=0,width = 1280, height = 650)






if __name__=="__main__":
    root=Tk()
    obj = Developer(root)
    root.mainloop()