

# https://www.linkedin.com/in/akshat-saxena-509225195/
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from cv2 import cv2
import webbrowser

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

        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student Details",cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        left_frame.place(x=10,y=10,width=630,height = 540)

        b4_1 = Button(left_frame,text="Contact",command =self.callback,cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        b4_1.place(x=10,y = 100,width=135 , height = 20)
        
    def callback(url="https://www.linkedin.com/in/akshat-saxena-509225195/"):
        webbrowser.open_new_tab(url)





if __name__=="__main__":
    root=Tk()
    obj = Developer(root)
    root.mainloop()