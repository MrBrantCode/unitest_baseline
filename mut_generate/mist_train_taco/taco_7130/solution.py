"""
QUESTION:
You are given two arrays of length n. An array a consisting of integers and another array d consisting of directions 'N', 'S', 'E', and 'W' denoting North, South, East, and West respectively.For every 'i' you move a[i] distance in d[i]th direction. You have to give the ceil of total distance covered through all the movements and then back to the starting  point. From the end of the journey you come to the starting point using the shortest distance.
Example 1:
Input: n = 3
a = {1, 3, 3}
d = {N, E, S}
Output: 11
Explaination: The total distance covered is 
ceil(1 + 3 + 3 + 3.6056) = 11.
Example 2:
Input: n = 4
a = {10, 10, 10, 10}
d = {N, E, S, W}
Output: 40
Explaination: The total distance covered is 
ceil(10 + 10 + 10 + 10 + 0) = 40.
Your Task:
You do not need to read input or print anything. Your task is to complete the function distance() which takes n, a, and d as input parameters and returns the ceil of total distance covered.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 1000
1 ≤ a[i] ≤ 1000
"""

import math

def calculate_total_distance(n, a, d):
    if len(d) == 1:
        d = list(d[0])
    x = 0
    y = 0
    for i in range(n):
        if d[i] == 'N':
            y += a[i]
        elif d[i] == 'S':
            y -= a[i]
        elif d[i] == 'E':
            x -= a[i]
        else:
            x += a[i]
    h = math.sqrt(x * x + y * y)
    return math.ceil(sum(a) + h)