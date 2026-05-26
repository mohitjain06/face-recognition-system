from tkinter import*
from tkinter import ttk     #for styling tools
from PIL import Image,ImageTk  #image ki processing ya edit krne ke liye
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="Help Desk",font=("Times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

       
        img_top=Image.open(r"face_project_images/Captures.PNG")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lbl=Label(self.root,image=self.photoimg_top)
        first_lbl.place(x=0,y=55,width=1530,height=720)


        

        help_label=Label(first_lbl,text="Email: mohitjain2380@gmail.com",font=("times new roman",20,"bold"),bg="white")
        help_label.place(x=550,y=250)













if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()