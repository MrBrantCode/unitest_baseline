"""
QUESTION:
Implement a function `analyze_numbers` that takes a set of integers as input, calculates and returns the number of positive integers, their average, maximum value, and minimum value. The set can contain up to 10^6 elements, each ranging from -10^9 to 10^9. If there are no positive numbers in the set, the average should be 0.
"""

def analyze_numbers(numbers):
    positive_count = 0
    sum_of_positives = 0
    max_positive = float('-inf')
    min_positive = float('inf')

    for number in numbers:
        if number > 0:
            positive_count += 1
            sum_of_positives += number
            max_positive = max(max_positive, number)
            min_positive = min(min_positive, number)

    if positive_count > 0:
        average_of_positives = sum_of_positives / positive_count
    else:
        average_of_positives = 0

    return positive_count, average_of_positives, max_positive, min_positive