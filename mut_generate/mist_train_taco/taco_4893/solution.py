"""
QUESTION:
Given an array arr[] of size N, use Radix Sort Algorithm to sort arr[] in ascending order.
Example 1:
Input :
N = 5
arr[] = {1, 9, 345, 2}
Output: 1 2 9 345
Example 2:
Input :
N = 10
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 1 2 3 4 5 6 7 8 9 10
Your Task:  
You dont need to read input or print anything. Complete the function radixSort() which takes arr[] and N as input parameters and sorts arr[] in-place. 
Expected Time Complexity: O(N * K) where K is the number of bits required to store each key.
Expected Auxiliary Space: O(N + K)
Constraints:
1 ≤ N ≤ 10^3
"""

def radix_sort(arr, n):
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is the current digit number
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, n, exp)
        exp *= 10
    
    return arr

def counting_sort(arr, n, exp):
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy the output array to arr[], so that arr[] now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]