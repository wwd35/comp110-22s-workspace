"""Example memory diagram program."""

age: int = int(input("How old are you? "))
year: int = int(input("What year is it? "))
age_in_2091: int = 2091 - year + age
print("In 2091, you will be " + str(age_in_2091))

age = age + 1
year = year + 1
print("In " + str(year) + ", you will be " + str(age))
