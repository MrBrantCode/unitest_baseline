"""
QUESTION:
Given N space separated integers. Your task is to arrange them such that the summation M of the absolute differences between every two adjacent numbers is maximum.  

Input:

First line of the input contains an integer N.      
Second line contains N space separated integers A_i.   

Output:

Print the above described M. 

Constraints:

1 ≤ N ≤ 1000.
1 ≤ A_i  ≤ 10^{5}.

SAMPLE INPUT
3
1 2 7

SAMPLE OUTPUT
11

Explanation

One of the best arrangements is (1,7,2), M = |1 - 7| + |7 - 2| = 11
"""

def maximize_adjacent_difference_sum(arr):
    arr.sort()
    n = len(arr)
    
    # Calculate sum1
    sum1 = 0
    i, j = 0, n - 1
    count = 0
    while i < j:
        sum1 += arr[j] - arr[i]
        count += 1
        if count % 2 == 1:
            i += 1
        else:
            j -= 1
    
    # Calculate sum2
    sum2 = 0
    i, j = 0, n - 1
    count = 0
    while i < j:
        sum2 += arr[j] - arr[i]
        count += 1
        if count % 2 == 1:
            j -= 1
        else:
            i += 1
    
    # Return the maximum of sum1 and sum2
    return max(sum1, sum2)