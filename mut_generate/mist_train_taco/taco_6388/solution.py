"""
QUESTION:
Given two numbers a and b. Find the last digit of a raised to the power b.
Example 1:
Input:
a = 3
b = 4
Output:
1
Explanation:
3^{4} = 81 so the last digit is 1.
Example 2:
Input:
a = 2
b = 8
Output:
6
Explanation:
2^{8} = 256 so the last digit is 6.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function quickExponents() which take two integers a and b and returns the last digit of a raise to the power b.
Expected Time Complexity: O(Log(b))
Expected Auxiliary Space: O(1)
Constraints:
1 <= a, b <= 10^{18}
"""

def last_digit_of_power(a: int, b: int) -> int:
    def fast_power(base: int, exp: int) -> int:
        if exp == 0:
            return 1
        if exp % 2 == 0:
            return fast_power((base * (base % 10)) % 10, exp // 2)
        else:
            return (base * fast_power((base * (base % 10)) % 10, exp // 2)) % 10
    
    return fast_power(a % 10, b)