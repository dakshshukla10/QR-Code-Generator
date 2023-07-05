from tkinter import * # Importing tkinter module
import qrcode # pip install qrcode
from PIL import Image,ImageTk # pip install pillow
import os # Built-in module
from resizeimage import resizeimage # pip install python-resize-image

class QR_Code_Gen:
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='#222831') # Setting background color
        self.root.geometry("900x500+200+50") # Setting window size
        self.root.title("QR Code Generator") # Setting window title
        self.root.resizable(False,False) # Setting window unresizable

        title=Label(self.root,text="QR Code Generator",font=("Drugsther",40),bg='#222831',fg='#EEEEEE').place(x=0,y=30,relwidth=1)

                            # User Detail Window

        user_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='#393E46') # Setting frame
        user_Frame.place(x=50,y=100,width=500,height=380) # Setting frame size

        self.var_userID=StringVar()
        self.var_userName=StringVar()
        self.var_userDepartment=StringVar()
        self.var_userBranch=StringVar()

        userTitle=Label(user_Frame,text="USER DETAILS",font=("Drugsther",30),bg="#393E46",fg='#EEEEEE').place(x=0,y=0,relwidth=1)

        userID=Label(user_Frame,text="STUDENT ID",font=("Drugsther",20,'bold'),bg="#393E46").place(x=20,y=60)
        userName=Label(user_Frame,text="NAME",font=("Drugsther",20,'bold'),bg="#393E46").place(x=20,y=100)
        userDepartment=Label(user_Frame,text="DEPARTMENT",font=("Drugsther",20,'bold'),bg="#393E46").place(x=20,y=140)
        userBranch=Label(user_Frame,text="BRANCH",font=("Drugsther",20,'bold'),bg="#393E46").place(x=20,y=180)

        txt_userID=Entry(user_Frame,font=("Drugsther",20),bg="#393E46",textvariable=self.var_userID).place(x=200,y=60)
        txt_userName=Entry(user_Frame,font=("Drugsther",20),bg="#393E46",textvariable=self.var_userName).place(x=200,y=100)
        txt_userDepartment=Entry(user_Frame,font=("Drugsther",20),bg="#393E46",textvariable=self.var_userDepartment).place(x=200,y=140)
        txt_userBranch=Entry(user_Frame,font=("Drugsther",20),bg="#393E46",textvariable=self.var_userBranch).place(x=200,y=180)

        btn_generate=Button(user_Frame,text="GENERATE",font=("Drugsther",20),bg="#393E46",activebackground='#00ADB5',fg='#393E46',command=self.generate).place(x=100,y=250,width=150,height=40)
        btn_clear=Button(user_Frame,text="CLEAR",font=("Drugsther",20),bg="#393E46",activebackground='#00ADB5',fg='#393E46',command=self.clear).place(x=270,y=250,width=150,height=40)

        self.success_msg=''
        self.success_msg_display=Label(user_Frame,text=self.success_msg,font=("Drugsther",20),bg="#393E46",fg='#EEEEEE')
        self.success_msg_display.place(x=0,y=310,relwidth=1)

                                # QR Code Generation Window

        QR_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='#393E46')
        QR_Frame.place(x=600,y=100,width=250,height=380)

        QrTitle=Label(QR_Frame,text="QR",font=("Drugsther",30),bg="#393E46",fg='#EEEEEE').place(x=0,y=0,relwidth=1)

        self.Qr_Code_img=Label(QR_Frame,text="QR Code\nNot Generated",font=("Drugsther",16),bg="#393E46",fg='#EEEEEE')
        self.Qr_Code_img.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_userID.set('')
        self.var_userName.set('')
        self.var_userDepartment.set('')
        self.var_userBranch.set('') 
        self.success_msg='' # Clearing success message
        self.success_msg_display.config(text=self.success_msg,fg='#EEEEEE') # Clearing success message
        self.Qr_Code_img.config(image='') # Clearing QR Code
          
    def generate(self):
        if  self.var_userName.get()=='' or self.var_userID.get()=='' or self.var_userDepartment.get()=='' or self.var_userBranch.get()=='':
            self.success_msg=("⚠️ All fields are required ⚠️")
            self.success_msg_display.config(text=self.success_msg,fg='red')
        else:
            qr_data=(f"Student ID : {self.var_userID.get()},\nStudent Name : {self.var_userName.get()},\nDepartment : {self.var_userDepartment.get()},\nBranch : {self.var_userBranch.get()}")
            qr_code=qrcode.make(qr_data)
            # print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            self.img=ImageTk.PhotoImage(image=qr_code)
            self.Qr_Code_img.config(image=self.img)
            
                            # Create directory if it does not exist

            if not os.path.exists('studentQRcodes'):
              os.makedirs('studentQRcodes')

            qr_code.save(f"studentQRcodes/{self.var_userID.get()}.png")

                            # Saving QR Code

            self.success_msg=("QR Code generated successfully ✓")
            self.success_msg_display.config(text=self.success_msg,fg='#00ADB5')

root=Tk() # Creating object of Tk class
obj = QR_Code_Gen(root) # Creating object of the class and passing root as argument 
root.mainloop() # Keeps the window open until we close it
