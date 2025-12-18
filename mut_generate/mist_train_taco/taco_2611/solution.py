"""
QUESTION:
You are given a string $\mbox{S}$. 

Your task is to find out whether $\mbox{S}$ is a valid regex or not.

Input Format

The first line contains integer $\mathbf{T}$, the number of test cases. 

The next $\mathbf{T}$ lines contains the string $\mbox{S}$.

Constraints

$\textbf{0}<T<100$

Output Format

Print "True" or "False" for each test case without quotes.

Sample Input
2
.*\+
.*+

Sample Output
True
False

Explanation

.*\+ : Valid regex. 

.*+: Has the error multiple repeat. Hence, it is invalid.
"""

import re

def is_valid_regex(regex_strings):
    results = []
    for s in regex_strings:
        try:
            re.compile(s.rstrip())
            results.append(True)
        except re.error:
            results.append(False)
    return results