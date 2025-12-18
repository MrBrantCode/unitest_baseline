"""
QUESTION:
Implement a function `count_nums(arr)` that takes an array of integers and returns the count of those numbers whose signed digit sum exceeds zero and is divisible by 4. The signed digit sum is calculated considering the initial digit as negative if the number itself is negative.
"""

def count_nums(arr):
    count = 0
    for num in arr:
        s = 0
        if num < 0:
            num = -1 * num
            for digit in str(num):
                s -= int(digit)
        else:
            for digit in str(num):
                s += int(digit)

        if s > 0 and s % 4 == 0:
            count += 1
    return count