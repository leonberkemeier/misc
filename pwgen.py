import secrets
password = ""
characters = "012345679abcdefghijklmnopqrstuvwxyz"
password_length = 8




print('length of the pw')

x = input()
password_length=int(x) 
for i in range (0,password_length):
    password_characters = secrets.choice(characters)
    password = password + password_characters

print("The Password is : " + password)