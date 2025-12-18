"""
QUESTION:
Akash singh is a student of Mathematics at Geekland University. These days he is busy with his girlfriend Jassi. On the other hand, Jassi don't like mathematics that much. One day, Jassi decided to find all the strings of length N (comprising only of characters from '0' to '9') having odd number of 0's.
For Example: 103,012,000 are all strings of length 3 having Odd number of 0's.
She asked Akash to find number of such strings of for a given length of string modulus 1000000009 (10^9 + 9). Akash being busy in organizing college fest asks for your help. Help Akash impressing his girlfriend.

Input: 

First line of input contains an integer t(t ≤ 10000) which is the number of test cases, then, t lines follow each containing an integer N ≤ 10^18

Output:

For each test case print single integer, the number of strings of length N comprising only of characters from '0' to '9'. Having odd number of zeroes. 

SAMPLE INPUT
2
1
2

SAMPLE OUTPUT
1
18

Explanation

Case 1:  only possible case is '0'. 
Case 2: The following string of length 2 contains odd number of zeroes: 
            01,02...,09,10 --> 10 numbers
            20,30,...,90 ---> 8 numbers
            total 18 numbers
"""

def count_strings_with_odd_zeros(N: int, mod: int = 1000000009) -> int:
    """
    Calculate the number of strings of length N comprising only of characters from '0' to '9'
    that have an odd number of '0's, modulo 1000000009 (10^9 + 9).

    Parameters:
    N (int): The length of the string.
    mod (int, optional): The modulus value to use in the calculation. Default is 1000000009.

    Returns:
    int: The number of such strings modulo mod.
    """
    if N == 1:
        return 1  # Only possible string is '0'
    
    # Calculate the number of valid strings using the given formula
    result = (pow(2, N-1, mod) * (pow(5, N, mod) - pow(4, N, mod))) % mod
    return result