import tkinter
from tkinter import *

class SignIn:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(username + " " + password + " in!")

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
        print(username + " " + password + " up!")

    def save(self,username,password):
        usernameFile = open("username.txt","a")
        passwordFile = open("password.txt","a")
        
        usernameFile.write(username + '\n')
        usernameFile.close

        passwordFile.write(password + '\n')
        passwordFile.close    

top = tkinter.Tk()
top.geometry("300x200")
top.bg = "yellow"

var = IntVar()
R1 = Radiobutton(top, text="Sign in", variable=var, value=1,font = 30)
R1.pack()
R1.place(x = 40 , y = 20)

R2 = Radiobutton(top, text="Sign up", variable=var, value=2,font = 30)
R2.pack()
R2.place(x = 160 , y = 20)

L1 = Label(top, text="User Name")
L1.pack()
L1.place(x = 20,y = 70)
E1 = Entry(top, bd =5)
E1.pack()
E1.place(x = 120,y = 70)

L1 = Label(top, text="Pass Word")
L1.pack()
L1.place(x = 20,y = 100)
E1 = Entry(top, bd = 5 , show = "*")
E1.pack()
E1.place(x = 120,y = 100)

B = tkinter.Button(top,text ="Import",
                   activebackground = "Green",
                   activeforeground = "blue",
                   bd = 5,
                   font = 30
                   )
B.pack()
B.place(x = 90, y = 140,width = 100)
if mode == "in":
    user = SignIn(username,password)
    if user.load():
        print("you succesfully signed in \"" + username + "\"")
    else:
        print("your password may be incorrect or your username doesn't exist")
    
elif mode == "up":
    user = SignUp(username,password)
    user.save(username,password)
    print("\"" + username + "\"! you succesfully signed up")

top.mainloop()
