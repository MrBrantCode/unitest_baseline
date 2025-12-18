"""
QUESTION:
Calculate the sum of the series :

INPUT:

First line contains the number of test cases t, for each test case a single line representing m and n with two space separated integers.

OUTPUT:

For each test case, a single line representing thee sum of the series in the form of p/q.

Constraints:

1 ≤ t ≤ 100

1 ≤ m, n ≤ 30

SAMPLE INPUT
1
2 3

SAMPLE OUTPUT
31/224
"""

def calculate_series_sum(t, test_cases):
    results = []
    for m, n in test_cases:
        p, q = 2**(m+n), 2**(n)
        result = f"{p-1}/{p*(q-1)}"
        results.append(result)
    return results