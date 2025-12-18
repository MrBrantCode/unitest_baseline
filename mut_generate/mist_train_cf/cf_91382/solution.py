"""
QUESTION:
Write a function called `calculate_mode` that takes a list of integers as input and returns a list of integers. The function should return the mode(s) of the input list, which is the number(s) that appear(s) most frequently. If multiple numbers have the same highest frequency, return all of them. The input list may contain duplicate numbers and negative numbers.
"""

def calculate_mode(numbers):
    frequency = {}
    
    # Count the frequency of each number
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    return modes