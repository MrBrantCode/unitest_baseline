"""
QUESTION:
Create a function named `count_nums` that accepts an integer array and returns the count of elements where the sum of absolute values of digits (preserving the number's sign) is divisible by 4.
"""

def count_nums(array):
    count = 0
    for i in array:
        if sum(int(dig) for dig in str(abs(i))) % 4 == 0:  # absoluting the number before converting into string
            count += 1
    return count