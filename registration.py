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

        
mode = input("enter mode: sign ")
username = input("Please enter your username: ")
password = input("Please enter your password: ")

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

