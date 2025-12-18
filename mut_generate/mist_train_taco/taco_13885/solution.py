"""
QUESTION:
You are given an integer $n$. Find a sequence of $n$ distinct integers $a_1, a_2, \dots, a_n$ such that $1 \leq a_i \leq 10^9$ for all $i$ and $$\max(a_1, a_2, \dots, a_n) - \min(a_1, a_2, \dots, a_n)= \sqrt{a_1 + a_2 + \dots + a_n}.$$

It can be proven that there exists a sequence of distinct integers that satisfies all the conditions above.


-----Input-----

The first line of input contains $t$ ($1 \leq t \leq 10^4$) — the number of test cases.

The first and only line of each test case contains one integer $n$ ($2 \leq n \leq 3 \cdot 10^5$) — the length of the sequence you have to find.

The sum of $n$ over all test cases does not exceed $3 \cdot 10^5$.


-----Output-----

For each test case, output $n$ space-separated distinct integers $a_1, a_2, \dots, a_n$ satisfying the conditions in the statement.

If there are several possible answers, you can output any of them. Please remember that your integers must be distinct!


-----Examples-----

Input
3
2
5
4
Output
3 1
20 29 18 26 28
25 21 23 31


-----Note-----

In the first test case, the maximum is $3$, the minimum is $1$, the sum is $4$, and $3 - 1 = \sqrt{4}$.

In the second test case, the maximum is $29$, the minimum is $18$, the sum is $121$, and $29-18 = \sqrt{121}$.

For each test case, the integers are all distinct.
"""

def generate_distinct_sequences(t: int, n_list: list[int]) -> list[list[int]]:
    """
    Generates sequences of distinct integers for each test case that satisfy the given conditions.

    Parameters:
    t (int): The number of test cases.
    n_list (list[int]): A list of integers where each integer represents the length of the sequence for each test case.

    Returns:
    list[list[int]]: A list of lists where each inner list contains the sequence of distinct integers for each test case.
    """
    results = []
    
    for n in n_list:
        if n % 2:
            ad = n - (n + 1) // 2
            v = [i + ad + 2 for i in range(1, n + 1)]
            v[0] -= 1
            v[-1] += 1
            v[-2] += 1
        else:
            ad = (2 * n - 1 - (n + 1)) // 2
            v = [i + ad for i in range(1, n + 1)]
            for i in range(len(v) - n // 2, len(v)):
                v[i] += 1
        
        results.append(v)
    
    return results