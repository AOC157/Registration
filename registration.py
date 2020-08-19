class SignIn:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(username + " " + password + " in")


class SignUp:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(username + " " + password + " up")

        
mode = input("enter mode: sign ")
username = input("Please enter your username")
password = input("Please enter your password")

if mode == "in":
    user = SignIn(username,password)
    
elif mode == "up":
    user = SignUp(username,password)

