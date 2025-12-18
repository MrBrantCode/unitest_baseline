"""
QUESTION:
Write a function `count_quadruples(arr)` that takes an array of unique positive and negative numbers and returns the number of quadruples in the array that sum up to zero. The function should have a time complexity of O(n^4), where n is the length of the input array.
"""

def count_quadruples(arr):
    count = 0
    
    for i in range(len(arr)-3):
        for j in range(i+1, len(arr)-2):
            for k in range(j+1, len(arr)-1):
                for l in range(k+1, len(arr)):
                    if arr[i] != arr[j] != arr[k] != arr[l]:
                        if arr[i] + arr[j] + arr[k] + arr[l] == 0:
                            count += 1
    
    return count