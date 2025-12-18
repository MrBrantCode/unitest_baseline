"""
QUESTION:
Given two given numbers a and b where 1<= a <= b, find the perfect cubes between a and b (a and b inclusive).
Example 1:
Input: a = 1, b = 100
Output: 1 8 27 64
Explaination: These are the proper cubes between 
1 and 100.
Example 2:
Input: a = 24, b = 576
Output: 27 64 125 216 343 512
Explaination: These are the proper cubes between 
24 and 576.
Your Task:
You do not need to read input or print anything. Your task is to complete the function properCubes() which takes a and b as input parameters and returns the proper cubes between a and b. The function returns -1 if there is no proper cube between the given values.
Expected Time Complexity: O(cuberoot(b))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ a ≤ b ≤ 10^{4}
"""

import math

def find_perfect_cubes(a, b):
    # Calculate the cube root of the bounds
    r = math.floor(b ** (1 / 3))
    l = math.ceil(a ** (1 / 3))
    
    # Adjust the upper bound if b is a perfect cube
    if (math.floor(b ** (1 / 3)) + 1) ** 3 == b:
        r += 1
    
    # If the bounds are the same, return the cube of l
    if l == r:
        return [l ** 3]
    
    # If l is greater than r, return [-1]
    if l > r:
        return [-1]
    
    # Generate the list of perfect cubes
    ans = [i ** 3 for i in range(l, r + 1)]
    
    # If the list is empty, return [-1]
    if not ans:
        ans.append(-1)
    
    return ans