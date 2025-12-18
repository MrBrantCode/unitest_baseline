"""
QUESTION:
Design a function named `compute_disparity_and_frequency` that accepts two numerical arrays as input and returns the largest disparity and the most frequent number between the two arrays. The disparity is defined as the absolute difference between the maximum value of one array and the minimum value of the other array, whichever is greater. If there are multiple most frequent numbers, return the lowest one. The function should have a time complexity of O(n) or O(n log n) where n is the length of the array.
"""

from collections import Counter

def compute_disparity_and_frequency(arr1, arr2):
    min1, max1 = min(arr1), max(arr1)
    min2, max2 = min(arr2), max(arr2)
    
    disparity = max(max1-min2, max2-min1)
    
    freq = Counter(arr1+arr2)
    most_freq_num = freq.most_common()
    most_freq_num.sort(key = lambda x: (-x[1], x[0]))
    
    return disparity, most_freq_num[0][0]