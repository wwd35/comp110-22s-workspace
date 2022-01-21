"""An example of conditional (if-else) statements."""

SECRET: int = 3

name: str = (input("What is your name?"))
print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("Have a wonderful day, " + str(name) + ".")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed to high, " + name + "!")
    else:
        print("You guessed too low, " + name + "!")

print("Game over.")
