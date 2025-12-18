"""
QUESTION:
Write a function `count_evens` that takes a two-dimensional list of integers as input. The function should return a list where the first elements are the count of even numbers in each sublist, and the last element is the total count of even numbers in the entire two-dimensional list.
"""

def count_evens(arr):
    total = 0
    counts = []
    for sublist in arr:
        subcount = 0
        for number in sublist:
            if number % 2 == 0:
                subcount += 1
                total += 1
        counts.append(subcount)
    counts.append(total)
    return counts