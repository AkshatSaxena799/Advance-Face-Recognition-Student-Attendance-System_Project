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
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Management System")
        
         #==========Variables==========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar() #for later uses
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        img = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\black.jpg")
        img = img.resize((1366,128),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 1366, height = 138)
        
        title_lbl = Label(f_lbl, text = "Attendance Management System", font=("times new roman", 30, "bold"),bg="white",fg="red")
        title_lbl.place(x=25,y=25,width = 1300,height = 90)
        
        #bg image.
        img2 = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\black.jpg")
        img2 = img2.resize((1366,640),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root,image = self.photoimg2)
        bg_img.place(x=0,y=130,width = 1366, height = 640)

        #main frame
        main_frame = Frame(bg_img)
        main_frame.place(x=25,y=0,width=1300,height = 560)

        #left frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student Attendance Details",cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        left_frame.place(x=10,y=10,width=630,height = 540)

        img_left = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\Attendance1.jpg")
        img_left = img_left.resize((540,80),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame,image =self.photoimg_left,cursor="hand2")
        f_lbl.place(x=10,y = 10,width=605, height = 80)

        left_inside_frame = LabelFrame(left_frame, relief=RIDGE)
        left_inside_frame.place(x=5,y=105,width=615,height = 400)

        #attendance id
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:",font=("times new roman", 12, "bold"), fg="red")
        attendanceId_label.grid(row=0,column=0,padx=10, sticky = W)

        attendanceID_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_id,font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5, sticky =W)

        #roll 

        roll_label = Label(left_inside_frame, text="Roll No:",font=("times new roman", 12, "bold"), fg="red")
        roll_label.grid(row=0,column=2,padx=10, sticky = W)

        roll_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5, sticky =W)

        #name

        name_label = Label(left_inside_frame, text="Name:",font=("times new roman", 12, "bold"), fg="red")
        name_label.grid(row=1,column=0,padx=10,pady=5, sticky = W)

        name_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font=("times new roman", 12, "bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5, sticky =W)

        #department

        dep_label = Label(left_inside_frame, text="Department:",font=("times new roman", 12, "bold"), fg="red")
        dep_label.grid(row=1,column=2, padx=10, sticky = W)
        dep_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_dep,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        dep_combo["values"]=("Select Department","Computer Science","Information Science ","Electronics","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=10, pady=5, sticky = W)

        #time

        time_label = Label(left_inside_frame, text="Time:",font=("times new roman", 12, "bold"), fg="red")
        time_label.grid(row=2,column=0,padx=10,pady=5, sticky = W)

        time_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_time,font=("times new roman", 12, "bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5, sticky =W)

        #date

        date_label = Label(left_inside_frame, text="Date:",font=("times new roman", 12, "bold"), fg="red")
        date_label.grid(row=2,column=2,padx=10,pady=5, sticky = W)

        date_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("times new roman", 12, "bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5, sticky =W)

        #attendance status

        attendance_label = Label(left_inside_frame, text="Attendance Status:",font=("times new roman", 12, "bold"), fg="red")
        attendance_label.grid(row=3,column=0, padx=10, sticky = W)
        attendance_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman", 12, "bold"),width=13,state = "readonly")
        attendance_combo["values"]=("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,padx=10, pady=5, sticky = W)

        btn_frame = Frame(left_inside_frame,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=350,width=600,height = 35)

        #import csv
        import_btn = Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        import_btn.grid(row=0,column=0,padx=2,pady=5,sticky = W)

        #export csv
        export_btn = Button(btn_frame,text="Export csv",width=15,command=self.exportCsv,font=("times new roman", 12, "bold"), fg="white",bg="red")
        export_btn.grid(row=0,column=1,padx=2,pady=2,sticky = W)

        #update button
        update_btn = Button(btn_frame,text="Update",command=self.action,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        update_btn.grid(row=0,column=2,padx=2,pady=2,sticky = W)

        #reset button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        reset_btn.grid(row=0,column=3,padx=2,pady=2,sticky = W)
        
        #right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Attendance Details",cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        right_frame.place(x=660,y=10,width=630,height = 540)

        #table frame
        table_frame = Frame(right_frame,relief=RIDGE)
        table_frame.place(x=5,y=10,width=615,height = 495)

        #========SCROLL BAR TABLE========

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("ID","Roll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll",text="Roll No")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance") 

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    
    #=======Fetch Data========
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode ="w",newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data exported to :"+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0]),
        self.var_atten_roll.set(rows[1]),
        self.var_atten_name.set(rows[2]),
        self.var_atten_dep.set(rows[3]),
        self.var_atten_time.set(rows[4]),
        self.var_atten_date.set(rows[5]),
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set(""),
        self.var_atten_roll.set(""),
        self.var_atten_name.set(""),
        self.var_atten_dep.set("Select Department"),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_attendance.set("Status")
    
    #update 

    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
            self.reset_data()
            

        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)








        



if __name__=="__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()