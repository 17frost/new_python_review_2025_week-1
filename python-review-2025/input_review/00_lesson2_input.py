# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")

# Get two numbers from the user and ask for their name to personalize the experience

# get user input

name = input("What's your name ")
# this is input always a string
print(f"Welcome!, {name} We'll do some math.\n")
# this is output

# ask for your birthday
# ask for your favorite food
# ask for two numbers

birthday = input("when's ur birthday boy? ")
FavFood = input("whats ur fav food? ")
num1 = int(input("enter in a number "))
num2 = int(input("enter in a second number "))

print(f"Well, {name}, u was born in {birthday}, and u love eating {FavFood}")
print(f"your numbers are {num1} and {num2}")







# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings