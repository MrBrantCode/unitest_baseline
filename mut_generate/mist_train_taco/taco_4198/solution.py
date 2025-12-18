"""
QUESTION:
Your security guard friend recently got a new job at a new security company. The company requires him to patrol an area of the city encompassing exactly N city blocks, but they let him choose which blocks. That is, your friend must walk the perimeter of a region whose area is exactly N blocks. Your friend is quite lazy and would like your help to find the shortest possible route that meets the requirements. The city is laid out in a square grid pattern, and is large enough that for the sake of the problem it can be considered infinite.


-----Input-----

Input will consist of a single integer N (1 ≤ N ≤ 10^6), the number of city blocks that must be enclosed by the route.


-----Output-----

Print the minimum perimeter that can be achieved.


-----Examples-----
Input
4

Output
8

Input
11

Output
14

Input
22

Output
20



-----Note-----

Here are some possible shapes for the examples:

[Image]
"""

from math import sqrt, floor, ceil

def calculate_minimum_perimeter(n):
    ls = floor(sqrt(n))
    us = ceil(sqrt(n))
    
    p1 = 4 * ls + 2
    p2 = 4 * us
    
    if ls < n - ls ** 2:
        return p2
    return min(p1, p2)