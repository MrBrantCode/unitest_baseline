"""
QUESTION:
Write a function called most_frequent that takes an array as input and returns the most frequent element in the array. The function must have a time complexity of O(n) and constant space complexity. The function should not use any built-in functions or data structures other than arrays and primitive types. The array can contain up to 1 million elements.
"""

def most_frequent(arr):
    max_freq = 0
    most_frequent = None

    for num in arr:
        freq = 0
        for n in arr:
            if num == n:
                freq += 1
        if freq > max_freq:
            max_freq = freq
            most_frequent = num

    return most_frequent