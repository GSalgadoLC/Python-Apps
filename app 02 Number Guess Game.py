import random

print("Welcome to guess the number 0-100 game")

user_input = input("Would you like to play? ")
if user_input.lower() != "yes":
    print("Exiting Game")
    quit()

print()
print("Let's get started")
top_of_range = input("Enter a number to be the top of range     ")
print()

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than zero next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randrange(top_of_range)
print(random_number)

tries = 0

while True:
    print()
    user_guess = input("Guess a number:  ")
    tries += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a valid number next time")
        continue

    if user_guess == random_number:
        print()
        print("!!!!  You got it  !!!")
        break

    elif user_guess < random_number:
        print(f"Its greater than {user_guess}, Try Again")

    else:
        print(f"Its less than {user_guess}, Try Again")

print(f"You took {tries} tries to guess the number")
print("     GAME OVER")
print()
