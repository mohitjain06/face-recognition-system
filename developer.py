from tkinter import*
from tkinter import ttk     #for styling tools
from PIL import Image,ImageTk  #image ki processing ya edit krne ke liye
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="DEVELOPER",font=("Times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

       
        img_top=Image.open(r"face_project_images/technology-w65hwkhmusntb0j9.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lbl=Label(self.root,image=self.photoimg_top)
        first_lbl.place(x=0,y=55,width=1530,height=720)


        main_frame=Frame(first_lbl,bd=2) 
        main_frame.place(x=1000,y=0,width=500,height=600)


        img_t=Image.open(r"face_project_images/75f64d4a726393e84bb0873b6ef02d9e.jpg")
        img_t=img_t.resize((500,600),Image.ANTIALIAS)
        self.photoimg_t=ImageTk.PhotoImage(img_t)

        first_l=Label(main_frame,image=self.photoimg_t)
        first_l.place(x=0,y=0,width=500,height=600)


        developer_label=Label(first_lbl,text="I am the  Developer",font=("times new roman",25,"bold"),bg="white")
        developer_label.place(x=1000,y=650)













if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()