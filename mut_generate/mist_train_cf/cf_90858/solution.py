"""
QUESTION:
Write a function called `find_max_min_avg` that takes an array of numbers as input and returns the maximum, minimum, and average values of the array. The function should not use any built-in functions or methods to sort or find the maximum, minimum, or average values. The solution should have a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1), meaning it should use a constant amount of extra space that does not depend on the size of the input array.
"""

def find_max_min_avg(numbers):
    if len(numbers) == 0:
        return None, None, None

    # Initialize variables
    max_value = float('-inf')
    min_value = float('inf')
    sum_value = 0

    # Iterate through the array
    for num in numbers:
        # Update maximum value
        if num > max_value:
            max_value = num

        # Update minimum value
        if num < min_value:
            min_value = num

        # Update sum of values
        sum_value += num

    # Calculate average value
    average_value = sum_value / len(numbers)

    return max_value, min_value, average_value