"""
QUESTION:
Write a function named `multiplication_table` that takes two parameters: `num` and `limit`. This function should recursively display the multiplication table of `num` up to `limit`, excluding any multiples of 3.
"""

def multiplication_table(num, limit):
    if limit == 0:
        return
    else:
        multiplication_table(num, limit-1)
        if limit % 3 != 0:
            print(f"{num} * {limit} = {num * limit}")