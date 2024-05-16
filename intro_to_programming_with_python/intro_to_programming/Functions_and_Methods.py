"""
Write a program that uses a multiply function to multiply two numbers 
and returns the result. Ask the user to enter the two numbers, then 
output the numbers and result as a simple equation.
"""


def multiply(num1, num2):
    result = num1 * num2
    return f"{num1} * {num2} = {result}"


def get_numbers():
    num = int(input("num: "))
    return num


print(multiply(get_numbers(), get_numbers()))
"""
se this function to determine which of the following lists contains
at least one number that is not evenly divisible by 3
"""


# print(any(remainders_3(numbers_1)))
# print(any(remainders_3(numbers_2)))
# print(any(remainders_3(numbers_3)))
# print(any(remainders_3(numbers_4)))

"""
Use this function to determine which of the following lists do not 
contain any numbers that are divisible by 5:
"""
