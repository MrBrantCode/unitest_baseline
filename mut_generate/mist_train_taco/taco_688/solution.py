"""
QUESTION:
Heading ##There are two integers A and B. You are required to compute the bitwise AND amongst all natural numbers lying between A and B, both inclusive.
Input Format

First line of the input contains T, the number of testcases to follow.
Each testcase in a newline contains A and B separated by a single space.

Constraints

1≤T≤200

0≤A≤B<232

Output Format

Output one line per test case with the required bitwise AND.

SAMPLE INPUT
3 
12 15 
2 3 
8 13

SAMPLE OUTPUT
12 
2 
8

Explanation

1st Test Case : 12 & 13 & 14 & 15 = 12

2nd Test Case : 2 & 3 = 2

3rd Test Case : 8 & 9 & 10 & 11 & 12 & 13 = 8
"""

def bitwise_and_between_range(A: int, B: int) -> int:
    """
    Computes the bitwise AND of all natural numbers between A and B (inclusive).

    Parameters:
    A (int): The starting integer of the range.
    B (int): The ending integer of the range.

    Returns:
    int: The result of the bitwise AND operation on all natural numbers between A and B.
    """
    # The bitwise AND of all numbers in the range [A, B] can be determined by finding
    # the common prefix of all numbers in the range. This is because any differing
    # bits will eventually become zero when ANDed together.
    
    # To find the common prefix, we can shift both A and B right until they are equal,
    # and then shift back by the same number of positions.
    
    shift = 0
    while A != B:
        A >>= 1
        B >>= 1
        shift += 1
    
    return A << shift