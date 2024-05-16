"""
Write a program named greeter.py that greets 'Victor' three times. 
Your program should use a variable and not hard code the string value 
'Victor' in each greeting.
"""

name = "Viktor"
print(f"Hello {name}\n" * 3)

"""
Write a program named age.py that includes someone's age and then 
calculates and reports the future age 10, 20, 30, and 40 years from now. 
Here's the output for someone who is 22 years old.
"""

age = int(input("What age are you? "))
for x in range(10, 50, 10):
    print(f"In {x} years, you will be {age  + x} years old.")

"""
Assume you have $1,000.00 in the bank, and you've somehow managed to 
find a bank that pays you 5% (this is a wish-fulfillment fantasy) 
compounded interest every year. After one year, you will have $1,050 
($1,000 times 1.05). After two years, you will have $1,050 times 1.05, 
or $1102.50. Create a variable named balance that contains the amount 
of money you will have after 5 years, then print the result. Use a single 
expression if you can to set balance to the correct value.
"""

balance = 1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05
print(balance)

"""
Repeat the previous question but, this time, use augmented assignment 
to compute the final result, one year at a time.
"""
balance = 1000
for x in range(5):
    balance *= 1.05
    print(balance)
