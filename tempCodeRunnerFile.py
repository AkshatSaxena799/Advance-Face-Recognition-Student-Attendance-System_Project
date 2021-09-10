def search_data(self):
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
        