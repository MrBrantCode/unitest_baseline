"""
QUESTION:
Develop a function named `find_mode` that accepts a list of integers as an argument and returns the mode, which is the integer that occurs most frequently within the list. If there is a tie, the function should return the mode with the greatest numerical value. The function should be able to handle a list containing a mix of both positive and negative integers. If the list is empty, the function should return None.
"""

def find_mode(numbers):
    if len(numbers) == 0:
        return None

    freq_dict = {}
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    max_freq = max(freq_dict.values())
    modes = [num for num, freq in freq_dict.items() if freq == max_freq]

    return max(modes)