"""
QUESTION:
Write a function `calculate_average` that calculates the average of even numbers with a factor of 3 in a given list of numbers. The function should take a list of integers as input, iterate over the list, and return the average of even numbers with a factor of 3. If no such numbers are found, the function should return a message indicating that.
"""

def calculate_average(numbers):
    count = 0
    total_sum = 0

    for number in numbers:
        if number % 2 == 0 and number % 3 == 0:
            count += 1
            total_sum += number

    if count > 0:
        return total_sum / count
    else:
        return "No even numbers with a factor of 3 found in the array."