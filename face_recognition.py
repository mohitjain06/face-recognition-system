from tkinter import*
from tkinter import ttk     #for styling tools
from PIL import Image,ImageTk  #image ki processing ya edit krne ke liye
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime




class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

       
        img_top=Image.open(r"c:\Users\Hp\Desktop\face_project_images\chessboard_1-mobile2x.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lbl=Label(self.root,image=self.photoimg_top)
        first_lbl.place(x=0,y=55,width=650,height=700)


        img_bottom=Image.open(r"c:\Users\Hp\Desktop\face_project_images\Capture.PNG")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        first_lbl=Label(self.root,image=self.photoimg_bottom)
        first_lbl.place(x=650,y=55,width=950,height=700)


        bt_btn=Button(first_lbl,text="Face Recognition",width=17,font=("times new roman",18,"bold"),bg="dark green",fg="white")
        bt_btn.place(x=365,y=620,width=200,height=40)


    def mark_attendance(self,i,r):
        with open("Mohit.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist :
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((i not in name_list) and (r not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{i}","{dtString},{d1},Present")





    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
             features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

             coord=[]

             for (x,y,w,h) in features:
                 cv2.rectangle(img(x,y),(x+w),(y+h),(0,255,0),3)
                 id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                 confidence=int((100*(1-predict/300)))


                 conn=mysql.connector.Connect(host="localhost",username="root",password="1234",database="face_recognizer")
                 my_cursor=conn.cursor() 

                 my_cursor.execute("Select Name from student where Student_id="+str(id))
                 i=my_cursor.fetchone()
                 i="+".join(i)

                 my_cursor.execute("Select Roll from student where Student_id="+str(id))
                 r=my_cursor.fetchone()
                 r="+".join(r)

                 if confidence>77:
                     cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     self.mark_attendance(r,i)

                 else:
                     cv2.rectangle(img(x,y),(x+w),(y+h),(0,0,255),2)
                     cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                 coord=[x,y,w,h]

             return coord
    
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img    
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
        clf=cv2.face.LBPHFFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face REcognizer",img)

            if cv2.waitKey(1)==13:
                break

            video_cap.release()
            cv2.destroyAllWindows
        
                     
                     
       







if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()