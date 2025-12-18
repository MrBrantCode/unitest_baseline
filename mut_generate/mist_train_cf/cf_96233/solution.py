"""
QUESTION:
Write a function `count_quadruplets(arr)` that takes an array of integers as input and returns the number of unique quadruplets that satisfy the triangle inequality, where the sum of any three sides must be greater than the fourth side. The function should have a time complexity of O(n^3), constant space complexity, and handle negative integers, floating-point numbers, and duplicate quadruplets correctly.
"""

def count_quadruplets(arr):
    n = len(arr)
    count = 0
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if (arr[i] + arr[j] + arr[k]) > arr[l] and (arr[i] + arr[j] + arr[l]) > arr[k] and (arr[i] + arr[k] + arr[l]) > arr[j] and (arr[j] + arr[k] + arr[l]) > arr[i]:
                        count += 1

    return count