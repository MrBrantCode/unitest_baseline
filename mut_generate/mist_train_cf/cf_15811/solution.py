"""
QUESTION:
Create a function named `calculate_running_average` that calculates the running average of an array of integers, only considering numbers that are divisible by 3 and greater than 10. The function should handle arrays with up to 1000 elements and return the running average as a floating point number.
"""

def calculate_running_average(data):
    total = 0
    count = 0

    for num in data:
        if num % 3 == 0 and num > 10:
            total += num
            count += 1

    return total / count if count > 0 else 0