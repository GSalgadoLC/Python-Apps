print("Welcome to my computer quiz")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    print("Game Exited")
    quit()

print("Okay lets play")

score = 0
questions = 4

answer = input("What does cpu stand for:    ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print()
print(f"your current score is {score}")

answer = input("What does GPU stand for:    ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print()
print(f"your current score is {score}")


answer = input("What does RAM stand for:    ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print()
print(f"your current score is {score}")


answer = input("What does PSU stand for:    ")

if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print()
print(f"your total score is {score} out of {questions}")
print(f" { (score / questions) * 100 } % ")

quit()
