"""
QUESTION:
Write a Python function named `calculate_average` that calculates the average of a list of numbers. The list can contain integers and strings, where the strings represent either numeric values or invalid/non-numeric values. The function should handle both types of strings and return the average of the valid numbers in the list. If no valid numbers are found, the function should return None.
"""

def calculate_average(numbers):
    sum = 0
    count = 0

    for num in numbers:
        if isinstance(num, int):
            sum += num
            count += 1
        elif isinstance(num, str):
            try:
                sum += float(num)
                count += 1
            except ValueError:
                pass  # Invalid or non-numeric value, ignore it

    if count > 0:
        average = sum / count
        return average
    else:
        return None  # No valid numbers found