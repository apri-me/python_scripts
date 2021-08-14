from random import randint
from math import ceil, floor

# rounding_functions = (ceil, floor)

print("Welcome to \"Guess Number Game\"")
a = 1
b = 1023
print(f"Guess a number between {a} to {b}")
tries = 0
while True:
    tries += 1
    n = int(input(f"Guess: "))
    if n - a == b - n == 0:
        print("Thats right, you win.")
        print(f"Tries: {tries}")
        break
    if n - a > b - n or (n - a == n - b and randint(0, 1)):
        b = n - 1
        print("Lower. ")
    else:
        a = n + 1
        print("Higher. ")
