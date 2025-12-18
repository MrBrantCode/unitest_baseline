"""
QUESTION:
Write a function `count_triplets` that takes an array of integers as input and returns the number of triplets that satisfy the triangle inequality. The triangle inequality states that for a valid triangle, the sum of the lengths of any two sides must be greater than the length of the third side. The function should return the count of such triplets in the array. The input array can contain duplicate values and the array will have at least three elements. The function should have a time complexity of O(n^2) or better.
"""

def count_triplets(arr):
    n = len(arr)
    arr.sort()
    counter = 0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] > arr[k]) and (arr[j] + arr[k] > arr[i]) and (arr[k] + arr[i] > arr[j]):
                    counter += 1
    return counter