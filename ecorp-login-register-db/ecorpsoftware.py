import tkinter as tk
from tkinter import ttk,messagebox
from PIL import ImageTk, Image
import pymysql
import time;



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MessengerAPP(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)


class LoginPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)



       self.bg = ImageTk.PhotoImage(file="background.jpg")
       bg = tk.Label(self, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

       # left image==
       self.left = ImageTk.PhotoImage(file="left-logo.png")
       left = tk.Label(self, image=self.left).place(x=60, y=80, width=335, height=303)


       # login frame
       frame1 = tk.Frame(self, bg="white")
       frame1.place(x=390, y=80, width=550, height=303)
       localtime = tk.Label(self, text="Local current time: "+str(time.asctime(time.localtime(time.time()))), font=("arial", 15, "bold"), bg="white", fg="black").place(x=503, y=51)
       title = tk.Label(frame1, text="Sign In", font=("arial", 15, "bold"), bg="white",fg="black").place(x=240, y=20)

       var_fname = tk.StringVar()
       f_name = tk.Label(frame1, text="Username", font=("arial", 15, "bold"), bg="white", fg="black").place(x=35, y=60)
       txt_fname = tk.Entry(frame1, font=("arial", 15), bg="lightgray",textvariable=var_fname).place(x=35, y=90)

       var_cpassword = tk.StringVar()
       cpassword = tk.Label(frame1, text="Password", font=("arial", 15, "bold"), bg="white", fg="black").place(x=35, y=150)
       txt_cpassword = tk.Entry(frame1, font=("arial", 15), bg="lightgray",textvariable=var_cpassword).place(x=35, y=180)

       self.login_img = ImageTk.PhotoImage(file="login.png")
       loginimg = tk.Button(frame1, image=self.login_img, cursor="hand2", bd=0).place(x=300, y=85)

       # CODE FOR LOGIN WITH DATABASE SQL


       def clear():
           var_fname.set('')
           var_cpassword.set('')

       def login_data():
           if var_fname.get() == "" or var_cpassword.get() == "":
               messagebox.showerror("Error", "All fields Are Required", parent=self)

           else:
               try:
                   con = pymysql.connect(host="localhost", user="root", password="", database="ecorpdb")
                   cur = con.cursor()

                   cur.execute("SELECT * FROM credentials WHERE username = %s AND password = %s", (var_fname.get(), var_cpassword.get()))
                   if cur.fetchone() is not None:
                       print("succes")
                       clear()
                   else:
                       print("fail")
                       clear()

               except Exception as es:
                   messagebox.showerror("Error", f"Error duo to: {str(es)}", parent=self)

       self.login_img = ImageTk.PhotoImage(file="login.png")
       loginimg = tk.Button(self, image=self.login_img, cursor="hand2", bd=0, command= login_data).place(x=690, y=165)
class RegisterPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       self.bg = ImageTk.PhotoImage(file="background.jpg")
       bg = tk.Label(self, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

       localtime = tk.Label(self, text="Local current time: " + str(time.asctime(time.localtime(time.time()))),font=("arial", 15, "bold"), bg="white", fg="black").place(x=503, y=51)
       # left image==
       self.left = ImageTk.PhotoImage(file="left-logo.png")
       left = tk.Label(self, image=self.left).place(x=60, y=80, width=335, height=303)

       # login frame
       frame1 = tk.Frame(self, bg="white")
       frame1.place(x=390, y=80, width=550, height=303)

       title = tk.Label(frame1, text="Register", font=("arial", 15, "bold"), bg="white", fg="black").place(x=240, y=20)

       var_fname=tk.StringVar()
       f_name = tk.Label(frame1, text="Username", font=("arial", 15, "bold"), bg="white", fg="black").place(x=35, y=65)
       txt_fname = tk.Entry(frame1, font=("arial", 15), bg="lightgray",textvariable=var_fname).place(x=35, y=90)

       var_cpassword=tk.StringVar()
       cpassword = tk.Label(frame1, text="Password", font=("arial", 15, "bold"), bg="white",fg="black").place(x=35, y=125)
       txt_cpassword = tk.Entry(frame1, font=("arial", 15), bg="lightgray",textvariable=var_cpassword).place(x=35, y=150)

       var_ccpassword = tk.StringVar()
      # ccpassword = tk.Label(frame1, text="Email", font=("arial", 15, "bold"), bg="white",fg="black").place(x=35, y=100)
       txt_ccpassword = tk.Entry(frame1, font=("arial", 15), bg="lightgray",textvariable=var_ccpassword).place(x=35, y=190)

       var_email = tk.StringVar()
       email = tk.Label(frame1, text="Email", font=("arial", 15, "bold"), bg="white",fg="black").place(x=35, y=225)
       txt_email = tk.Entry(frame1, font=("arial", 15), bg="lightgray",textvariable=var_email).place(x=35, y=250)


       #CODE FOR REGISTATION WITH DATABASE SQL
       def clear():
           var_fname.set('')
           var_cpassword.set('')
           var_ccpassword.set('')
           var_email.set('')


       def register_data():
           if var_fname.get()=="" or var_cpassword.get()=="" or var_ccpassword.get()=="" or var_email.get()=="":
               messagebox.showerror("Error","All fields Are Required",parent=self)
           elif var_cpassword.get()!=var_ccpassword.get():
               messagebox.showerror("Error","Password & Confirm Password should be same",parent=self)
           else:
               try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="ecorpdb")
                    cur=con.cursor()

                    cur.execute("select * from credentials where username=%s",var_fname.get())
                    #cur.execute("select * from credentials where username=%s",var_fname.get())
                    row=cur.fetchone()

                    #print(row)
                    if row!=None:
                        messagebox.showerror("Error","User already Exist, Please try with another username",parent=self)
                    else:
                        cur.execute("insert into credentials (username,password,email) values(%s,%s,%s)",
                                    (var_fname.get(),
                                     var_cpassword.get(),
                                     var_email.get()
                                    ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Register Success",parent=self)
                        clear()
               except Exception as es:
                    messagebox.showerror("Error",f"Error duo to: {str(es)}",parent=self)



           #print(var_fname.get())
           #print(var_cpassword.get())
           #print(var_email.get())
       self.register_img = ImageTk.PhotoImage(file="register.png")
       registerimg = tk.Button(self, image=self.register_img, cursor="hand2", bd=0,command=register_data).place(x=690, y=165)

class afterLogin(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
        #AFTER LOGIN INTERFACE

        #background
       self.bg = ImageTk.PhotoImage(file="background.jpg")
       bg = tk.Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

       # left image==
    #   self.left = ImageTk.PhotoImage(file="left-logo.png")
     #  left = tk.Label(self, image=self.left).place(x=60, y=80, width=335, height=303)

       frame1 = tk.Frame(self, bg="white")
       frame1.place(x=30, y=30, width=940, height=450)

    #center logo
       self.center = ImageTk.PhotoImage(file="center-logo.png")
       center = tk.Label(self, image=self.center).place(x=400, y=0, width=200, height=181)
       wlc_msg = tk.Label(self, text="Login as: karidis arxidis ", font=("arial", 10, "bold"), bg="black", fg="white").place(x=30,y=0,height=30)

       #wlc_time = tk.Label(self, text=str(time.asctime(time.localtime(time.time()))), font=("arial", 15, "bold"), bg="black",fg="white").place(x=750, y=0, height=30)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = LoginPage(self)
        p2 = RegisterPage(self)
        p3 = afterLogin(self)
        p4 = MessengerAPP(self)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

       # b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
       # b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
       # b3 = tk.Button(buttonframe, text="Page 3", command=p4.lift)

       # b1.pack(side="left")
       # b2.pack(side="left")
       # b3.pack(side="left")

#page 1 buttons
        p1.register_img = ImageTk.PhotoImage(file="register.png")
        p1.registerimg = tk.Button(p1, image=p1.register_img, cursor="hand2", bd=0, command=p2.lift).place(x=690, y=250)

       # p1.login_img = ImageTk.PhotoImage(file="login.png")
       # p1.loginimg = tk.Button(p1, image=p1.login_img, cursor="hand2", bd=0,command=p3.lift).place(x=690, y=165)

#page 2 buttons
        #p2.register_img = ImageTk.PhotoImage(file="register.png")
        #p2.registerimg = tk.Button(p2, image=p2.register_img, cursor="hand2", bd=0,command=p2.register_data()).place(x=690, y=165)

        p2.login_img = ImageTk.PhotoImage(file="login.png")
        p2.loginimg = tk.Button(p2, image=p2.login_img, cursor="hand2", bd=0,command=p1.lift).place(x=690, y=250)
#page 3 buttons

        p3.signout_img=ImageTk.PhotoImage(file="signout.png")
        p3.signoutimg = tk.Button(p3, image=p3.signout_img, cursor="hand2", bd=0,command=p1.lift).place(x=735, y=40)


#page4 buttons

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x500+0+0")
    root.resizable(False, False)
    root.title("E-Corp Software")

    root.mainloop()