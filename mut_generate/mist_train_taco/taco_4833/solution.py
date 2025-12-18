"""
QUESTION:
You are given a array of integers. Find the diff between the maximum average value and minimum average value of sub-sequences of array.

Input:
First line contains a single integer denoting N, the number of elements of array. 
Next line contains N space separated integers denoting the array.

Output:

Print the  greatest integer of the answer.
Greatest integer of 2.5 is 2.
Greatest integer of 2 is 2.

Constraints

1 ≤ N ≤ 500,
0 ≤ A[i] ≤ 10^5

SAMPLE INPUT
4
1 2 1 2

SAMPLE OUTPUT
1

Explanation

Minimum Average value of sub-sequence 1, 1 is 1. Maximum Average value of sub-sequence 2, 2 is 2.Therefore answer is 2-1=1

P.S. : A subsequence of a string is not necessarily continuous.
"""

def calculate_max_avg_diff(arr):
    # Sort the array to easily find the minimum and maximum average values
    arr.sort()
    
    # Minimum average value of the smallest two elements
    min_avg = (arr[0] + arr[1]) / 2
    
    # Maximum average value of the largest two elements
    max_avg = (arr[-1] + arr[-2]) / 2
    
    # Calculate the difference and return the greatest integer part
    return int(max_avg - min_avg)