"""
QUESTION:
Write a function `calculate_mean(input_string)` that takes a string of comma-separated numbers, converts it to a list of non-negative numbers, and returns the rounded mean of these numbers. The function should ignore any non-numeric characters and negative numbers in the input string.
"""

def calculate_mean(input_string):
    numbers = input_string.split(",")
    total = 0
    count = 0
    for number in numbers:
        try:
            num = float(number)
            if num >= 0:
                total += num
                count += 1
        except ValueError:
            continue
    if count == 0:
        return 0
    mean = round(total / count)
    return mean