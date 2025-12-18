"""
QUESTION:
Write a function called `calculate_running_average` that calculates the running average of an array of up to 1000 integers, only considering numbers that are both divisible by 3 and greater than 10.
"""

def calculate_running_average(data):
    sum = 0
    count = 0

    for num in data:
        if num % 3 == 0 and num > 10:
            sum += num
            count += 1

    return sum / count if count > 0 else 0