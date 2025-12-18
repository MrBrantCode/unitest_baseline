"""
QUESTION:
Write a function `compute_average(numbers)` that calculates the average of the positive integers greater than 5 in the given list of numbers. The function should return the average rounded to the nearest whole number. The input list may contain duplicate numbers and can have a length of up to 1000.
"""

def compute_average(numbers):
    sum = 0
    count = 0
    for num in numbers:
        if num > 5:
            sum += num
            count += 1
    if count == 0:
        return 0
    average = round(sum / count)
    return average