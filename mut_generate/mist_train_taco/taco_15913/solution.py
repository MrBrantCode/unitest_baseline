"""
QUESTION:
Given a value N, find out the largest palindrome number which is product of two N-digit numbers.
 
Example 1:
Input: N = 2
Output: 9009
Explanation: 9009 is the largest number 
which is product of two 2-digit numbers. 
9009 = 91*99.
Example 2:
Input: N = 1
Output: 9
Explanation: 9 is the largest number 
which is product of two 1-digit numbers. 
3 * 3 = 9.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function LargestProductPalin() which takes N as input parameter and returns largest palindromic product of 2 N-digit numbers.
 
Expected Time Complexity: O(10^{n+1})
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 6
"""

def largest_palindromic_product(n: int) -> int:
    upper_limit = 10 ** n - 1
    lower_limit = 1 + upper_limit // 10
    max_product = 0
    
    for i in range(upper_limit, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j
            if product < max_product:
                break
            number = product
            reverse = 0
            while number != 0:
                reverse = reverse * 10 + number % 10
                number = number // 10
            if product == reverse and product > max_product:
                max_product = product
    
    return max_product