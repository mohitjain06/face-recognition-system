from tkinter import*
from tkinter import ttk     #for styling tools
from PIL import Image,ImageTk  #image ki processing ya edit krne ke liye
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        img1=Image.open(r"c:\Users\Hp\Desktop\face_project_images\download (1).jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=0,y=0,width=800,height=200)


        #second image
        img2=Image.open(r"c:\Users\Hp\Desktop\face_project_images\download (2).jpg")
        img2=img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl=Label(self.root,image=self.photoimg2)
        first_lbl.place(x=800,y=0,width=800,height=200)


        #bg image
        img4=Image.open(r"c:\Users\Hp\Desktop\face_project_images\bg_img.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)



        #bg image
        img4=Image.open(r"c:\Users\Hp\Desktop\face_project_images\bg_img.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)



        title_lbl=Label(bg_img,text="Attendance Management System",font=("Times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        

        
        main_frame=Frame(bg_img,bd=2) 
        main_frame.place(x=0,y=55,width=1520,height=600)
        
        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=700)

        img_left=Image.open(r"c:\Users\Hp\Desktop\face_project_images\facial-recognition-behavior-analysis-in-the-classroom-educational-sector.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_lbl=Label(left_frame,image=self.photoimg_left)
        first_lbl.place(x=5,y=0,width=720,height=130)


        inside_frame=Frame(left_frame,bd=2,relief=RIDGE) 
        inside_frame.place(x=0,y=135,width=720,height=300)


        attendanceId_label=Label(inside_frame,text="AttendanceId",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,sticky=W)

        attendanceID_entry=ttk.Entry(inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,sticky=W)


        roll_label=Label(inside_frame,text="Roll",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8)

        attendroll_entry=ttk.Entry(inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",13,"bold"))
        attendroll_entry.grid(row=0,column=3,pady=8)

        # name
        Name_label=Label(inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0)

        attendName_entry=ttk.Entry(inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",13,"bold"))
        attendName_entry.grid(row=1,column=1,pady=8)


        deplabel=Label(inside_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        deplabel.grid(row=1,column=2)

        dep_entry=ttk.Entry(inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=3,pady=8)

        
        time_label=Label(inside_frame,text="Time",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0)

        time_entry=ttk.Entry(inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,pady=8)


        
        date_label=Label(inside_frame,text="Date",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=2)

        date_entry=ttk.Entry(inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,pady=8)


        
        attendance_label=Label(inside_frame,textvariable=self.var_atten_attendance,text="Attendance Status",font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(inside_frame,font=("comicsansns,11,bold"),state="readonly",width=20)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=2,pady=8)
        self.atten_status.current(0)


         
        btn_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=525,width=715,height=75)


        save_btn=Button(btn_frame,text="Import csv",command=self.importdata,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Export",command=self.exportdata,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=750,height=580)

        
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=445)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttendanceReport=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReport.xview)
        scroll_y.config(command=self.AttendanceReport.yview)


        self.AttendanceReport.heading("id",text="Attendance ID")
        self.AttendanceReport.heading("roll",text="Roll")
        self.AttendanceReport.heading("name",text="Name")
        self.AttendanceReport.heading("department",text="Department")
        self.AttendanceReport.heading("time",text="Time")
        self.AttendanceReport.heading("date",text="Date")
        self.AttendanceReport.heading("attendance",text="Attendance")
       
        self.AttendanceReport["show"]="headings"
        self.AttendanceReport.column("id",width=100)
        self.AttendanceReport.column("roll",width=100)
        self.AttendanceReport.column("name",width=100)
        self.AttendanceReport.column("department",width=100)
        self.AttendanceReport.column("time",width=100)
        self.AttendanceReport.column("date",width=100)
        self.AttendanceReport.column("attendance",width=100)


        self.AttendanceReport.pack(fill=BOTH,expand=1)
        self.AttendanceReport.bind("<ButtonRelease>",self.get_cursor)

    
    def fetchdata(self,rows):
        self.AttendanceReport.delete(*self.AttendanceReport.get_children())
        for i in rows:
            self.AttendanceReport.insert("",END,values=i)


    def importdata(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)


    def exportdata(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
            for i in mydata:
                exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your Data Exported")
        
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReport.focus()
        content=self.AttendanceReport.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        
        

            













if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()