"""
QUESTION:
We have an unsolved mystery this time too! 

Input:

First line of input contains T – the number of test cases. Each of the next T lines contain two integers a and b separated by a space.

Output:

Output T lines, each containing a single integer that is the output of that test case.

Constraints:

1 ≤ T ≤ 300

1 ≤ a ≤ 999

5 ≤ b ≤ 8

SAMPLE INPUT
6
5 5
10 6
2 7
90 6
5 6
2 8

SAMPLE OUTPUT
10
14
2
230
5
2

Explanation

No explanation!!
"""

def process_test_cases(test_cases):
    results = []
    for a, b in test_cases:
        if a < b:
            results.append(a)
        else:
            V = []
            while a >= b:
                V.append(a % b)
                a = a // b
            V.append(a)
            V.reverse()
            S = list(map(str, V))
            results.append(int("".join(S)))
    return results