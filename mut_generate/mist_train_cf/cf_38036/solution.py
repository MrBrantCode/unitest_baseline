"""
QUESTION:
Given an array A of integers and an integer K, find the smallest possible difference between the maximum and minimum values of the array after adding or subtracting K from each element in the array. The function smallestRangeII should take in A and K as input and return the smallest possible range of the modified array. 

A contains 2 to 10000 integers ranging from -10000 to 10000. K is an integer ranging from -10000 to 10000.
"""

def smallestRangeII(A, K):
    A.sort()
    ans = A[-1] - A[0]
    for x, y in zip(A, A[1:]):
        ans = min(ans, max(A[-1]-K, x+K) - min(A[0]+K, y-K))
    return ans