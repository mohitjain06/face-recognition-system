from tkinter import*
from tkinter import ttk     #for styling tools
from PIL import Image,ImageTk  #image ki processing ya edit krne ke liye
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import conj



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        #first image
        img1=Image.open(r"c:\Users\Hp\Desktop\face_project_images\download (1).jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=0,y=0,width=500,height=130)


        #second image
        img2=Image.open(r"c:\Users\Hp\Desktop\face_project_images\download (2).jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl=Label(self.root,image=self.photoimg2)
        first_lbl.place(x=500,y=0,width=500,height=130)


        #third image
        img3=Image.open(r"c:\Users\Hp\Desktop\face_project_images\images (2).jpg")
        img3=img3.resize((550,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        first_lbl=Label(self.root,image=self.photoimg3)
        first_lbl.place(x=1000,y=0,width=550,height=130)


         #bg image
        img4=Image.open(r"c:\Users\Hp\Desktop\face_project_images\bg_img.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="Student Management System",font=("Times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2) 
        main_frame.place(x=0,y=55,width=1520,height=600)
        
        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"c:\Users\Hp\Desktop\face_project_images\facial-recognition-behavior-analysis-in-the-classroom-educational-sector.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_lbl=Label(left_frame,image=self.photoimg_left)
        first_lbl.place(x=5,y=0,width=720,height=130)

        #current course
        CURRENT_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        CURRENT_course_frame.place(x=5,y=135,width=720,height=150)

        dep_label=Label(CURRENT_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(CURRENT_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select department","Engineering & Technology","Management","Pharmacy","Agriculture")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(CURRENT_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(CURRENT_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select course","Computer Science","IT","Civil","Mechanical","Electrical")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(CURRENT_course_frame,text="year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(CURRENT_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(CURRENT_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(CURRENT_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student information
        Class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_student_frame.place(x=5,y=250,width=720,height=300)


        studentId_label=Label(Class_student_frame,text="StudentId",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        studentName_label=Label(Class_student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(Class_student_frame,text="Class Division",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Division_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=17)
        Division_combo["values"]=("Select ","A","B","C","D")
        Division_combo.current(0)
        Division_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #roll no
        roll_no_label=Label(Class_student_frame,text="Roll No",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #gender
        gender_label=Label(Class_student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=17)
        gender_combo["values"]=("Select ","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        


        #dob
        dob_label=Label(Class_student_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #email
        email_label=Label(Class_student_frame,text="Email",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #phone no
        phone_no_label=Label(Class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        Address_label=Label(Class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(Class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #teacher name
        teacher_label=Label(Class_student_frame,text="Teacher Name",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(Class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
        self.var_radio1=StringVar()
        radiobtn2=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)


        btn_frame=LabelFrame(Class_student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=220,width=715,height=35)


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=LabelFrame(Class_student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame1.place(x=0,y=255,width=715,height=35)


        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take  Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=750,height=580)

        img_right=Image.open(r"c:\Users\Hp\Desktop\face_project_images\indian-college-friends-student-studying-laptop-library-JC2CA3.jpg")
        img_right=img_right.resize((750,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        first_lbl=Label(right_frame,image=self.photoimg_right)
        first_lbl.place(x=5,y=0,width=750,height=130)


        #search system
        search_system_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_system_frame.place(x=5,y=150,width=740,height=70)

        search_label=Label(search_system_frame,text="Search By",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_system_frame,font=("times new roman",13,"bold"),state="readonly",width=17)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_system_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        search_btn=Button(search_system_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        ShowAll_btn=Button(search_system_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4)

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #function declaration
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            conn=mysql.connector.Connect(host="localhost",username="root",password="1234",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
           
    def  fetch_data(self):
                conn=mysql.connector.Connect(host="localhost",username="root",password="1234",database="face_recognizer")
                my_cursor=conn.cursor()   
                my_cursor.execute("select * from student")  
                data = my_cursor.fetchall()

                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()

    def get_cursor(self):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0]),  
        self.var_course.set(data[1]), 
        self.var_year.set(data[2]), 
        self.var_semester.set(data[3]),  
        self.var_id.set(data[4]),  
        self.var_name.set(data[5]),     
        self.var_div.set(data[6]),  
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),  
        self.var_dob.set(data[9]),  
        self.var_email.set(data[10]),  
        self.var_phone.set(data[11]),  
        self.var_address.set(data[12]),  
        self.var_teacher.set(data[13]),  
        self.usertype.set(data[14]),  



    def generate_dataset(self):
           if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)

           else:
                try:
                    conn=mysql.connector.Connect(host="localhost",username="root",password="1234",database="face_recognizer")
                    my_cursor=conn.cursor()  
                    my_cursor.execute("select * from Student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_id.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get()
                                                                                                                                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                
                
                except Exception as es:
                   messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
   
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
        

                def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)


                        for(x,y,w,h) in faces:
                             face_cropped=img[y:y+h,x:x+w]
                             return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                        ret,myframe=cap.read()
                        if face_cropped(myframe) is not None:
                            img_id+=1
                            fece=cv2.resize(face_cropped(myframe),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name)
                            cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")        
    
                



        

        

        
        
        




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()