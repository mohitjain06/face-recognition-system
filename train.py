from tkinter import*
from tkinter import ttk     #for styling tools
from PIL import Image,ImageTk  #image ki processing ya edit krne ke liye
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open(r"c:\Users\Hp\Desktop\face_project_images\1_LJa3uwoVHFQ-ojw5JgF3nw.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lbl=Label(self.root,image=self.photoimg_top)
        first_lbl.place(x=0,y=55,width=1530,height=325)

        bt_btn=Button(self.root,text="TRAIN DATA",width=17,font=("times new roman",30,"bold"),bg="red",fg="white")
        bt_btn.place(x=0,y=380,width=1530,height=40)


        img_bottom=Image.open(r"c:\Users\Hp\Desktop\face_project_images\download (3).jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        first_lbl=Label(self.root,image=self.photoimg_bottom)
        first_lbl.place(x=0,y=440,width=1530,height=325)

    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        face=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.'[1]))

            face.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(face,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed")

            


        



if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()