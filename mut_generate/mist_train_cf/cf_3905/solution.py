"""
QUESTION:
Create a function called calculate_statistics that takes an array of positive integers and returns a string representing the mean, median, and mode of the numbers. The function should calculate the mode using the highest frequency of occurrence, handle floating-point numbers and round the mean to two decimal places, and handle arrays with odd and even lengths for calculating the median. The function should have a time complexity of O(n) and a space complexity of O(n), handle non-integer and negative inputs by returning error messages, and use a single array to store intermediate results without using any additional data structures or built-in functions for mean, median, or mode calculations.
"""

def calculate_statistics(arr):
    # Check if input array is empty
    if not arr:
        return "Input array is empty."

    # Check if input array contains only positive integers
    if not all(isinstance(num, int) and num > 0 for num in arr):
        return "Input array must contain only positive integers."

    # Calculate mean
    mean = round(sum(arr) / len(arr), 2)

    # Calculate median
    sorted_arr = sorted(arr)
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        median = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        median = sorted_arr[mid]

    # Calculate mode
    freq = {}
    max_freq = 0
    mode = []
    for num in arr:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
        if freq[num] > max_freq:
            max_freq = freq[num]
            mode = [num]
        elif freq[num] == max_freq:
            mode.append(num)

    # Return the result as a string
    return f"Mean: {mean}, Median: {median}, Mode: {', '.join(str(num) for num in mode)}"