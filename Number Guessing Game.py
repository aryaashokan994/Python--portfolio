import random

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100")

secret_number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congrats! You got it in {guesses} guesses!")
        break