"""
QUESTION:
Create a function named `sum_of_elements` that takes an array of integers as input and returns the sum of the elements that meet the following conditions:
- The element is divisible by 3.
- The element is greater than 5.
- The element is less than 100.
- The element does not contain the digit 2.
"""

def sum_of_elements(arr):
    total_sum = 0

    for num in arr:
        if num % 3 == 0 and num > 5 and num < 100 and '2' not in str(num):
            total_sum += num

    return total_sum