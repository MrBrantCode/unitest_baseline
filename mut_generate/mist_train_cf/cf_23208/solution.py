"""
QUESTION:
Write a function called `sum_numbers` that takes a range of numbers from `start` to `end` and returns the sum of each number in the range multiplied by 2. The function should use recursion and divide the range into sub-ranges of no more than 100 numbers each.
"""

def sum_numbers(start, end):
    if start > end:
        return 0
    elif end - start <= 100:
        total = 0
        for num in range(start, end + 1):
            total += num * 2
        return total
    else:
        mid = (start + end) // 2
        return sum_numbers(start, mid) + sum_numbers(mid + 1, end)