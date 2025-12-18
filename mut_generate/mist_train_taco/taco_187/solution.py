"""
QUESTION:
Count the number of 2s as digit in all numbers from 0 to n.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains the input integer n.
Output:
Print the count of the number of 2s as digit in all numbers from 0 to n.
Constraints:
1<=T<=100
1<=N<=10^5
Example:
Input:
2
22
100
Output:
6
20
"""

def count_twos_in_range(n: int) -> int:
    s = ''
    for i in range(n + 1):
        s += str(i)
    return s.count('2')