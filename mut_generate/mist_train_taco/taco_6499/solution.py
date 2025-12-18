"""
QUESTION:
Given X and Y as the GCD and LCM of two numbers A and B. Find all possible pairs of (A,B).
Note: (a, b) and (b, a) are considered as two different pairs.
Example 1:
Input: x = 2, y = 12
Output: 4
Explaination: The pairs are (2, 12), 
(4, 6), (6, 4) and (12, 2).
Example 2:
Input: x = 3, y = 6
Output: 2
Explaination: The pairs are (3, 6) and 
(6, 3).
Example 3:
Input: x = 6, y = 4
Output: 0
Explaination: There is no such pair such 
that gcd is 6 and lcm is 4.
Your Task:
You do not need to read input or print anything. Your task is to complete the function pairCount() which takes x and y as input parameters and returns the number of possibe pairs.
Expected Time Complexity: O(sqrt(N)*LogN)    [N is maximum of x and y]
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ x, y ≤ 10^{4}
"""

def find_pairs_with_gcd_lcm(x, y):
    if x > y:
        return 0
    
    def gcd(m, n):
        u = max(m, n)
        v = min(m, n)
        r = u % v
        while r > 0:
            u = v
            v = r
            r = u % v
        return v
    
    n = y
    p = x * y
    arr = []
    pr = []
    
    for i in range(1, y + 1):
        if y % i == 0:
            arr.append(i)
    
    for i in range(len(arr)):
        a = x * arr[i]
        b = n * x // a
        if gcd(a, b) == x:
            pr.append([a, b])
    
    return len(pr)