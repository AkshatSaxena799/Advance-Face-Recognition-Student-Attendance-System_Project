from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from tkinter import messagebox
import sqlite3
from cv2 import cv2
import numpy as np
from time import strftime
from datetime import datetime
from attendance import Attendance
from developer import Developer
import webbrowser

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        img = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\black.jpg")
        img = img.resize((1366,128),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 1366, height = 138)
        
        title_lbl = Label(f_lbl, text = "ATTENDANCE SYSTEM BASED ON FACE RECOGNITION", font=("times new roman", 30, "bold"),bg="white",fg="red")
        title_lbl.place(x=25,y=25,width = 1300,height = 90)
        
        #bg image.
        img2 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\bg1.jpg")
        img2 = img2.resize((1366,640),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root,image = self.photoimg2)
        bg_img.place(x=0,y=138,width = 1366, height = 640)
        
        #student button
        img3 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\student.jpg")
        img3 = img3.resize((150,150),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(bg_img,image =self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=50,y = 100,width=125 , height = 125)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        b1_1.place(x=45,y = 230,width=135 , height = 20)

        #detect face button
        img4 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\facedetect.png")
        img4 = img4.resize((100,100),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b2 = Button(bg_img,image =self.photoimg4,cursor="hand2",command=self.face_recog)
        b2.place(x=225,y = 100,width=125 , height = 125)

        b2_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recog,font=("times new roman", 12, "bold"),bg="white",fg="red")
        b2_1.place(x=220,y = 230,width=135 , height = 20)

        #attendance button
        img5 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\attendance.png")
        img5 = img5.resize((100,100),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b3 = Button(bg_img,image =self.photoimg5,cursor="hand2",command=self.attendance_data)
        b3.place(x=400,y = 100,width=125 , height = 125)

        b3_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 12, "bold"),bg="white",fg="red")
        b3_1.place(x=395,y = 230,width=135 , height = 20)

        #help desk button
        img6 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\contact.png")
        img6 = img6.resize((100,100),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b4 = Button(bg_img,image =self.photoimg6,cursor="hand2",command=self.contact_info)
        b4.place(x=575,y = 100,width=125 , height = 125)

        b4_1 = Button(bg_img,text="Contact",cursor="hand2",command=self.contact_info,font=("times new roman", 12, "bold"),bg="white",fg="red")
        b4_1.place(x=570,y = 230,width=135 , height = 20)

        #train face button
        img7 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\traindata.png")
        img7 = img7.resize((100,100),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b5 = Button(bg_img,image =self.photoimg7,cursor="hand2",command=self.train_classifier)
        b5.place(x=750,y = 100,width=125 , height = 125)

        b5_1 = Button(bg_img,text="Train Face",cursor="hand2",command=self.train_classifier,font=("times new roman", 12, "bold"),bg="white",fg="red")
        b5_1.place(x=745,y = 230,width=135 , height = 20)

        #photos button
        img8 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\photos.jpg")
        img8 = img8.resize((100,100),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b6 = Button(bg_img,image =self.photoimg8,cursor="hand2",command=self.open_img)
        b6.place(x=925,y = 100,width=125 , height = 125)

        b6_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 12, "bold"),bg="white",fg="red")
        b6_1.place(x=920,y = 230,width=135 , height = 20)

        #Developer button
        b7_1 = Button(bg_img,text="Developed by : AKSHAT SAXENA",command= self.developer_details,cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        b7_1.place(x=50,y = 525,width=250 , height = 20)
 
    def open_img(self):
        os.startfile("data")
#training data
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #GreyScale Img
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #======Train Classifier and Save======
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

#=============Attendance===============
    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList= f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
    
#==============contact================

    def contact_info(self):
        root = Tk()
        root.geometry("1366x768+0+0")
        root.title("Contact Me")
        new = 1
        url = "https://www.linkedin.com/in/akshat-saxena-509225195/"
        url1="https://github.com/AkshatSaxena799"
        def openweb():
            webbrowser.open(url,new=new)
        def openweb1():
            webbrowser.open(url1,new=new)
        Btn = Button(root, text = "Linkedin",command=openweb)
        Btn.pack()

        Btn1 = Button(root, text = "GitHub",command=openweb1)
        Btn1.pack()
        root.mainloop()

        
        #bg image.
        img2 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\black.jpg")
        img2 = img2.resize((1366,768)) #resize and converting high level img to low level img.
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root,image = self.photoimg2)
        bg_img.place(x=0,y=0,width = 1366, height = 768)

        main_frame = Frame(bg_img)
        main_frame.place(x=38,y=20,width=1280,height = 650)

        img3 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\designer.png")
        img3 = img3.resize((1280,650)) #resize and converting high level img to low level img.
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img2 = Label(main_frame,image = self.photoimg3)
        bg_img2.place(x=0,y=0,width = 1280, height = 650)








#Face Recognization
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)
            
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=sqlite3.connect('FR.db')
                my_cursor=conn.cursor()
                my_cursor.execute('''SELECT Name FROM Student where ID=? ''',(str(id)))
                n = my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute('''SELECT Roll FROM Student where ID=? ''',(str(id)))
                r = my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute('''SELECT Department FROM Student where ID=? ''',(str(id)))
                d = my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute('''SELECT ID FROM Student where ID=? ''',(str(id)))
                i = my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]

            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            k=cv2.waitKey(30)
            if k==27:
                break
        video_cap.release()
        cv2.destroyAllWindows()






         

    #===============FUNCTIONS BUTTONS=================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    


if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()