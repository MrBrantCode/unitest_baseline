"""
QUESTION:
Given a number n, write code to find the sum of digits in the factorial of the number.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n, the number.
Output:
Print the sum of digits in the factorial of the number.
Constraints:
1<=T<=1000
1<=n<=5000
Example:
Input:
2
10
100
Output:
27
648
"""

def sum_of_digits_in_factorial(n):
    # Calculate the factorial of n
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    
    # Calculate the sum of digits in the factorial
    sum_of_digit = 0
    for digit in str(fact):
        sum_of_digit += int(digit)
    
    return sum_of_digit