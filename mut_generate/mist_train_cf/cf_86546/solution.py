"""
QUESTION:
Create a function named `calculate_sum` that takes an array of integers as input and returns the sum of all values that are less than 10 and divisible by 3. If the array contains any values that are greater than or equal to 10, print a warning message and skip adding them to the sum.
"""

def calculate_sum(arr):
    sum = 0
    for num in arr:
        if num >= 10:
            print("Warning: Skipping value", num)
            continue
        if num % 3 == 0:
            sum += num
    return sum