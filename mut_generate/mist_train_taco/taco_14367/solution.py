"""
QUESTION:
A number is a special number if it’s digits only consist 0, 1, 2, 3, 4 or 5. Given a number N and we have to find N-th Special Number. 
Example 1:
Input:
N = 6
Output: 5
Explanation: First 6 numbers are
( 0, 1, 2, 3, 4, 5 )
Ã¢â¬â¹Example 2:
Input: 
N = 7
Output: 10
Explanation: First 7 numbers are
( 0, 1, 2, 3, 4, 5, 10 )
Your Task:
You don't need to read input or print anything. Your task is to complete the function getSpecialNumber() which accepts an integer N and return N^{th} Special Number.
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{5}
"""

def get_special_number(n: int) -> int:
    digits = []
    n -= 1
    while n:
        digits.append(n % 6)
        n //= 6
    ans = 0
    for d in reversed(digits):
        ans = ans * 10 + d
    return ans