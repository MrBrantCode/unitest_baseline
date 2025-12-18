"""
QUESTION:
You are given the array of integer numbers a_0, a_1, ..., a_{n} - 1. For each element find the distance to the nearest zero (to the element which equals to zero). There is at least one zero element in the given array.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 2·10^5) — length of the array a. The second line contains integer elements of the array separated by single spaces ( - 10^9 ≤ a_{i} ≤ 10^9).


-----Output-----

Print the sequence d_0, d_1, ..., d_{n} - 1, where d_{i} is the difference of indices between i and nearest j such that a_{j} = 0. It is possible that i = j.


-----Examples-----
Input
9
2 1 0 3 0 0 3 2 4

Output
2 1 0 1 0 0 1 2 3 
Input
5
0 1 2 3 4

Output
0 1 2 3 4 
Input
7
5 6 0 1 -2 3 4

Output
2 1 0 1 2 3 4
"""

def find_distances_to_nearest_zero(a):
    n = len(a)
    
    # Initialize the result array with -1
    result = [-1] * n
    
    # First pass: forward pass to find distances to the nearest zero on the right
    last_zero_index = -1
    for i in range(n):
        if a[i] == 0:
            last_zero_index = i
        if last_zero_index != -1:
            result[i] = i - last_zero_index
    
    # Second pass: backward pass to find distances to the nearest zero on the left
    last_zero_index = -1
    for i in range(n-1, -1, -1):
        if a[i] == 0:
            last_zero_index = i
        if last_zero_index != -1 and (result[i] == -1 or result[i] > last_zero_index - i):
            result[i] = last_zero_index - i
    
    return result