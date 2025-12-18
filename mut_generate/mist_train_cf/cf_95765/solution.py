"""
QUESTION:
Implement the function `calculate_median(numbers)` that takes an array of integers as input and returns the median number. You cannot use any built-in functions or libraries to sort the array. The input array may contain both odd and even number of elements, duplicates, and negative numbers.
"""

def calculate_median(numbers):
    # Find the minimum and maximum values
    min_num = min(numbers)
    max_num = max(numbers)

    # Create a frequency array
    frequency = [0] * (max_num - min_num + 1)

    # Count the occurrences of each number
    for num in numbers:
        frequency[num - min_num] += 1

    # Calculate the total number of elements
    n = sum(frequency)

    # Calculate the middle index
    m = (n + 1) // 2

    # Iterate through the frequency array
    count = 0
    for i, freq in enumerate(frequency):
        count += freq
        if count >= m:
            # Return the median number
            if n % 2 == 0 and count == m:
                # Handle even number of elements
                next_num = i + min_num + 1
                return (i + min_num + next_num) / 2
            else:
                return i + min_num