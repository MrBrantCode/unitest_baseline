"""
QUESTION:
Implement a function called `special_sort` that takes an array of mixed numbers as input and returns the sorted array. The array contains negative numbers, zeros, rational numbers between 0 and 1, and integers 1 and 2. The function must sort the array such that negative numbers are at the beginning in ascending order, followed by zeros, then rational numbers in ascending order, and finally integers 1 and 2 in descending order. The function should have a time complexity of O(n log n) or better.
"""

def special_sort(arr):
    arr.sort()
    negatives = [num for num in arr if num < 0]
    zeros = [num for num in arr if num == 0]
    rationals = [num for num in arr if 0 < num < 1]
    ones_twos = [num for num in arr if num == 1 or num == 2]
    ones_twos.sort(reverse=True)
    return negatives + zeros + rationals + ones_twos