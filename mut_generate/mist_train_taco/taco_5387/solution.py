"""
QUESTION:
Patlu has recently got a new problem based on Pallindromes. A Pallindrome is a number that is same from front and back, example $121$ is pallindrome but $123$ is not . He wants to calculate sum of all $N$ digit number which are Pallindromic in nature and divisible by $9$ and does not contain any zero in their decimal representation. As the answer can be very large so print the sum modulo $10^9 + 7$.

-----Input:-----
- First line of input contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains single line of input , one integer $N$.

-----Output:-----
- For each testcase, output in a single line answer having $N$ digits pallindromic string.

-----Constraints-----
- $1\leq T \leq 100$
- $1\leq N \leq 10^5$

-----Sample Input:-----
2
1
2

-----Sample Output:-----
9
99
"""

def sum_of_n_digit_palindromic_numbers(N: int) -> int:
    """
    Calculate the sum of all N-digit palindromic numbers that are divisible by 9 and do not contain any zero.
    
    Parameters:
    N (int): The number of digits in the palindromic numbers.
    
    Returns:
    int: The sum of all such N-digit palindromic numbers modulo 10^9 + 7.
    """
    if N == 1:
        return 9
    if N == 2:
        return 99
    
    s = '5' * N
    s = int(s)
    
    if N % 2 == 0:
        s = s * pow(9, N // 2 - 1)
    else:
        s = s * pow(9, N // 2)
    
    return s % (pow(10, 9) + 7)