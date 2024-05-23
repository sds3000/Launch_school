from pprint import pp

"""
Concatenate two strings, one with your first name and one with your last, 
to create a new string with your full name as its value. For example, 
if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.
"""

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print(last_name, first_name, sep=", ", end=".")

# print(first + " " + last)

"""
This question may be a little challenging if your math skills are rusty. 
Don't be afraid to take advantage of the hints. Try your best to solve the problem, 
but don't feel compelled to complete it if you become frustrated.

Use the REPL and the arithmetic operators to extract the individual digits of 4936:
"""
num = 4936

ones = num % 10
tens = (num // 10) % 10
hundreds = (num // 100) % 10
thousands = (num // 1000) % 10
print(
    f"Ones place: {ones}\nTens place: {tens}\nHundreds place: {hundreds}\nThousands place: {thousands}"
)


# turns number into a string and calls them by index


# Refactor the code from the previous exercise to use coercion to print 15 instead.
