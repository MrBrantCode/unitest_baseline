"""
QUESTION:
Given a list of distinct numbers, find the length of the longest increasing subsequence, where a subsequence is considered increasing if each element is greater than its previous element. Write a function `longest_increasing_subsequence(arr)` that takes a list of integers `arr` as input and returns the length of the longest increasing subsequence.
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
  
    # Initialize the list with 1's as a single 
    # element can be a longest increasing sequence
    length_table = [1]*n

    # Start from the second element
    for i in range (1 , n):
        # Check all elements before it
        for j in range(0 , i):
            # If current element is greater
            if arr[i] > arr[j] and length_table[i]< length_table[j] + 1 :
                # Update the length
                length_table[i] = length_table[j]+1

    # Get the maximum length from the array
    maximum = 0
    for i in range(len(length_table)):
        maximum = max(maximum , length_table[i])
 
    return maximum