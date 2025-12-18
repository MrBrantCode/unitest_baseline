"""
QUESTION:
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

 
Constraints:

1 <= n <= 10^5
"""

def calculate_digit_difference(n: int) -> int:
    string_int = str(n)
    product = 1
    sum_digits = 0
    for digit in string_int:
        product *= int(digit)
        sum_digits += int(digit)
    return product - sum_digits