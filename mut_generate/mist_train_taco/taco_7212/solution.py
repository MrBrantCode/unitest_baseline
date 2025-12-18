"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.

In this problem, a substring is defined as a sequence of continuous characters S_{i}, S_{i+1}, ..., S_{j} where 1 ≤ i ≤ j ≤ N.

------ Input ------ 

First line contains T, the number of testcases. Each testcase consists of N(the length of string) in one line and string in second line.

------ Output ------ 

For each testcase, print the required answer in one line.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$Sum of  N  over all testcases ≤ 10^{5}$

----- Sample Input 1 ------ 
2
4
1111
5
10001
----- Sample Output 1 ------ 
10
3
----- explanation 1 ------ 
Test case $1$: All substrings of this string start and end with 1. The substrings are $\{ 1, 1, 1, 1, 11, 11, 11, 111, 111, 1111 \}$. The total count of these substrings is $10$.

Test case $2$: Three substrings of this string start and end with 1. These are $\{1, 1, 10001\}$.
"""

def count_substrings_starting_ending_with_one(s: str) -> int:
    """
    Counts the number of substrings in the given string 's' that start and end with '1'.

    Parameters:
    s (str): A string consisting of only '1's and '0's.

    Returns:
    int: The number of substrings that start and end with '1'.
    """
    c = s.count('1')
    return c * (c + 1) // 2