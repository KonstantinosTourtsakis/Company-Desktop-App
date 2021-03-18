import tkinter as tk
from tkinter import ttk,messagebox
from PIL import ImageTk, Image
import pymysql
import time
import uuid
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread




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

       p3 = afterLogin(self)

       buttonframe = tk.Frame(self)
       container = tk.Frame(self)
       buttonframe.pack(side="top", fill="x", expand=False)
       container.pack(side="top", fill="both", expand=True)



       p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)



       self.bg = ImageTk.PhotoImage(file="background.jpg")
       bg = tk.Label(self, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

       # left image==
       self.left = ImageTk.PhotoImage(file="left-logo.png")
       left = tk.Label(self, image=self.left).place(x=60, y=80, width=335, height=303)


       # login frame
       frame1 = tk.Frame(self, bg="white")
       frame1.place(x=390, y=80, width=550, height=303)

       localtime = tk.Label(self, text="Local current time: " + str(time.asctime(time.localtime(time.time()))),font=("arial", 10, "bold"), bg="white", fg="black").place(x=640, y=360)
       title = tk.Label(frame1, text="Sign In", font=("arial", 15, "bold"), bg="white",fg="black").place(x=240, y=20)

       var_fname = tk.StringVar()
       f_name = tk.Label(frame1, text="Username", font=("arial", 15, "bold"), bg="white", fg="black").place(x=35, y=60)
       txt_fname = tk.Entry(frame1, font=("arial", 15), bg="lightgray",textvariable=var_fname).place(x=35, y=90)
       bullet = "\u2022"
       var_cpassword = tk.StringVar()
       cpassword = tk.Label(frame1, text="Password", font=("arial", 15, "bold"), bg="white", fg="black").place(x=35, y=150)
       txt_cpassword = tk.Entry(frame1, font=("arial", 15), bg="lightgray", show=bullet,textvariable=var_cpassword).place(x=35, y=180)

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
                   name=str(var_fname.get())
                   con=pymysql.connect(host="sql11.freesqldatabase.com",user="sql11395303",password="KP5AULC8iS",database="sql11395303")
                   cur = con.cursor()

                   cur.execute("SELECT * FROM credentials WHERE username = %s AND password = %s", (var_fname.get(), var_cpassword.get()))
                   if cur.fetchone() is not None:

                       #success_msg = tk.Label(self, text="Succesful Login       ", font=("arial", 10, "bold"), bg="white",fg="green").place(x=480, y=300)
                       clear()

                       p3.show()
                   else:

                       fail_msg = tk.Label(self, text="Invalid Credentials", font=("arial", 10, "bold"), bg="white",fg="red").place(x=480, y=300)
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
       bullet = "\u2022"
       var_cpassword=tk.StringVar()
       cpassword = tk.Label(frame1, text="Password", font=("arial", 15, "bold"), bg="white",fg="black").place(x=35, y=125)
       txt_cpassword = tk.Entry(frame1, font=("arial", 15), bg="lightgray", show=bullet,textvariable=var_cpassword).place(x=35, y=150)

       var_ccpassword = tk.StringVar()
      # ccpassword = tk.Label(frame1, text="Email", font=("arial", 15, "bold"), bg="white",fg="black").place(x=35, y=100)
       txt_ccpassword = tk.Entry(frame1, font=("arial", 15), bg="lightgray", show=bullet,textvariable=var_ccpassword).place(x=35, y=190)

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
                    con=pymysql.connect(host="sql11.freesqldatabase.com",user="sql11395303",password="KP5AULC8iS",database="sql11395303")
                    cur=con.cursor()

                    cur.execute("select * from credentials where username=%s",var_fname.get())
                    #cur.execute("select * from credentials where username=%s",var_fname.get())
                    row=cur.fetchone()

                    #print(row)

                    if row!=None:
                        messagebox.showerror("Error","User already Exist, Please try with another username",parent=self)
                    else:
                        cur.execute("insert into credentials (id,username,password,email) values(%s,%s,%s,%s)",
                                    (str(uuid.uuid4()).replace('-',''),
                                     var_fname.get(),
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


       def displaySQLdata():
           def connect():
               con1 = pymysql.connect(host="sql11.freesqldatabase.com", user="sql11395303", password="KP5AULC8iS",database="sql11395303")
               con1.close()

           def View():
               con1 = pymysql.connect(host="sql11.freesqldatabase.com", user="sql11395303", password="KP5AULC8iS",database="sql11395303")
               cur1 = con1.cursor()
               cur1.execute("SELECT * FROM credentials")

               rows = cur1.fetchall()

               for row in rows:
                   tree.insert("", tk.END, values=row)
               con1.close()

           # connect to the database

           connect()
           root = tk.Tk()

           root.after(10000, lambda: root.destroy())

           root.resizable(False, False)
           root.title("E-Corp DisplayDB - Database={sql11395303} Table={credentials}")

           tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4"), show='headings')
           tree.column("#1", anchor=tk.CENTER)
           tree.heading("#1", text="ID")
           tree.column("#2", anchor=tk.CENTER)
           tree.heading("#2", text="Username")
           tree.column("#3", anchor=tk.CENTER)
           tree.heading("#3", text="Password")
           tree.column("#4", anchor=tk.CENTER)
           tree.heading("#4", text="Email")
           tree.pack()
           View()

           root.mainloop()


       def delete(id):
           print(id)
           con1 = pymysql.connect(host="sql11.freesqldatabase.com", user="sql11395303", password="KP5AULC8iS",database="sql11395303")
           cur = con1.cursor()
           cur.execute("DELETE FROM credentials WHERE id=%s", id)
           con1.commit()
           con1.close()
           var_id.set('')




       def deleteSQLdata():
           try:
               int_id_var=int(var_id.get())
               delete(int_id_var)
               messagebox.showinfo("Success", "User with ID="+str(int_id_var)+" had deleted!", parent=self)
           except:
               messagebox.showerror("Error","Please enter an integer data type!",parent=self)


       frame1 = tk.Frame(self, bg="#e2e2e2")
       frame1.place(x=620, y=40, width=330, height=350)
       ctr_panel_db = tk.Label(self, text="Database Control panel", font=("arial", 15, "bold"), bg="#e2e2e2", fg="black").place(x=675,y=40)
       info_db = tk.Label(self, text="1 - Display database data", font=("arial", 13), bg="#e2e2e2",fg="green").place(x=690, y=70)
       diplay_sql_data = tk.Button(self, text="Display",cursor="hand2", command=displaySQLdata).place(x=720,y=95,width=150)

       frame2 = tk.Frame(self, bg="#ffc4c4")
       frame2.place(x=690, y=130, width=200, height=110)
       del_db = tk.Label(self, text="2 - Delete database data", font=("arial", 13), bg="#ffc4c4", fg="red").place(x=695, y=130)

       var_id = tk.StringVar()
       del_id = tk.Label(self, text="Select ID:", font=("arial", 10), bg="#ffc4c4", fg="black").place(x=760,y=150)
       txt_id = tk.Entry(self, font=("arial", 15), bg="white", textvariable=var_id).place(x=715, y=170,width=150)
       delete_sql_data = tk.Button(self, text="Delete", cursor="hand2",command=deleteSQLdata).place(x=715, y=205,width=150)



      # msg_btn = tk.Button(self, text="OPEN MSG", cursor="hand2", command=msg_app).place(x=0, y=205,width=150)
       #wlc_msg = tk.Label(self, text="Login as: o magkos einai karkinos", font=("arial", 10, "bold"), bg="black", fg="white").place(x=30,y=0,height=30)

       #os.remove("username")




       #wlc_time = tk.Label(self, text=str(time.asctime(time.localtime(time.time()))), font=("arial", 15, "bold"), bg="black",fg="white").place(x=750, y=0, height=30)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = LoginPage(self)
        p2 = RegisterPage(self)
        p3 = afterLogin(self)
        p4 = MessengerAPP(self)

        global flag
        flag=False

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
    #root.wm_geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.resizable(False, False)
    #root.iconbitmap('icon.ico')
    root.title("E-Corp Software AdministratorUI")
    root.deiconify()
    root.mainloop()