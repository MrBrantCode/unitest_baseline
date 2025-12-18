"""
QUESTION:
Given a positive integer n, find first k digits after the decimal in the value of 1/n and return it as a string. 
Note: Your program should avoid overflow and floating-point arithmetic. 
Example 1:
Input: n = 3, k = 3
Output: 333
Explanation: 1/3=0.33333, so
after point 3 digits are 3,3,3.
Ã¢â¬â¹Example 2:
Input: n = 50, k = 4
Output: 0200
Explanation: 1/50=0.020000, so 
after point 4 digits are 0,2,0,0.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function Kdigits() which takes n, k as inputs and returns the string.
Expected Time Complexity: O(k)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n, k ≤ 10^{5}
"""

def get_first_k_digits_after_decimal(n: int, k: int) -> str:
    rem = 1
    result = ''
    for _ in range(k):
        result += str((10 * rem) // n)
        rem = (10 * rem) % n
    return result