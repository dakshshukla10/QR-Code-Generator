#importing libraries
from tkinter import*
class QR_Code_Gen:
  def __init__(self,root):
    """
    Initializes the QR_Code_Gen class with the given root window.

    Args:
    root: The root window object.

    Returns:
    None
    """
    self.root=root
    self.root.configure(bg='#222831') #Setting background color
    self.root.geometry("900x500+200+50") #Setting window size
    self.root.title("QR Code Generator") #Setting window title
    self.root.resizable(False,False) #Setting window unresizable
    
    title=Label(self.root,text="QR Code Generator",font=("Drugsther",40),bg='#222831',fg='#EEEEEE').place(x=0,y=0,relwidth=1)
    
    #User Detail Window
    user_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='#393E46')
    user_Frame.place(x=50,y=100,width=500,height=380)
    
    userTitle=Label(user_Frame,text="USER DETAILS",font=("Drugsther",30),bg="#393E46",fg='#EEEEEE').place(x=0,y=0,relwidth=1)
    
    userID=Label(user_Frame,text="STUDENT ID",font=("Drugsther",20,'bold'),bg="#393E46").place(x=20,y=60)
    userName=Label(user_Frame,text="NAME",font=("Drugsther",20,'bold'),bg="#393E46").place(x=20,y=100)
    userDepartment=Label(user_Frame,text="DEPARTMENT",font=("Drugsther",20,'bold'),bg="#393E46").place(x=20,y=140)
    userBranch=Label(user_Frame,text="BRANCH",font=("Drugsther",20,'bold'),bg="#393E46").place(x=20,y=180)
    
    txt_userID=Entry(user_Frame,font=("Drugsther",20),bg="#393E46").place(x=200,y=60)
    txt_userName=Entry(user_Frame,font=("Drugsther",20),bg="#393E46").place(x=200,y=100)
    txt_userDepartment=Entry(user_Frame,font=("Drugsther",20),bg="#393E46").place(x=200,y=140)
    txt_userBranch=Entry(user_Frame,font=("Drugsther",20),bg="#393E46").place(x=200,y=180)
    
    btn_generate=Button(user_Frame,text="GENERATE",font=("Drugsther",20),bg="#393E46",activebackground='#00ADB5',fg='#393E46').place(x=100,y=250,width=150,height=40)
    btn_clear=Button(user_Frame,text="CLEAR",font=("Drugsther",20),bg="#393E46",activebackground='#00ADB5',fg='#393E46').place(x=270,y=250,width=150,height=40)
    
    success_msg=("QR Code intialized successfully")
    success_msg_display=Label(user_Frame,text=success_msg,font=("Drugsther",20),bg="#393E46",fg='#EEEEEE').place(x=0,y=310,relwidth=1)
    
                      #QR Code Generation Window
    QR_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='#393E46')
    QR_Frame.place(x=600,y=100,width=250,height=380)
    
    QrTitle=Label(QR_Frame,text="QR",font=("Drugsther",30),bg="#393E46",fg='#EEEEEE').place(x=0,y=0,relwidth=1)
    
    Qr_Code_img=Label(QR_Frame,text="QR Code\nNot Generated",font=("Drugsther",16),bg="#393E46",fg='#EEEEEE').place(x=35,y=100,width=180,height=180)
    
root=Tk() #Creating object of Tk class
obj =QR_Code_Gen(root) #Creating object of the class and passing root as argument 
root.mainloop() #Keeps the window open until we close it
