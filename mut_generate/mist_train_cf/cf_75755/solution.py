"""
QUESTION:
Write a function named `longest_increasing_subsequence` that determines the length of the longest increasing subsequence in a given array of integers. The function should take one argument, an array of integers, and return an integer representing the length of the longest increasing subsequence. The function should have a time complexity of at least O(n^2), where n is the number of elements in the input array.
"""

def longest_increasing_subsequence(arr): 
    n = len(arr) 
    lis = [1]*n
  
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    maximum = 0
    for i in range(len(lis)): 
        maximum = max(maximum , lis[i]) 
  
    return maximum