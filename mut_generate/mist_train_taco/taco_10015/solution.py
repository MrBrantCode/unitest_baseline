"""
QUESTION:
Andrewid the Android is a galaxy-famous detective. In his free time he likes to think about strings containing zeros and ones.

Once he thought about a string of length n consisting of zeroes and ones. Consider the following operation: we choose any two adjacent positions in the string, and if one them contains 0, and the other contains 1, then we are allowed to remove these two digits from the string, obtaining a string of length n - 2 as a result.

Now Andreid thinks about what is the minimum length of the string that can remain after applying the described operation several times (possibly, zero)? Help him to calculate this number.


-----Input-----

First line of the input contains a single integer n (1 ≤ n ≤ 2·10^5), the length of the string that Andreid has.

The second line contains the string of length n consisting only from zeros and ones.


-----Output-----

Output the minimum length of the string that may remain after applying the described operations several times.


-----Examples-----
Input
4
1100

Output
0

Input
5
01010

Output
1

Input
8
11101111

Output
6



-----Note-----

In the first sample test it is possible to change the string like the following: $1100 \rightarrow 10 \rightarrow(\text{empty})$.

In the second sample test it is possible to change the string like the following: $01010 \rightarrow 010 \rightarrow 0$.

In the third sample test it is possible to change the string like the following: $11101111 \rightarrow 111111$.
"""

def minimum_length_after_operations(n: int, s: str) -> int:
    """
    Calculate the minimum length of the string that can remain after applying the described operations.

    Parameters:
    n (int): The length of the string.
    s (str): The string consisting of '0's and '1's.

    Returns:
    int: The minimum length of the string that can remain.
    """
    o = 0  # Count of '1's
    z = 0  # Count of '0's
    
    for i in range(n):
        if s[i] == '0':
            z += 1
        else:
            o += 1
    
    return abs(z - o)