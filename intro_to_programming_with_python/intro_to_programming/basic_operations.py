"""
Concatenate two strings, one with your first name and one with your last, 
to create a new string with your full name as its value. For example, 
if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.
"""

first = "shane"
last = "smith"
# print(first + " " + last)

"""
This question may be a little challenging if your math skills are rusty. 
Don't be afraid to take advantage of the hints. Try your best to solve the problem, 
but don't feel compelled to complete it if you become frustrated.
"""


# turns number into a string and calls them by index
def numb_extrapalator(num):
    string = str(num)
    print(
        f"One place is {string[3]}\n",
        f"Tens place is {int(string[2])}\n",
        f"Hundred place is {int(string[1])}\n",
        f"Thousands place is {int(string[0])}",
    )


numb_extrapalator(4396)


def math_way(num):
    tens = (num // 10) % 10
    hund = (num // 100) % 10
    thou = num // 1000
    print(
        f"One place is {num %10}\n",
        f"Tens place is {tens}\n",
        f"Hundred place is {hund}\n",
        f"Thousands place is {thou}",
    )


math_way(4396)

# Refactor the code from the previous exercise to use coercion to print 15 instead.

print(int(5) + int(10))
