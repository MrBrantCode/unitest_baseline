"""
QUESTION:
Write a function `compute_average` that calculates the average of the positive integers greater than 5 in a given list of numbers. The list may contain duplicate numbers and has a length of up to 1000. The function should return the average rounded to the nearest whole number.
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