"""
QUESTION:
Solve the mystery.

Input

The first line contains T, the number of test cases.

T lines follow each containing a single integer N.

Output

Output the answer for each test case in a new line.

Constraints

1 ≤ T ≤ 10^5

1 ≤ N ≤ 365

NOTE

There is partial marking for this question

SAMPLE INPUT
5
10
60
100
200
360

SAMPLE OUTPUT
1
3
4
7
12
"""

def solve_mystery(test_cases):
    # Precompute the day-to-month mapping
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_to_month = [0] * 365
    k = 0
    for month in range(1, len(days_in_months)):
        for day in range(days_in_months[month]):
            day_to_month[k] = month
            k += 1
    
    # Process each test case
    results = []
    for n in test_cases:
        results.append(day_to_month[n - 1])
    
    return results