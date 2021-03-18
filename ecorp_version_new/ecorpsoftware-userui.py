import tkinter as tk
from tkinter import ttk,messagebox,font
from PIL import ImageTk, Image
import pymysql
import time
import threading
#from vidstream import StreamingServer
import os
import webbrowser


#TKINTER MAIN SHOW FRAME
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

#NOTHING
class MessengerAPP(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

#LOGIN PAGE FRAME
class LoginPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       p3 = afterLogin(self)

       screen_width = self.winfo_screenwidth()
       screen_height = self.winfo_screenheight()

       buttonframe = tk.Frame(self)
       container = tk.Frame(self)
       buttonframe.pack(side="top", fill="x", expand=False)
       container.pack(side="top", fill="both", expand=True)

       def quit(self):
           self.destroy()


       p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


  #     self.configure(bg='blue')
       self.bg = ImageTk.PhotoImage(file="images/clientui/user-background.png")
       bg = tk.Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)



       #center image==
       self.left = ImageTk.PhotoImage(file="images/clientui/user-center-logo.png")
       left = tk.Label(self, image=self.left).place(relx=0.5, y=screen_height/2.5, width=335, height=303,anchor='s')




       self.quit_img = ImageTk.PhotoImage(file="images/clientui/user-exit.png")
       quitimg = tk.Button(self, image=self.quit_img, cursor="hand2", highlightthickness = 0, bd = 0,command=self.quit).place(x=10, y=20)

       # login frame

       self.centeremp=ImageTk.PhotoImage(file="images/clientui/employer-login.png")
       centeremp=tk.Label(self,image=self.centeremp).place(relx=0.5, y=screen_height/2,width=65, height=65,anchor='center')

      # localtime = tk.Label(self, text="Local current time: " + str(time.asctime(time.localtime(time.time()))),font=("arial", 10, "bold"), bg="white", fg="black").place(x=640, y=360)
       #title = tk.Label(frame1, text="Sign In", font=("arial", 15, "bold"), bg="white",fg="black").place(x=240, y=20)



      # Employee=tk.Label(frame1, text="Employee Login", font=("arial", 15, "bold"), bg="#82defb", fg="black").place(x=75, y=15)
       var_fname = tk.StringVar()
       f_name = tk.Label(self, text="E-Corp Employee login system", font=("arial", 15, "bold"), bg="#82defb", fg="black").place(relx=0.5, rely=0.6,anchor='center')
       txt_fname = tk.Entry(self, font=("arial", 15), bg="white",textvariable=var_fname).place(relx=0.5, y=screen_height/1.5,anchor='center')


       bullet = "\u2022"
       var_cpassword = tk.StringVar()
       #cpassword = tk.Label(self, text="Password", font=("arial", 15, "bold"), bg="#82defb", fg="black").place(relx=0.5, rely=0.8,anchor='center')
       txt_cpassword = tk.Entry(self, font=("arial", 15), bg="white", show=bullet,textvariable=var_cpassword).place(relx=0.5, y=screen_height/1.4,anchor='center')


       var_chk=tk.IntVar()
       chk=tk.Checkbutton(self,font=("arial", 8),text="I Agree the Terms & Conditions",bg="#82defb",variable=var_chk).place(relx=0.5, y=screen_height/1.3,anchor='center')

       def termsanconditions():
           messagebox.showinfo("Terms & Conditions", "Facebook has responded in a statement, saying the data uncovered is, and always has been, obtained through means that users themselves agreed to.ADVERTISEMENT“Call and text history logging is part of an opt-in feature for people using Messenger or Facebook Lite on Android...people have to expressly agree to use this feature.”In fact, you haven’t just agreed to a personal call log, but many other things the social media site has on file, including (but not limited to) your current or past addresses, all apps you have added, places you’ve checked into, your birthday, pending friend requests, deleted friends, your education, email address (even those you’ve removed), events you have been invited to, your last location, and phone numbers of people who don’t necessarily have Facebook. Facebook also records every IP address you’ve ever logged into Facebook from, and geographical coordinates of these logins. And has facial recognition data based on photographs you are tagged in. Come as a surprise? If you have agredto share this information without even realising it, then what else have you agreed to? went through Facebook’s legal terms (last updated on 31 January 2018) to find out. ", parent=self)

       self.term_img = ImageTk.PhotoImage(file="images/clientui/term-info.png")
       termimg = tk.Button(self, image=self.term_img, cursor="hand2", highlightthickness=0, bd=0,command=termsanconditions).place(relx=0.6, y=screen_height / 1.3, anchor='center')
       # CODE FOR LOGIN WITH DATABASE SQL

       mb_size = tk.Label(self, text="Software Version: DEMO", font=("arial", 10, "bold"),bg="#82defb", fg="#afe8fa").place(relx=1,anchor='ne')

       mb_size=tk.Label(self, text="Available Space in Database: 0.4% of 5.00MB", font=("arial", 10, "bold"), bg="#afe8fa", fg="black").place(relx=0.5, y=screen_height/1.1,anchor='s')
       def clear():
           var_fname.set('')
           var_cpassword.set('')


       loginas = var_fname.get()
       def login_data():
           if var_fname.get() == "" or var_cpassword.get() == "":
               messagebox.showerror("Error", "All fields Are Required", parent=self)
           elif var_chk.get()==0:
               messagebox.showinfo("Terms & Conditions", "Please agree terms & conditions", parent=self)

           else:
               try:

                   con=pymysql.connect(host="sql11.freesqldatabase.com",user="sql11395303",password="KP5AULC8iS",database="sql11395303")
                   cur = con.cursor()

                   cur.execute("SELECT * FROM credentials WHERE username = %s AND password = %s", (var_fname.get(), var_cpassword.get()))
                   if cur.fetchone() is not None:
                       cur.close()
                       #success_msg = tk.Label(self, text="Succesful Login       ", font=("arial", 10, "bold"), bg="white",fg="green").place(x=480, y=300)
                       clear()

                       p3.show()
                   else:

                       fail_msg = tk.Label(self, text="Invalid Credentials", font=("arial", 10, "bold"), bg="#82defb",fg="red").place(relx=0.5, y=screen_height/1.2,anchor='s')
                       clear()

               except Exception as es:
                   messagebox.showerror("Error", f"Error duo to: {str(es)}", parent=self)

       self.login_img = ImageTk.PhotoImage(file="images/clientui/user-login.png")
       loginimg = tk.Button(self, image=self.login_img, cursor="hand2", highlightthickness = 0, bd = 0, command=login_data).place(relx=0.6, y=screen_height/1.4,anchor='center')

#AFTER LOGIN FRAME
class afterLogin(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)


       #AFTER LOGIN INTERFACE


       #def messengerAPP():
            #g = GUI()
       screen_width = self.winfo_screenwidth()
       screen_height = self.winfo_screenheight()


       def open_apps_explorer():
           os.system("explorer")

       def quit(self):
           self.destroy()

       def open_apps_notepad():
           os.system("notepad.exe")

       def open_apps_firefox():
           webbrowser.open('https://github.com/KonstantinosTourtsakis/Monitoring-App')
        #background
       self.bg = ImageTk.PhotoImage(file="images/clientui/user-background.png")
       bg = tk.Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

       self.quit_img = ImageTk.PhotoImage(file="images/clientui/user-exit.png")
       quitimg = tk.Button(self, image=self.quit_img, cursor="hand2", highlightthickness=0, bd=0, command=self.quit).place(x=10, y=20)

     #  self.logout_img = ImageTk.PhotoImage(file="user-logout.png")
     #  logoutimg = tk.Button(self, image=self.logout_img, cursor="hand2", highlightthickness=0, bd=0,).place(x=45, y=20)

       # left image==
    #   self.left = ImageTk.PhotoImage(file="left-logo.png")
     #  left = tk.Label(self, image=self.left).place(x=60, y=80, width=335, height=303)

       self.left = ImageTk.PhotoImage(file="images/clientui/user-center-logo.png")
       left = tk.Label(self, image=self.left).place(relx=0.5, y=screen_height/2.5, width=335, height=303,anchor='s')



       apps_frame = tk.Frame(self, bg="#afe8fa")
       apps_frame.place(x=screen_width/1, rely=0.2, anchor='e', width=450, height=250)


       ctr_panel = tk.Label(apps_frame, text="Applications", font=("arial", 15, "bold"), bg="#afe8fa", fg="white").place(relx=0.5, rely=0.1, anchor='center')


       self.noteepad=ImageTk.PhotoImage(file="images/clientui/notepad.png")
       noteepad= tk.Button(apps_frame, image=self.noteepad,cursor="hand2", highlightthickness=0, bd=0, command=open_apps_notepad).place(relx=0.5, rely=0.5, anchor='center', width=40, height=37)

       self.firefox = ImageTk.PhotoImage(file="images/clientui/firefox.png")
       firefox = tk.Button(apps_frame, image=self.firefox, cursor="hand2", highlightthickness=0, bd=0,command=open_apps_firefox).place(relx=0.4, rely=0.5, anchor='center', width=40, height=37)

       self.zoom = ImageTk.PhotoImage(file="images/clientui/zoom.png")
       zoom = tk.Button(apps_frame, image=self.zoom, cursor="hand2", highlightthickness=0, bd=0,).place(relx=0.6, rely=0.5, anchor='center', width=40, height=37)

       self.filex = ImageTk.PhotoImage(file="images/clientui/explorer.png")
       filex = tk.Button(apps_frame, image=self.filex, cursor="hand2", highlightthickness=0, bd=0,command=open_apps_explorer).place(relx=0.7, rely=0.5, anchor='center', width=40, height=37)



"""
       #wlc_msg = tk.Label(self, text="Login as: o magkos einai karkinos", font=("arial", 10, "bold"), bg="black", fg="white").place(x=30,y=0,height=30)

       #os.remove("username")

       #wlc_time = tk.Label(self, text=str(time.asctime(time.localtime(time.time()))), font=("arial", 15, "bold"), bg="black",fg="white").place(x=750, y=0, height=30)
"""


#START PROGRAM MAINVIEW FRAME
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = LoginPage(self)
     #   p2 = RegisterPage(self)
        p3 = afterLogin(self)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)


        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
 #       p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)



        p1.show()




if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    #root.wm_geometry("1000x500+0+0")

    #root.wm_geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    #root.resizable(False, False)
    root.attributes('-fullscreen',True)

    #root.iconbitmap('icon.ico')
    root.title("E-Corp Software ClientUI")

    root.mainloop()
