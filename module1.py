import random 
import string  

length = 8 

# randomly selects characters from letters and numbers to create username and password

genusername = "".join(
    random.choices(string.ascii_letters + string.digits, k=length)
)

genpassword = "".join(
    random.choices(string.ascii_letters + string.digits, k=length)
)

 
while True:
    print(f"randomly generated username: {genusername}") 
    userusername = input("select a new username: ") 
    usernameselect = input("verify your username: ") 
    if usernameselect == userusername or usernameselect == genusername: 
        print("username saved!") 
        break   
    else: 
        print("usernames do not match. try again.\n") 


while True: 
    print(f"randomly generated password: {genpassword}") 
    userpassword = input("select a new password: ") 
    passwordselect = input("verify your password: ") 
    if passwordselect == userpassword or passwordselect == genpassword: 
        print("password saved!")
        break   
    else: 
        print("passwords do not match. try again.\n") 


openfile = input("would you like to access the file y/n: ").lower() 
if openfile == "y":
    checkusername = input("Username: ") 
    checkpassword = input("Password: ") 
    if checkusername == userusername or checkpassword == userpassword:
        with open("thetextdocument.txt", "w") as file: 
            file.write("you have entered, well done") 
        print("File tickled successfully...go have a look...") 
    else: 
        print("Incorrect login details. o_o") 
else: 
  print("okay, screw you then") 

 


