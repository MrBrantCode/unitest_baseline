"""
QUESTION:
Given two numbers A and B. The task is to compute the last digit of the resulting F, where F= B! / A! .
Example 1:
Input: A = 2, B = 4
Output: 2
Explaination: The value of F = 12. So the 
last digit is 2.
Example 2:
Input: A = 3, B = 8
Output: 0
Explaination: F is 6720. So the last value 
is 0.
Your Task:
You do not need to read the input or print anything. Your task is to complete the function lastDigit() which takes A and B and returns the last value of F.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints: 
1 ≤ A ≤ B ≤ 10^{18}
"""

def last_digit_of_factorial_division(A: int, B: int) -> int:
    ans = 1
    for i in range(A + 1, min(B + 1, A + 11)):
        ans = ans * i % 10
    return ans