from logging import raiseExceptions


user_input = (input("Please enter a number between 0.0  and 1.0 \n"))

try:
    if (float(user_input) > 1) or (float(user_input) < 0):
        raiseExceptions
        print("please enter a valid input")
    else:
        if float(user_input) >= 0.9:
            print("A")
        elif float(user_input) >= 0.8:
            print("B")
        elif float(user_input) >= 0.7:
            print("C")
        elif float(user_input) >= 0.6:
            print("D")
        elif float(user_input) < 0.6:
            print("F")
except:
    print("Please enter a number in the valid range of 0.0 and 1.0")
