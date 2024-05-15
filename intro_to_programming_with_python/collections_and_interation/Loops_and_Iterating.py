from pprint import pp
import random

my_list = [6, 3, 0, 11, 20, 4, 17]

# for x in my_list:
#     print(x)
# x = 0


# while x < len(my_list):
#     if my_list[x] % 2 == 0:
#         print(my_list[x])

#     x += 1
# for x in my_list:
#     if x % 2 == 0:
#         continue
#     print(x)
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
# for x in my_list:
#     for y in x:
#         if y % 2 == 1:
#             continue
#         print(y)
my_list = [
    1,
    3,
    6,
    11,
    4,
    2,
    4,
    9,
    17,
    16,
    0,
]
# lst = []
# for x in my_list:
#     if x % 2 == 0:
#         lst.append("even")
#         continue
#     lst.append("odd")
# lst1 = ["even" if x % 2 == 0 else "odd" for x in my_list]
# pp(lst1)

# my_tuple = (1, "a", "1", 3, [7], 3.1415, -4, None, {1, 2, 3}, False)


# def find_integers(tup):
#     lst = []
#     for x in tup:
#         if type(x) is int:
#             lst.append(x)
#     return lst


# integers = find_integers(my_tuple)
# print(integers)  # [1, 3, -4]
# my_set = {
#     "Fluffy",
#     "Butterscotch",
#     "Pudding",
#     "Cheddar",
#     "Cocoa",
# }
# dictionary = {x: len(x) for x in my_set}
# print(dictionary)

# x = int(input("Enter a number "))
# y = [f"{i}" for i in range(x)]
# print(y)

# lst = 1
# for i in range(x):
#     lst *= i + 1
# print(f"{x}! = {lst}")


# highest = 10

# while True:

#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
x = 0
y = 0
while True:
    while True:
        if my_list[x][y] % 2 == 0:
            print(my_list[x][y])
        y += 1
        if y == len(my_list[x]):
            x += 1
            y = 0
        if x == len(my_list):
            break
    break
