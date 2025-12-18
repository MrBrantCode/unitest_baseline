"""
QUESTION:
Write a function named count_quadruples that takes an array of unique integers as input and returns the number of quadruples (sets of four distinct numbers) in the array that sum up to zero.
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