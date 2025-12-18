"""
QUESTION:
Design a function `sort_by_binary_ones_desc` that takes a list of positive integers as input and returns the list sorted in ascending order based on the count of 1s in their binary representation. If two or more integers have the same count of 1s, they should be arranged according to their decimal values in reverse order.
"""

def sort_by_binary_ones_desc(arr):        
    # Key function that returns a tuple composed of count of '1' and negative value of element
    def sort_key(x):
        return (bin(x).count('1'), -x)

    arr.sort(key=sort_key)

    return arr