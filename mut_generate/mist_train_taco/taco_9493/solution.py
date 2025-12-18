"""
QUESTION:
You are given array consisting of n integers. Your task is to find the maximum length of an increasing subarray of the given array.

A subarray is the sequence of consecutive elements of the array. Subarray is called increasing if each element of this subarray strictly greater than previous.


-----Input-----

The first line contains single positive integer n (1 ≤ n ≤ 10^5) — the number of integers.

The second line contains n positive integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9).


-----Output-----

Print the maximum length of an increasing subarray of the given array.


-----Examples-----
Input
5
1 7 2 11 15

Output
3

Input
6
100 100 100 100 100 100

Output
1

Input
3
1 2 3

Output
3
"""

def find_max_increasing_subarray_length(arr):
    if not arr:
        return 0
    
    n = len(arr)
    mx = 1
    cn = 1
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            cn += 1
        else:
            cn = 1
        if cn > mx:
            mx = cn
    
    return mx