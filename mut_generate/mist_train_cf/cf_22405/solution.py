"""
QUESTION:
Implement a function `calculate_median(x, y, z, w, a, b)` that takes six numbers as input and returns their median. The function should sort the numbers in ascending order without using any built-in sorting function or library. The median is the average of the middle two elements if the length is even, and the middle element if the length is odd.
"""

def calculate_median(x, y, z, w, a, b):
    # Initialize the array
    numbers = [x, y, z, w, a, b]

    # Sort the array using bubble sort
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Check if the length is even or odd
    length = len(numbers)
    if length % 2 == 0:
        # Calculate median for even length
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        # Calculate median for odd length
        median = numbers[length // 2]

    return median