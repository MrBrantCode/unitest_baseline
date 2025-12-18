"""
QUESTION:
Find the mode(s) in a list of numbers, which are the numbers that appear most frequently. If there are multiple modes, return a list of all of them sorted in ascending order. The function should be able to handle a list of at least one number and no more than 10^6 numbers, with numbers in the range of -10^6 to 10^6. The function name should be `find_modes`.
"""

from collections import Counter

def find_modes(numbers):
    counter = Counter(numbers) 
    max_count = max(counter.values()) 

    modes = [num for num, count in counter.items() if count == max_count] 

    return sorted(modes) 