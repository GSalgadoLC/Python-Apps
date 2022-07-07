# Password Manager
# Details encrpted

from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        '''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User: ", user, "Password: ",
                  fer.decrypt(password.encode()).decode())


def add():
    input_name = input("Account name:  ")
    input_password = input("Password:  ")

    with open("password.txt", 'a') as f:
        f.write(input_name + "|" +
                fer.encrypt(input_password.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones(view,add). q to quit:  ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
        # write_key()
    elif mode == "add":
        add()
    else:
        print("Please select a valid mode")
        continue

# Notes
# b"string" is != "string"
# byte string and string are different
