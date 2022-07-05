import random

print()
print("Welcome to Rock Paper Scissors")

print()
user_input = input("Ready to Play...")
if user_input.lower() != "yes":
    print("Exiting Game")
    quit()

print()

# Score
computer_score = 0
user_score = 0

options = ["rock", "paper", "scissors"]


while True:
    print()
    user_input = input("Type Rock, Paper, Scissors or Q to quit...  ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock is 0, paper is 1 and scissors is 2
    computer_pick = options[random_number]
    print(f"Computer picked: {computer_pick}")

    if user_input == computer_pick:
        print("Draw")
    elif user_input == "rock" and computer_pick == "scissors":
        print("You win")
        user_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_score += 1

    else:
        print("You lost")
        computer_score += 1


print()
print(f"You won {user_score} games, the computer won {computer_score} games")
print("Game Over")
