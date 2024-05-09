"""
Write a program that uses a multiply function to multiply two numbers 
and returns the result. Ask the user to enter the two numbers, then 
output the numbers and result as a simple equation.
"""


def multiply():
    num1 = int(input("enter num"))
    num2 = int(input("enter num2"))
    return num1 * num2


# print(multiply())
"""
se this function to determine which of the following lists contains
at least one number that is not evenly divisible by 3
"""


def remainders_3(numbers):
    return [number % 3 for number in numbers]


numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

# print(any(remainders_3(numbers_1)))
# print(any(remainders_3(numbers_2)))
# print(any(remainders_3(numbers_3)))
# print(any(remainders_3(numbers_4)))

"""
Use this function to determine which of the following lists do not 
contain any numbers that are divisible by 5:
"""


def remainders_5(numbers):
    return [number % 5 for number in numbers]


numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []
print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
