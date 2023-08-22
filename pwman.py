from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open ("key.key","wb") as key_file:
        key_file.write(key)"""

def load_key():
    return open ("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Whats the master pword    ")

key = load_key() + master_pwd.encode()

fer = Fernet (key)

def anschauen():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print ( "Verwendung:", user, "Passwort", fer.decrypt(passw.decode))

def hinzufügen():
    name = input("Name des Accounts: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode) + "\n")


while True:
    mode = input ("Altes PWD anschauen (anschauen) oder NEUES PWD hinzufügen (hinzufügen)   ?")
    if mode == "b":
        break
    if mode == "anschauen":
        anschauen()
    elif mode == "hinzufügen":
        hinzufügen()
    else:
        print("Unzureichende Informationen")
