"""
QUESTION:
You are given an integer $n$. Find a sequence of $n$ integers $a_1, a_2, \dots, a_n$ such that $1 \leq a_i \leq 10^9$ for all $i$ and $$a_1 \oplus a_2 \oplus \dots \oplus a_n = \frac{a_1 + a_2 + \dots + a_n}{n},$$ where $\oplus$ represents the bitwise XOR .

It can be proven that there exists a sequence of integers that satisfies all the conditions above.


-----Input-----

The first line of input contains $t$ ($1 \leq t \leq 10^4$) — the number of test cases.

The first and only line of each test case contains one integer $n$ ($1 \leq n \leq 10^5$) — the length of the sequence you have to find.

The sum of $n$ over all test cases does not exceed $10^5$.


-----Output-----

For each test case, output $n$ space-separated integers $a_1, a_2, \dots, a_n$ satisfying the conditions in the statement.

If there are several possible answers, you can output any of them.


-----Examples-----

Input
3
1
4
3
Output
69
13 2 8 1
7 7 7


-----Note-----

In the first test case, $69 = \frac{69}{1} = 69$.

In the second test case, $13 \oplus 2 \oplus 8 \oplus 1 = \frac{13 + 2 + 8 + 1}{4} = 6$.
"""

def generate_sequence(n: int) -> list[int]:
    """
    Generates a sequence of n integers such that the bitwise XOR of all elements
    equals the average of the sum of all elements.

    Parameters:
    n (int): The length of the sequence to be generated.

    Returns:
    list[int]: A list of n integers satisfying the conditions.
    """
    if n == 1:
        return [69]  # Special case for n = 1
    
    sequence = []
    for i in range(n):
        if n % 2 == 1 or i > 1:
            sequence.append(2)
        elif i == 0:
            sequence.append(1)
        else:
            sequence.append(3)
    
    return sequence