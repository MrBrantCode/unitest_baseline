"""
QUESTION:
Write a function `most_frequent_element` that finds the most frequent element in a given array. The function must have a time complexity of O(n) and a space complexity of O(1), without using any built-in functions or data structures. The function should handle arrays with up to 1 million elements.
"""

def most_frequent_element(arr):
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