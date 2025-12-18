"""
QUESTION:
You are given an array of n integer numbers a_0, a_1, ..., a_{n} - 1. Find the distance between two closest (nearest) minimums in it. It is guaranteed that in the array a minimum occurs at least two times.


-----Input-----

The first line contains positive integer n (2 ≤ n ≤ 10^5) — size of the given array. The second line contains n integers a_0, a_1, ..., a_{n} - 1 (1 ≤ a_{i} ≤ 10^9) — elements of the array. It is guaranteed that in the array a minimum occurs at least two times.


-----Output-----

Print the only number — distance between two nearest minimums in the array.


-----Examples-----
Input
2
3 3

Output
1

Input
3
5 6 5

Output
2

Input
9
2 1 3 5 4 1 2 3 1

Output
3
"""

def find_nearest_minimum_distance(n, a):
    min_value = min(a)
    min_indices = [i for i, value in enumerate(a) if value == min_value]
    
    nearest_distance = float('inf')
    for i in range(1, len(min_indices)):
        distance = min_indices[i] - min_indices[i - 1]
        if distance < nearest_distance:
            nearest_distance = distance
    
    return nearest_distance