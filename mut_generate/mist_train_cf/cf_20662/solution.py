"""
QUESTION:
Write a function `count_quadruplets` that takes an array of integers as input and returns the number of unique quadruplets in the array that satisfy the triangle inequality, i.e., the sum of any three sides is greater than the fourth side. The function should have a time complexity of O(n^3) and constant space complexity, handle negative integers and floating-point numbers, and correctly handle duplicates in the input array.
"""

def count_quadruplets(arr):
    n = len(arr)
    count = 0
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if arr[i] + arr[j] > arr[l] and arr[i] + arr[l] > arr[j] and arr[j] + arr[l] > arr[i]:
                        count += 1

    return count