"""
Write a program named greeter.py. The program should ask for 
your name, then output Hello, NAME! where NAME is the name you 
entered:
"""

name = input("What is your name? ")

print(f"Hello, {name}")

"""Modify the greeter.py program to ask for the user's first 
and last names separately, then greet the user with their 
full name.
"""

first = input("What is your first name? ")
last = input("What is your last name? ")

print(f"Hello, {first} {last}!")

"""
Write a program named age.py that asks the user to enter their 
age, then calculates and reports the future age 10, 20, 30, and 
40 years from now.
"""

age = int(input("How old are you? "))
years = 10

while years <= 40:
    print(f"In {years}, you will be {age + years} years old.")
    years += 10
