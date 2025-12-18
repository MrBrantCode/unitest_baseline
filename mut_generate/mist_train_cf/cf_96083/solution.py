"""
QUESTION:
Write a function called `print_and_return_frequencies` that takes an array of integers as input, prints the frequencies of even and odd numbers, and the frequencies of negative and positive numbers in the array, then returns the two most frequent even numbers and the two most frequent odd numbers in the array. The function should have a time complexity of less than O(n^2).
"""

from collections import defaultdict

def print_and_return_frequencies(arr):
    # Dictionary to keep track of frequencies
    freq = defaultdict(int)
    even_nums = defaultdict(int)
    odd_nums = defaultdict(int)

    for num in arr:
        # Update even/odd frequencies
        if num % 2 == 0:
            freq['even'] += 1
            even_nums[num] += 1
        else:
            freq['odd'] += 1
            odd_nums[num] += 1
        
        # Update positive/negative frequencies
        if num >= 0:
            freq['positive'] += 1
        else:
            freq['negative'] += 1

    # Sort the even and odd numbers in descending order of frequency
    sorted_even_nums = sorted(even_nums.items(), key=lambda x: x[1], reverse=True)
    sorted_odd_nums = sorted(odd_nums.items(), key=lambda x: x[1], reverse=True)

    # Find the two most frequent even and odd numbers
    most_frequent_even_nums = [x[0] for x in sorted_even_nums[:2]]
    most_frequent_odd_nums = [x[0] for x in sorted_odd_nums[:2]]

    # Print frequencies
    print("Even: ", freq['even'])
    print("Odd: ", freq['odd'])
    print("Positive: ", freq['positive'])
    print("Negative: ", freq['negative'])

    # Return the two most frequent even and odd numbers
    return most_frequent_even_nums, most_frequent_odd_nums