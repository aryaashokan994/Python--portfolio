name = input("What is your name? ")
print("Hello", name, "Welcome to python in VS Code!")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", num1 + num2)
secret = 7
guess = int(input("Guess a number from 1 to 10: "))
if guess == secret:
    print("You got it!")
else:
    print("Nope, try again. It was", secret)
    