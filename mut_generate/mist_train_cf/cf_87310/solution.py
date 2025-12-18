"""
QUESTION:
Write a function `calculate_average` that takes a list of integers and strings as input, where the strings represent either valid integers or invalid/non-numeric values. The function should calculate and return the average of the valid integers in the list. If no valid integers are found, the function should return None. The function should use type casting and error handling to handle invalid or non-numeric values.
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
                sum += int(num)
                count += 1
            except ValueError:
                pass  # Invalid or non-numeric value, ignore it

    if count > 0:
        average = sum / count
        return average
    else:
        return None  # No valid numbers found