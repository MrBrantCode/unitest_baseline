"""
QUESTION:
Create a function named `remove_consecutive_duplicates` that takes an array as input and returns a new array with consecutive duplicate elements removed, keeping only one instance of each repeated value. The function should only consider consecutive identical entries and not remove non-consecutive duplicate values.
"""

def remove_consecutive_duplicates(array):
    return [array[i] for i in range(len(array)) if i == 0 or array[i] != array[i - 1]]