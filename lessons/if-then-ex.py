"""Practice with If Then Statements."""

choice: int = int(input("Pick a Number:"))

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("D")
        else:
            print("C")