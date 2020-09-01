import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.font as font


class SignIn:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def load(self):
        userCounter = 0
        usernameFile = open("username.txt","r")
        passwordFile = open("password.txt","r")
        username = usernameFile.readline()
        while(username != self.username + '\n'):
            userCounter += 1
            username = usernameFile.readline()
            if(username == ""):
                usernameFile.close()
                passwordFile.close()
                return False
        passCounter = 0
        while (passCounter < userCounter):
            passwordFile.readline()
            passCounter += 1
        password = passwordFile.readline()
        if (password == self.password + '\n'):
            usernameFile.close()
            passwordFile.close()
            return True

        else:
            print(password)
            usernameFile.close()
            passwordFile.close()
            return False


class SignUp:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save(self):
        usernameFile = open("username.txt","a")
        passwordFile = open("password.txt","a")
        
        usernameFile.write(self.username + '\n')
        usernameFile.close

        passwordFile.write(self.password + '\n')
        passwordFile.close    

top = tkinter.Tk()
top.configure(bg = "yellow")
top.geometry("300x200")
top.iconbitmap("icon.ico")
top.title("sign in/up")
top.resizable(False, False)

radioFont = font.Font(family="Times New Roman",size = 15)
labelFont = font.Font(family="Arial",size = 11)
buttonFont = font.Font(family="Times New Roman",size = 13)


var = IntVar()    
R1 = Radiobutton(top, text="Sign in",width = 11,height = 2, variable=var, value=1,
            bg = "gold",activebackground = "maroon",activeforeground = "white")
R1['font'] = radioFont
R1.pack()
R1.place(x = 0 , y = 0)

R2 = Radiobutton(top, text="Sign up",height = 2,width = 11, variable=var, value=2,
            bg = "goldenrod",activebackground = "blue",activeforeground = "white")
R2['font'] = radioFont
R2.pack()
R2.place(x = 150 , y = 0)

L1 = Label(top, text="Username",bg = "yellow")
L1['font'] = labelFont
L1.pack()
L1.place(x = 25,y = 75)

E1 = Entry(top, bd =5)
E1.pack()
E1.place(x = 125,y = 75)

L2 = Label(top, text="Password",bg = "yellow")
L2['font'] = labelFont
L2.pack()
L2.place(x = 25,y = 105)

E2 = Entry(top, bd = 5 , show = "*")
E2.pack()
E2.place(x = 125,y = 105)


def check():
    username = E1.get()
    password = E2.get()
    if(var.get() == 1):
        user = SignIn(username,password)
        if user.load():
            msg.showinfo("Sign in","you succesfully signed in \"" + username + "\"")
        else:
            msg.showinfo("Sign in","your password may be incorrect or your username doesn't exist")

    elif (var.get() == 2):
        user = SignUp(username,password)
        user.save()
        msg.showinfo("Sign up","\"" + username + "\"! you succesfully signed up")

    else:
         msg.showinfo( "warning", "you don't choose any mode")

B = tkinter.Button(top,text ="Import",
                   command = check,
                   activebackground = "springgreen4",
                   activeforeground = "gray99",
                   bd = 5, bg = "deep sky blue")
B['font'] = buttonFont
B.pack()
B.place(x = 100, y = 145,width = 100)


top.mainloop()
