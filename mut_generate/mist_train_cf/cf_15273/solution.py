"""
QUESTION:
Write a function `find_most_frequent` that takes an array of at least 20 integers as input, and returns a list of the most frequent elements that occur at least three times, in descending order of frequency. The function should have a time complexity of O(n) and must not use any additional data structures beyond a constant amount of space.
"""

def find_most_frequent(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    frequent_nums = []
    for num, count in counts.items():
        if count >= 3:
            frequent_nums.append((num, count))
    
    frequent_nums.sort(key=lambda x: x[1], reverse=True)
    
    return [num for num, count in frequent_nums]