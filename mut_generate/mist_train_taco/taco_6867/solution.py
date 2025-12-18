"""
QUESTION:
Given an integer array of which both the first halve and second halve are sorted. The task is to merge these two sorted halves of the array into a single sorted array.
Note: The two halves can be of arbitrary sizes (i.e. if first halve of size k then the second halve is of size N-k where 0<=k<=N).
Example 1:
Input:
N = 6
arr[] = {2 3 8 -1 7 10}
Output: -1 2 3 7 8 10 
Explanation: {2 3 8} and {-1 7 10} are sorted 
in the original array. The overall sorted 
version is {-1 2 3 7 8 10}
Example 2:
Input:
N = 5
arr[] = {-4 6 9 -1 3}
Output: -4 -1 3 6 9 
Explanation: {-4 -1} and {3 6 9} are sorted 
in the original array. The overall sorted 
version is {-4 -1 3 6 9}
Your Task:
You don't need to read input or print anything. Your task is to complete the function sortHalves () which takes the array arr[] and its size n as inputs and modifies the array such that it gets sorted completely.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
Constraints:
1 <= N <= 10^{6}
"""

def merge_sorted_halves(arr, n):
    # Create a temporary array to store the merged result
    temp = [0] * n
    
    # Find the midpoint to divide the array into two halves
    mid = n // 2
    
    # Initialize pointers for the two halves
    i = 0  # Pointer for the first half
    j = mid  # Pointer for the second half
    k = 0  # Pointer for the temporary array
    
    # Merge the two halves into the temporary array
    while i < mid and j < n:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of the first half, if any
    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of the second half, if any
    while j < n:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    # Copy the merged elements back to the original array
    for i in range(n):
        arr[i] = temp[i]
    
    return arr