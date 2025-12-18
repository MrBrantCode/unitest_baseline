"""
QUESTION:
You are given an integer n, find the smallest positive integer root of equation x, or else print -1 if no roots are found.
Equation: x^2+s(x)*x-n=0
where x, n are positive integers, s(x) is the function, equal to the sum of digits of number x in the decimal number system.
 
Example 1:
Input: n = 110
Output: 10
Explanation: x=10 is the minimum root. 
As s(10)=1+0=1 and 102+1*10-110=0.
Example 2:
Input: n = 5
Output: -1
Explanation: There is no x possible which
satisfy the above equation.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Root() which takes n as input parameter and retuns the minimum root of the given equation. If not possible returns -1.
 
Expected Time Complexity: O(k) where k is constant
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 10^{18}
"""

import math

def sum_of_digits(x):
    """Helper function to calculate the sum of digits of a number x."""
    temp = 0
    while x > 0:
        temp += x % 10
        x //= 10
    return temp

def quadratic_root(a, b, c):
    """Helper function to find the root of a quadratic equation ax^2 + bx + c = 0."""
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return -1
    root = (-b + math.sqrt(discriminant)) / (2 * a)
    if int(root) == root and root > 0:
        return int(root)
    return -1

def find_smallest_root(n):
    """
    Function to find the smallest positive integer root of the equation x^2 + s(x)*x - n = 0,
    where s(x) is the sum of digits of x.
    
    Parameters:
    - n: An integer representing the input value.
    
    Returns:
    - An integer representing the smallest positive integer root, or -1 if no such root exists.
    """
    smallest_root = float('inf')
    found = False
    
    for i in range(91):  # Since the maximum sum of digits for a number with 18 digits is 9*18 = 162, we can limit our search to 90
        temp_root = quadratic_root(1, i, -n)
        if temp_root != -1 and sum_of_digits(temp_root) == i:
            if temp_root < smallest_root:
                smallest_root = temp_root
                found = True
    
    return smallest_root if found else -1