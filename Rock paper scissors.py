import random
print("== Rock Paper Scissors ==")
choices = ["rock","paper","scissors"]
user = input("Your choice: ").lower()
computer = random.choice(choices)
print(f"Computer chose: {computer}")
if user == computer:
    print("It's a Tie!")
elif (user=="rock"and computer == "scissors") or \
     (user=="paper"and computer =="rock") or \
     (user=="scissors"and computer =="paper"):
     print("You Win! 🎉")
else:
    print("Computer Wins")   
     