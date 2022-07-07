# Password Manager
# Details encrpted

from cryptography.fernet import Fernet

master_password = input("What is the master password:  ")


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb")


def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User: ", user, "Password: ", password)


def add():
    input_name = input("Account name:  ")
    input_password = input("Password:  ")

    with open("password.txt", 'a') as f:
        f.write(input_name + "|" + input_password + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones(view,add). q to quit:  ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Please select a valid mode")
        continue
