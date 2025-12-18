"""
QUESTION:
Given an array of n$n$ integers : A1,A2,...,An$ A_1, A_2,... , A_n$, find the longest size subsequence which satisfies the following property: The xor of adjacent integers in the subsequence must be non-decreasing.

-----Input:-----
- First line contains an integer n$n$, denoting the length of the array. 
- Second line will contain n$n$ space separated integers, denoting the elements of the array.

-----Output:-----
Output a single integer denoting the longest size of subsequence with the given property.

-----Constraints-----
- 1≤n≤103$1 \leq n \leq 10^3$
- 0≤Ai≤1018$0 \leq A_i \leq 10^{18}$

-----Sample Input:-----
8
1 200 3 0 400 4 1 7

-----Sample Output:-----
6

-----EXPLANATION:-----
The subsequence of maximum length is {1, 3, 0, 4, 1, 7} with Xor of adjacent indexes as {2,3,4,5,6} (non-decreasing)
"""

def longest_non_decreasing_xor_subsequence(arr):
    n = len(arr)
    xors = []
    
    # Calculate all possible xors and their indices
    for i in range(n):
        for j in range(i + 1, n):
            xors.append([arr[i] ^ arr[j], (i, j)])
    
    # Sort the xors based on the xor value
    xors.sort()
    
    # Initialize the upto array to keep track of the longest subsequence ending at each index
    upto = [0] * n
    
    # Update the upto array based on the sorted xors
    for i in range(len(xors)):
        (b, c) = (xors[i][1][0], xors[i][1][1])
        upto[c] = max(upto[c], upto[b] + 1)
    
    # The result is the maximum value in the upto array plus one
    return max(upto) + 1