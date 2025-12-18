"""
QUESTION:
Given 4 integers a,b,c and k . Find the min(non-negative Integral) value of x such that ax^{2}+bx+c >= k.
Example 1:
Input: a = 4, b = 6, c = 5, k = 5
Output: 0
Explanation: 4*(0)^{2}+6*0+5 = 5 which is
>= 5.
Ã¢â¬â¹Example 2:
Input: a = 1, b = 2, c = 3, k = 4 
Output: 1 
Explanation: 1*(1)^{2}+2*1+3 = 6 which is
Ã¢â¬â¹>= 4.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minX() which takes a, b, c and k as inputs and returns the answer.
Expected Time Complexity: O(log k)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ a, b, c ≤ 10^{5}
1 ≤ k ≤ 10^{9}
"""

def find_min_x(a: int, b: int, c: int, k: int) -> int:
    if a != 0:
        discriminant = b ** 2 - 4 * a * (c - k)
        if discriminant < 0:
            return 0
        x = (-b + discriminant ** 0.5) / (2 * a)
        if x < 0:
            return 0
        elif x == int(x):
            return int(x)
        else:
            return int(x) + 1
    elif a == 0:
        if b == 0:
            return 0 if c >= k else -1  # No solution if b == 0 and c < k
        x = (k - c) / b
        if x == int(x):
            return int(x)
        else:
            return int(x) + 1