"""
QUESTION:
Write a function `most_frequent_item(arr, m)` that finds the most frequently occurring item in a list of integers `arr` where each integer is in the range of 1 to `m`. The function should have a time complexity of O(n), where n is the length of `arr`, and a space complexity of O(m).
"""

def most_frequent_item(arr, m):
    counts = [0] * (m + 1)
    max_count = 0
    most_frequent = None
    
    for num in arr:
        counts[num] += 1
        
        if counts[num] > max_count:
            max_count = counts[num]
            most_frequent = num
    
    return most_frequent