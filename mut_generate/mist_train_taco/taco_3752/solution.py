"""
QUESTION:
The chef has a number N, Cheffina challenges chef to form the largest number X from the digits of N.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, $N$. 

-----Output:-----
For each test case, output in a single line answer.

-----Constraints-----
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^6$

-----Sample Input:-----
2
2
212

-----Sample Output:-----
2
221
"""

def form_largest_number(test_cases):
    results = []
    for num in test_cases:
        digits = list(map(int, str(num)))
        digits.sort(reverse=True)
        largest_number = int(''.join(map(str, digits)))
        results.append(largest_number)
    return results