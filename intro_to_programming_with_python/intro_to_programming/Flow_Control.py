"""
Write a function, even_or_odd, that determines whether its 
argument is an even or odd number. If it's even, the function 
should print 'even'; otherwise, it should print 'odd'. Assume the argument 
is always an integer.
"""


def even_or_odd(num):
    return "even" if num % 2 == 0 else "odd"


# print(even_or_odd(7))


def caps(str):
    print(str.upper() if len(str) > 10 else str)


# caps("yo")


def caps(str):
    if len(str) > 10:
        print(str.upper())
    else:
        print(str)


# caps("hello world!!!!")
