"""
QUESTION:
Write a function `multiply(lst)` that takes a populated array of integers as input and returns the product of all odd numerals located at even indices within the array that are simultaneously multiples of 3. The indices of the array start at 0 (even). The function should have a time complexity of O(n), where n is the number of elements in the input list, and a space complexity of O(1).
"""

def multiply(lst):
    """Given a populated array of integers, lst, compute the product of all odd numerals located at even indices within the array that are simultaneously multiples of 3.

    """
    result = 1
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 1 and lst[i] % 3 == 0:
            result *= lst[i]
    return result