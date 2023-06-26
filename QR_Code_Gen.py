from tkinter import*
class QR_Code_Gen:
  def __init__(self,root):
    self.root=root
    self.root.geometry("900x500+200+50")
    self.root.title("QR Code Generator")
    self.root.resizable(False,False)
    title=Label(self.root,text="QR Code Generator",font=("times new roman",40),bg='#525FE1').place(x=0,y=0,relwidth=1)
    
    
root=Tk()
obj =QR_Code_Gen(root)
root.mainloop()