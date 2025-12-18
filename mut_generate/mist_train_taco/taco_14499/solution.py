"""
QUESTION:
Given A and B, count the numbers N such that A ≤ N ≤ B and N is a palindrome.   

Examples: 
Palindromes: 121, 11 , 11411 
Not Palindromes: 122, 10

Input: 
First line contains T, the number of testcases. Each testcase consists of two integers A and B in one line.

Output: 
For each testcase, print the required answer in one line.

Constraints: 
1 ≤ T ≤ 10 
0 ≤ A ≤ B ≤ 10^5

SAMPLE INPUT
2
10 13
20 30

SAMPLE OUTPUT
1
1
"""

def count_palindromes(A: int, B: int) -> int:
    """
    Counts the number of palindromic numbers between A and B (inclusive).

    Parameters:
    A (int): The lower bound of the range.
    B (int): The upper bound of the range.

    Returns:
    int: The count of palindromic numbers between A and B.
    """
    pal_count = 0
    for num in range(A, B + 1):
        s = str(num)
        if s == s[::-1]:
            pal_count += 1
    return pal_count