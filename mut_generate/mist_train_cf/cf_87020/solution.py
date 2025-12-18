"""
QUESTION:
Write a function `calculate_average` that takes a list of numbers as input and returns the average of the numbers rounded to the nearest integer. The function should handle cases where the input list contains duplicate values, negative numbers, and floating-point numbers. If the input list is empty or contains non-numeric values, the function should return `None`. The function should have a time complexity of O(n), where n is the number of elements in the input list.
"""

def calculate_average(a_list):
    if not a_list:
        return None

    try:
        count = 0
        total_sum = 0

        for num in a_list:
            total_sum += float(num)
            count += 1

        average = total_sum / count
        rounded_average = round(average)

        return rounded_average

    except (ValueError, TypeError):
        return None