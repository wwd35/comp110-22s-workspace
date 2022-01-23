"""Wordle Coding Assignment WD."""

__author__ = "730394476"

word: str = str(input("Enter a 5-character word:"))

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = str(input("Enter a single character:"))

if len(letter) != 1:
    print("Error: Character must contain a single character")
    exit()

instance: int = 0
print("Searching for " + letter + " in " + word)


if letter is word[0]:
    print(letter + " found at index 0.")
    instance = instance + 1
if letter is word[1]:
    print(letter + " found at index 1.")
    instance = instance + 1
if letter is word[2]:
    print(letter + " found at index 2.")
    instance = instance + 1
if letter is word[3]:
    print(letter + " found at index 3.")
    instance = instance + 1
if letter is word[4]:
    print(letter + " found at index 4.")
    instance = instance + 1

if instance == 1:
    print(str(instance) + " instance of " + letter + " found in " + word)
else:
    if instance > 0:
        print(str(instance) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)