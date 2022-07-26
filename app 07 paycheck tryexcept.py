user_hours = (input("How many hours did you work \n"))
user_rate = (input("What is your pay rate? \n"))


try:
    if int(user_hours) > 0 and int(user_rate) > 0:

        pay = int(user_hours)*int(user_rate)
        gross_pay = pay

        if (int(user_hours)-40) > 0:
            gross_pay = ((int(user_hours)-40)*(int(user_rate)*.5))+pay
            print(f'Your gross pay is {gross_pay}')
        else:
            print(f'Your gross pay is {gross_pay}')
    else:
        print("please enter valid inputs")

except:
    print("please enter valid inputs")
