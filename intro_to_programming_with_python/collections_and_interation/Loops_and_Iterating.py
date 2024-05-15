from pprint import pp

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
lst = []
for x in my_list:
    if x % 2 == 0:
        lst.append("even")
        continue
    lst.append("odd")
pp(lst)
