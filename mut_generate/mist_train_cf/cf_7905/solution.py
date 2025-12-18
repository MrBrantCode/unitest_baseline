"""
QUESTION:
Write a function `median_of_six_numbers` that calculates the median of six given numbers without using any additional data structures and with a time complexity of O(n^2) or better and a space complexity of O(1). The function should not modify the original array. The numbers are passed as a list to the function.
"""

def median_of_six_numbers(numbers):
    # Sort the array in ascending order using your own sorting algorithm
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # Check if the length of the array is even or odd
    is_even_length = len(numbers) % 2 == 0

    # If the length is even, the median is the average of the middle two elements
    if is_even_length:
        middle_index = len(numbers) // 2
        median = (numbers[middle_index-1] + numbers[middle_index]) / 2
    # If the length is odd, the median is the middle element
    else:
        middle_index = len(numbers) // 2
        median = numbers[middle_index]

    return median