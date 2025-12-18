"""
QUESTION:
Create a function named `divisible_by_2_and_5` that takes a start and end value as input, returns a list of numbers within that range that are divisible by both 2 and 5, and sorts the list in descending order of the sum of digits of each number.
"""

def divisible_by_2_and_5(start, end):
    nums = []
    for i in range(start, end+1):
        if i % 2 == 0 and i % 5 == 0:
            nums.append(i)
    nums.sort(key=lambda x: sum(int(digit) for digit in str(x)), reverse=True)
    return nums