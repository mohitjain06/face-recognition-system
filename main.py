from tkinter import*
from tkinter import ttk
import tkinter.messagebox     #for styling tools
from PIL import Image,ImageTk  #image ki processing ya edit krne ke liye
from attendance import Attendance
from student import Student
import tkinter
from time import strftime
import os
from attendance import Attendance
from train import Train
from face_recognition import Face_Recognition_system
from developer import Developer
from help import Help




class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img1=Image.open(r"c:\Users\Hp\Desktop\face_project_images\download1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=0,y=0,width=500,height=130)


        #second image
        img2=Image.open(r"c:\Users\Hp\Desktop\face_project_images\download2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl=Label(self.root,image=self.photoimg2)
        first_lbl.place(x=500,y=0,width=500,height=130)


        #third image
        img3=Image.open(r"c:\Users\Hp\Desktop\face_project_images\download.jpg")
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


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Times new roman",35,"bold"),bg="White",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("Times new roman",13,"bold"),bg="White",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #student button
        img5=Image.open(r"c:\Users\Hp\Desktop\face_project_images\std_image.webp")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_l=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=200,y=300,width=220,height=40)


        #detect face
        img6=Image.open(r"c:\Users\Hp\Desktop\face_project_images\std_img.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_l=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=500,y=300,width=220,height=40)



        #Attendance system
        img7=Image.open(r"c:\Users\Hp\Desktop\face_project_images\atd_img.webp")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Attendance_system)
        b1.place(x=800,y=100,width=220,height=220)

        b1_l=Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendance_system,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=800,y=300,width=220,height=40)

        #help
        img8=Image.open(r"c:\Users\Hp\Desktop\face_project_images\hlp_img.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_system)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_l=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_system,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=1100,y=300,width=220,height=40)

        #train data
        img9=Image.open(r"c:\Users\Hp\Desktop\face_project_images\train_data.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_l=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=200,y=580,width=220,height=40)

        #photos
        img10=Image.open(r"c:\Users\Hp\Desktop\face_project_images\photos.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_l=Button(bg_img,text="Photos ",cursor="hand2",command=self.open_img,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=500,y=580,width=220,height=40)

        

        #developer
        img12=Image.open(r"c:\Users\Hp\Desktop\face_project_images\dvl_img.png")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.developer_system)
        b1.place(x=800,y=380,width=220,height=220)

        b1_l=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_system,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=800,y=580,width=220,height=40)


        #exit
        img13=Image.open(r"c:\Users\Hp\Desktop\face_project_images\exit.png")
        img13=img13.resize((220,220),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        b1=Button(bg_img,image=self.photoimg13,cursor="hand2",command=self.iexit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_l=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=1100,y=580,width=220,height=40)
    
    def open_img(self):
        os.startfile("data")


    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return


        #function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_system(self.new_window)


    def Attendance_system(self):
       self.new_window=Toplevel(self.root)
       self.app=Attendance(self.new_window)


    
    def developer_system(self):
       self.new_window=Toplevel(self.root)
       self.app=Developer(self.new_window)


    def help_system(self):
       self.new_window=Toplevel(self.root)
       self.app=Help(self.new_window)





        










if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()