"""
QUESTION:
You are given a decimal representation of an integer $x$ without leading zeros.

You have to perform the following reduction on it exactly once: take two neighboring digits in $x$ and replace them with their sum without leading zeros (if the sum is $0$, it's represented as a single $0$).

For example, if $x = 10057$, the possible reductions are:

choose the first and the second digits $1$ and $0$, replace them with $1+0=1$; the result is $1057$;

choose the second and the third digits $0$ and $0$, replace them with $0+0=0$; the result is also $1057$;

choose the third and the fourth digits $0$ and $5$, replace them with $0+5=5$; the result is still $1057$;

choose the fourth and the fifth digits $5$ and $7$, replace them with $5+7=12$; the result is $10012$.

What's the largest number that can be obtained?


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of testcases.

Each testcase consists of a single integer $x$ ($10 \le x < 10^{200000}$). $x$ doesn't contain leading zeros.

The total length of the decimal representations of $x$ over all testcases doesn't exceed $2 \cdot 10^5$.


-----Output-----

For each testcase, print a single integer — the largest number that can be obtained after the reduction is applied exactly once. The number should not contain leading zeros.


-----Examples-----

Input
2
10057
90
Output
10012
9


-----Note-----

The first testcase of the example is already explained in the statement.

In the second testcase, there is only one possible reduction: the first and the second digits.
"""

def largest_reduction(s: str) -> str:
    """
    Perform a reduction on the given integer string `s` by summing two neighboring digits and replacing them with their sum.
    The function returns the largest number that can be obtained after performing this reduction exactly once.

    Parameters:
    s (str): The integer string without leading zeros.

    Returns:
    str: The largest number obtained after the reduction.
    """
    equal = {'19', '28', '29', '37', '38', '39', '46', '47', '48', '49', '55', '56', '57', '58', '59', '64', '65', '66', '67', '68', '69', '73', '74', '75', '76', '77', '78', '79', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99'}
    
    n = len(s)
    for i in range(n - 2, -1, -1):
        if s[i:i + 2] in equal:
            mid = str(int(s[i]) + int(s[i + 1]))
            return s[:i] + mid + s[i + 2:]
    
    mid = str(int(s[0]) + int(s[1]))
    return mid + s[2:]