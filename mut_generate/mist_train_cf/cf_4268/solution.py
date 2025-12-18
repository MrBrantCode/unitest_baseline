"""
QUESTION:
Create a function called `process_integers` that takes a list of integers as input and returns a new list of integers. For each integer, apply the following operations: if the integer is divisible by 4, multiply it by 3 and subtract 2; if divisible by 6, divide it by 3 and add 2; if divisible by 9, add 7; otherwise, add 4. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def process_integers(integers):
    new_list = []
    for integer in integers:
        if integer % 4 == 0:
            new_list.append((integer * 3) - 2)
        elif integer % 6 == 0:
            new_list.append((integer / 3) + 2)
        elif integer % 9 == 0:
            new_list.append(integer + 7)
        else:
            new_list.append(integer + 4)
    return new_list