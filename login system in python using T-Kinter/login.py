from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #All Images
    

        self.bg=ImageTk.PhotoImage(file="C:/Users/harish/Downloads/Python Projects/login system in python using T-Kinter/images/bg4.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #login frame

        Frame_login=Frame(self.root,bg="black")
        Frame_login.place(x=150,y=150,height=440,width=800)


        title=Label(Frame_login,text="Login Here",bg="red",fg="black",font=("times new roman",25,"bold")).place(x=250,y=30)
        desk=Label(Frame_login,text="User Login Area",bg="red",fg="black",font=("times new roman",10,)).place(x=285,y=100)
        user=Label(Frame_login,text="User Name",bg="red",fg="black",font=("times new roman",15,)).place(x=165,y=150)
        self.txt_user=Entry(Frame_login,font=("times new roman",15))
        self.txt_user.place(x=165,y=190,width=350,height=30)
        user=Label(Frame_login,text="Password",bg="red",fg="black",font=("times new roman",15,)).place(x=165,y=240)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15))
        self.txt_pass.place(x=165,y=280,width=350,height=30)

        forget=Button(Frame_login,text="Forget Password",cursor="hand2",fg="black",bd=0,bg="red",font=("times new roman",10,)).place(x=165,y=320)
        Login=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="black",bd=0,bg="red",font=("times new roman",15,)).place(x=400,y=520,width=200)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="Harish":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\n you Have Successfully logged in ",parent=self.root)


root = Tk()

obj=Login_System(root)
root.mainloop()
