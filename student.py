from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from cv2 import cv2



class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System")

        #==========Variables==========
        self.serchTxt_var=StringVar()
        self.search_var=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar() #for later uses
        self.var_year=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_semester=StringVar()
        

        img = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\black.jpg")
        img = img.resize((1366,128),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 1366, height = 138)
        
        title_lbl = Label(f_lbl, text = "Student Management System", font=("times new roman", 30, "bold"),bg="white",fg="red")
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
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student Details",cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        left_frame.place(x=10,y=10,width=630,height = 540)
        img_left = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\student2.jpg")
        img_left = img_left.resize((100,60),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame,image =self.photoimg_left,cursor="hand2")
        f_lbl.place(x=270,y = 10,width=60, height = 60)

        #current course
        current_course_frame = LabelFrame(left_frame, relief=RIDGE,text="Current Course Information",font=("times new roman", 12, "bold"),fg="red")
        current_course_frame.place(x=5,y=75,width=615,height = 105)

        #department
        dep_label = Label(current_course_frame, text="Department:",font=("times new roman", 12, "bold"), fg="red")
        dep_label.grid(row=0,column=0, padx=10, sticky = W)
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        dep_combo["values"]=("Select Department","Computer Science","Information Science ","Electronics","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2, pady=10, sticky = W)

        #year
        year_label = Label(current_course_frame, text="Year:",font=("times new roman", 12, "bold"), fg="red")
        year_label.grid(row=0,column=2,padx=10, sticky = W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        year_combo["values"]=("Select Year","First Year","Second Year","Third Year","Fourth Year")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2, pady=10, sticky = W)

        #semester
        semester_label = Label(current_course_frame, text="Semester:",font=("times new roman", 12, "bold"), fg="red")
        semester_label.grid(row=1,column=0,padx=10, sticky = W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        semester_combo["values"]=("Select Semester","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=1,padx=2, pady=10, sticky = W)

        #Class Information
        class_Student_frame = LabelFrame(left_frame, relief=RIDGE,text="Class Information",font=("times new roman", 12, "bold"),fg="red")
        class_Student_frame.place(x=5,y=185,width=615,height = 315)

        #Student ID
        studentId_label = Label(class_Student_frame, text="Student ID:",font=("times new roman", 12, "bold"), fg="red")
        studentId_label.grid(row=0,column=0,padx=10, sticky = W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5, sticky =W)

        #Student Name
        studentName_label = Label(class_Student_frame, text="Student Name:",font=("times new roman", 12, "bold"), fg="red")
        studentName_label.grid(row=0,column=2,padx=10, sticky = W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5, sticky =W)

        #Class Division
        class_div_label = Label(class_Student_frame, text="Class and Section:",font=("times new roman", 12, "bold"), fg="red")
        class_div_label.grid(row=1,column=0,padx=10, sticky = W)

        class_div_entry = ttk.Entry(class_Student_frame,textvariable=self.var_div,width=15,font=("times new roman", 12, "bold"))
        class_div_entry.grid(row=1,column=1,padx=10, pady=5, sticky =W)

        #Roll_No
        roll_no_label = Label(class_Student_frame, text="Roll No:",font=("times new roman", 12, "bold"), fg="red")
        roll_no_label.grid(row=1,column=2,padx=10, sticky = W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1,column=3,padx=10, pady=5, sticky =W)

        #Gender
        gender_label = Label(class_Student_frame, text="Gender:",font=("times new roman", 12, "bold"), fg="red")
        gender_label.grid(row=2,column=0,padx=10, sticky = W)
        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman", 12, "bold"),width=13,state = "readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10, pady=5, sticky = W)

        #Date of birth
        dob_label = Label(class_Student_frame, text="Date of Birth:",font=("times new roman", 12, "bold"), fg="red")
        dob_label.grid(row=2,column=2,padx=10, sticky = W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2,column=3,padx=10, pady=5, sticky =W)

        #Email
        email_label = Label(class_Student_frame, text="Email:",font=("times new roman", 12, "bold"), fg="red")
        email_label.grid(row=3,column=0,padx=10, sticky = W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("times new roman", 12, "bold"))
        email_entry.grid(row=3,column=1,padx=10, pady=5, sticky =W)

        #Phone No
        phone_label = Label(class_Student_frame, text="Phone No:",font=("times new roman", 12, "bold"), fg="red")
        phone_label.grid(row=3,column=2,padx=10, sticky = W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=15,font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3,column=3,padx=10, pady=5, sticky =W)

        #Address
        address_label = Label(class_Student_frame, text="Address:",font=("times new roman", 12, "bold"), fg="red")
        address_label.grid(row=4,column=0,padx=10, sticky = W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("times new roman", 12, "bold"))
        address_entry.grid(row=4,column=1,padx=10, pady=5, sticky =W)

        #Teacher name
        teacher_label = Label(class_Student_frame, text="Teacher:",font=("times new roman", 12, "bold"), fg="red")
        teacher_label.grid(row=4,column=2,padx=10, sticky = W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10, pady=5, sticky =W)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1= ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text ="Take a photo sample", value="Yes")
        radionbtn1.grid(row=5,column=0)
        radionbtn2= ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text ="No photo sample", value="No")
        radionbtn2.grid(row=5,column=1)

        
        #bbuttons_frame
        btn_frame = Frame(class_Student_frame,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=600,height = 85)

        #save button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        save_btn.grid(row=0,column=0,padx=2,pady=5,sticky = W)

        #update button
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        update_btn.grid(row=0,column=1,padx=2,pady=2,sticky = W)

        #delete button
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_Data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        delete_btn.grid(row=0,column=2,padx=2,pady=2,sticky = W)

        #reset button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman", 12, "bold"), fg="white",bg="red")
        reset_btn.grid(row=0,column=3,padx=2,pady=2,sticky = W)

        btn_frame1 = Frame(class_Student_frame,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=240,width=600,height = 35)

        #take photo button
        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample",width=30,font=("times new roman", 12, "bold"), fg="white",bg="red")
        take_photo_btn.grid(row=0,column=0,padx=10,pady=2,sticky = W)

        #update photo button
        update_btn = Button(btn_frame1,text="Update Photo",command=self.generate_dataset,width=30,font=("times new roman", 12, "bold"), fg="white",bg="red")
        update_btn.grid(row=0,column=1,padx=2,pady=2,sticky = W)




        #right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student Details",cursor="hand2",font=("times new roman", 12, "bold"),bg="white",fg="red")
        right_frame.place(x=660,y=10,width=630,height = 540)

        img_right = Image.open(r"C:\Users\Dell\Desktop\FR SYSTEM\Images\student1.png")
        img_right= img_right.resize((250,60),Image.ANTIALIAS) #resize and converting high level img to low level img.
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(right_frame,image =self.photoimg_right,cursor="hand2")
        f_lbl.place(x=5,y = 10,width=615, height = 60)


        #=======SEARCH SYSTEM=======
        search_frame = LabelFrame(right_frame, relief=RIDGE,text="Search System (UNDER CONSTRUCTION)",font=("times new roman", 12, "bold"),fg="red")
        search_frame.place(x=5,y=75,width=615,height = 70)

        search_label = Label(search_frame, text="Search By:",font=("times new roman", 12, "bold"), fg="red")
        search_label.grid(row=0,column=0,padx=3,pady=5, sticky = W)

        search_combo = ttk.Combobox(search_frame,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3, pady=5, sticky = W)

        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman", 12, "bold"))
        search_entry.grid(row=0,column=2,padx=10, pady=5, sticky =W)


        search_btn = Button(search_frame,text="Search",width=10,font=("times new roman", 12, "bold"), fg="white",bg="red")
        search_btn.grid(row=0,column=3,padx=3,pady=4,sticky = W)

        showAll_btn = Button(search_frame,text="Show All",width=10,font=("times new roman", 12, "bold"), fg="white",bg="red")
        showAll_btn.grid(row=0,column=4,padx=3,pady=4,sticky = W)
        
        #table frame
        table_frame = Frame(right_frame,relief=RIDGE)
        table_frame.place(x=5,y=150,width=615,height=250)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Department","Year","Semester","ID","Name","Division","Roll No","Gender","DOB","Email","Phone","Address","Teacher","Photo Sample Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Department",text="Department")
        #self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo Sample Status",text="Photo Sample Status")
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    
    #=============Function Declaration==============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=sqlite3.connect('FR.db')
                my_cursor=conn.cursor()
                my_cursor.execute(''' INSERT INTO Student VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''' ,(self.var_dep.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)

    #==========Fetch Data===============
    def fetch_data(self):
        conn=sqlite3.connect('FR.db')
        my_cursor=conn.cursor()
        my_cursor.execute('''SELECT * FROM Student''')
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #=============Get Cursor==============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_std_id.set(data[3]),
        self.var_std_name.set(data[4]),
        self.var_div.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13])
    #Update Function
    def update_data(self): #ERROR
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this data", parent = self.root)
                if Update>0:
                    conn=sqlite3.connect('FR.db')
                    my_cursor=conn.cursor()
                    my_cursor.execute('''Update Student SET Department=?, Year=? , Semester=? , Name=? , Division=? , Roll=? , Gender=? , DOB=? , Email=? , Phone=? , Address=? , Teacher=? , PhotoSample=? where ID=?''',(self.var_dep.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get(),))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)

    #Delete Function
    def delete_Data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?", parent=self.root)
                if delete>0:
                    conn=sqlite3.connect('FR.db')
                    my_cursor=conn.cursor()
                    sql='''DELETE FROM Student WHERE ID=?'''
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Successfully Deleted",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)
    
    #Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    #search
    # def search_data(self):
    #     if self.serchTxt_var.get()=="" or self.search_var.get()=="Select Option":
    #         messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
    #     else:
    #         try:
    #             conn=sqlite3.connect('FR.db')
    #             my_cursor=conn.cursor()
    #             my_cursor.execute('''select * from Student where self.search_var.get() LIKE "%" + self.serchTxt_var.get())+ %''')
    #             rows=my_cursor.fetchall()         
    #             if len(rows)!=0:
    #                 self.student_table.delete(*self.student_table.get_children())
    #                 for i in rows:
    #                     self.student_table.insert("",END,values=i)
    #                 if rows==None:
    #                     messagebox.showerror("Error","Data Not Found",parent=self.root)
    #                     conn.commit()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   
        
    #Take Photo Sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=sqlite3.connect('FR.db')
                my_cursor=conn.cursor()
                my_cursor.execute('''SELECT * FROM Student''')
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute('''Update Student SET Department=?, Year=? , Semester=? , Name=? , Division=? , Roll=? , Gender=? , DOB=? , Email=? , Phone=? , Address=? , Teacher=? , PhotoSample=? where ID=?''',(self.var_dep.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id==id+1,))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=======Load predefined data on face frontals from open cv=========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimum Neighbour = 5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450), fx=0.5, fy=0.5)
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)






                 

            








if __name__=="__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()