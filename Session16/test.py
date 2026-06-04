# # str.translate() & str.maketrans()
# table = str.maketrans(
#     "",
#     "",
#     "- ()."
# )

# phone = "(098) 123-4567"

# print(phone.translate(table))

# TODO: Map
# numbers = [1, 2, 3, 4]

# result = list(map(lambda x: x * 2, numbers))

# print(result)

# VD 2
# names = [
#     "nguyen van a",
#     "tran thi b",
#     "le van c"
# ]

# result = list(map(str.title, names))

# print(result)

# TODO: filter
# numbers = [1, 2, 3, 4, 5, 6]

# result = list(filter(lambda x: x % 2 == 0, numbers))

# print(result)

# VD2 

# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]

# result = list(filter(is_even, numbers))

# print(result)

# TODO Reduce
# from functools import reduce

# numbers = [1, 2, 3, 4]

# result = reduce(lambda x, y: x * y, numbers)

# print(result)

# VD2
# from functools import reduce

# numbers = [5, 2, 9, 1, 7]

# result = reduce(
#     lambda x, y: x if x > y else y,
#     numbers
# )

# print(result)