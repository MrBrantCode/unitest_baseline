"""
QUESTION:
Vivek was roaming around in the electronics shop, where he saw a box called as BlackBox. He was intrigued by its function, so he bought it. It's functionality states that for given integer input N  ≤ 1000  - it outputs the sum of all the digits in factorial of N (N!).

Now Vivek wants to extend its functionality for large numbers. So, he wants you to write a program that can check the correctness of the BlackBox . 

INPUT :  

The first line of the input contains a single integer T ( the number of test cases ). Next T lines of input contains an integer N .

OUTPUT :  

For each test case, print the sum of all digits in the factorial of the corresponding input integer.

CONSTRAINTS :  

1 ≤ T ≤ 10^3  

0 ≤ N ≤ 1000

SAMPLE INPUT
5
1
2
3
4
5

SAMPLE OUTPUT
1
2
6
6
3

Explanation

for test 1, N=1 , factorial of N = 1 ,      sum of digits = 1.
for test 2, N=2 , factorial of N = 2 ,      sum of digits = 2.
for test 3, N=3 , factorial of N = 6 ,      sum of digits = 6.
for test 4, N=4 , factorial of N = 24 ,    sum of digits = 6.
for test 5, N=5 , factorial of N = 120 , sum of digits = 3.
"""

def calculate_factorial_digit_sum(N: int) -> int:
    """
    Calculate the sum of all digits in the factorial of a given integer N.

    Parameters:
    N (int): The integer for which the factorial digit sum is to be calculated.

    Returns:
    int: The sum of all digits in the factorial of N.
    """
    if N == 0:
        return 1  # 0! is 1, and sum of digits of 1 is 1
    
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    
    digit_sum = sum(map(int, str(factorial)))
    return digit_sum