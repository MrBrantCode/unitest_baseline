"""
QUESTION:
Create a function `calculate_statistics` that takes an array of positive integers and returns a string representing the mean, median, and mode of the numbers. The function should handle duplicate numbers and non-integer inputs, providing error messages for negative numbers and empty arrays. The mode should be calculated using the highest frequency of occurrence, and the function should have a time complexity of O(n) and a space complexity of O(n). The function should not use built-in functions or libraries for mean, median, or mode calculations and should handle floating-point numbers by rounding the mean to two decimal places.
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