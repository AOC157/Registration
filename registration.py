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

    def save(self,username,password):
        usernameFile = open("username.txt","a")
        passwordFile = open("password.txt","a")
        
        usernameFile.write(username + " ")
        usernameFile.close

        passwordFile.write(password + " ")
        passwordFile.close    

        
mode = input("enter mode: sign ")
username = input("Please enter your username")
password = input("Please enter your password")

if mode == "in":
    user = SignIn(username,password)
    
elif mode == "up":
    user = SignUp(username,password)
    user.save(username,password)

