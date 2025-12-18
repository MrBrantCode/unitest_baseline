"""
QUESTION:
Given a positive floating point number N, the task is to find the smallest integer k, such that when we multiply k with N, we get a natural number.
 
Example 1:
Input: N = "30.25"
Output: 4
Explanation: 30.25 * 4 = 321, there is no 
number less than 4 which can convert 30.25
into natural number.
Example 2:
Input: N = "5.5"
Output: 2
Explanation: 5.5 * 2 = 11, there is no number
less than 2 which can convert 5.5 into 
natural number.
 
Your Task:
You don' need to read or print anything. Your task is to complete the function findMinMultiple() which takes N as input parameter in string format and returns the minimum k such that when we multiply it with N we get a natural number.
 
Expected Time Complexity:O(c) where c is constant
Expected Space Compelxity: O(1)
 
Constraints:
1 <= N <= 1000
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def find_min_multiple(N: str) -> int:
    l = N.split('.')
    c = len(l[1])
    d = int(l[1])
    h = 10 ** c
    return h // gcd(d, h)