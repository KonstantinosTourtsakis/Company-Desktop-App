import tkinter as tk
from PIL import ImageTk, Image
import time;

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

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
       localtime = tk.Label(self, text="Local current time: "+str(time.asctime(time.localtime(time.time()))), font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=550, y=51)
       title = tk.Label(frame1, text="Sign In", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=240, y=20)


       f_name = tk.Label(frame1, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=35, y=60)
       txt_fname = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=35, y=90)

       cpassword = tk.Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=35, y=150)
       txt_cpassword = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=35, y=180)

       self.login_img = ImageTk.PhotoImage(file="login.png")
       loginimg = tk.Button(frame1, image=self.login_img, cursor="hand2", bd=0).place(x=300, y=85)




class RegisterPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.bg = ImageTk.PhotoImage(file="background.jpg")
       bg = tk.Label(self, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)
       localtime = tk.Label(self, text="Local current time: " + str(time.asctime(time.localtime(time.time()))),font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=550, y=51)
       # left image==
       self.left = ImageTk.PhotoImage(file="left-logo.png")
       left = tk.Label(self, image=self.left).place(x=60, y=80, width=335, height=303)

       # login frame
       frame1 = tk.Frame(self, bg="white")
       frame1.place(x=390, y=80, width=550, height=303)

       title = tk.Label(frame1, text="Register", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=240, y=20)

       f_name = tk.Label(frame1, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=35, y=65)
       txt_fname = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=35, y=90)

       cpassword = tk.Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=35, y=125)
       txt_cpassword = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=35, y=150)

      # ccpassword = tk.Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=35, y=100)
       txt_ccpassword = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=35, y=190)

       email = tk.Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=35, y=225)
       txt_email = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray").place(x=35, y=250)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = LoginPage(self)
        p2 = RegisterPage(self)
        p3 = Page3(self)



        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.register_img = ImageTk.PhotoImage(file="register.png")
        p1.registerimg = tk.Button(p1, image=p1.register_img, cursor="hand2", bd=0, command=p2.lift).place(x=690, y=250)


        p2.register_img = ImageTk.PhotoImage(file="register.png")
        p2.registerimg = tk.Button(p2, image=p2.register_img, cursor="hand2", bd=0).place(x=690, y=165)

        p2.login_img = ImageTk.PhotoImage(file="login.png")
        p2.loginimg = tk.Button(p2, image=p2.login_img, cursor="hand2", bd=0,command=p1.lift).place(x=690, y=250)


        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x500+0+0")
    root.resizable(False, False)
    root.title("E-Corp Software")
    root.mainloop()