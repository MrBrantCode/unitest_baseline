"""
QUESTION:
Given two coins of denominations X and Y respectively, find the largest amount that cannot be obtained using these two coins (assuming infinite supply of coins) followed by the total number of such non obtainable amounts.
 
Example 1:
Input: X = 2, Y = 5
Output: 3 2
Explanation: 3 is the largest amount that
can not be formed using 2 and 5. And there 
are only 2 such non obtainable amounts and 
they are 1 and 3.
Example 2:
Input: 5 10
Output: -1
Explanation: Using 5 and 10 there can be 
infinite number of amounts that cannot be
formed.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function frobenius() which takes X and Y as input parameters and returns a list of two numbers in which first number should be maximum amount that cannot be obtained and the second number should be total number of non-obtainable amounts. If no such value exist then returns a list containing -1.
 
Expected Time Complexity: O(log_{2}(max(X, Y)))
Expected Space Complexity: O(1)
 
Constraints:
2 <= X, Y <= 10000
"""

def find_largest_non_obtainable_amount(X: int, Y: int) -> list:
    def gcd(a: int, b: int) -> int:
        if b == 0:
            return a
        return gcd(b, a % b)
    
    if gcd(X, Y) != 1:
        return [-1]
    
    largest_non_obtainable = X * Y - (X + Y)
    total_non_obtainable = (X - 1) * (Y - 1) // 2
    
    return [largest_non_obtainable, total_non_obtainable]