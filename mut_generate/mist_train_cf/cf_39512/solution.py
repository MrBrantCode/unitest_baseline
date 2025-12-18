"""
QUESTION:
Write a function `combineData` that takes two arrays, each containing a string and an integer, as input. The function should return a new array where the first element is the concatenation of the strings from the input arrays, and the second element is the sum of the integers from the input arrays.
"""

def combineData(data1, data2):
    letter = data1[0] + data2[0]
    total_sum = data1[1] + data2[1]
    return [letter, total_sum]