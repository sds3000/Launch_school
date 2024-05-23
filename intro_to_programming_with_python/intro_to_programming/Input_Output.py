"""
Write a program named greeter.py. The program should ask for 
your name, then output Hello, NAME! where NAME is the name you 
entered:
"""

name = input("name? ")
print(f"Hello, {name}")

"""Modify the greeter.py program to ask for the user's first 
and last names separately, then greet the user with their 
full name.
"""
first_name = input("first name")
last_name = input("last name? ")
print(f"hello, {first_name} {last_name}")
"""
Write a program named age.py that asks the user to enter their 
age, then calculates and reports the future age 10, 20, 30, and 
40 years from now.
"""

age = int(input("age?"))

for x in range(10, 50, 10):
    print(f"In {x} years, you will be {age + x} years old")
