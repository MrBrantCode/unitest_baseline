"""
QUESTION:
Write a function `average_even_numbers` that takes an array of at least 5 positive integers as input and returns the average of the even elements, rounded to the nearest whole number.
"""

def average_even_numbers(arr):
    total = 0
    count = 0
    for num in arr:
        if num % 2 == 0:
            total += num
            count += 1
    return round(total/count)