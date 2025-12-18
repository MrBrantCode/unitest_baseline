"""
QUESTION:
Let's define $S(x)$ to be the sum of digits of number $x$ written in decimal system. For example, $S(5) = 5$, $S(10) = 1$, $S(322) = 7$.

We will call an integer $x$ interesting if $S(x + 1) < S(x)$. In each test you will be given one integer $n$. Your task is to calculate the number of integers $x$ such that $1 \le x \le n$ and $x$ is interesting.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 1000$)  — number of test cases.

Then $t$ lines follow, the $i$-th line contains one integer $n$ ($1 \le n \le 10^9$) for the $i$-th test case.


-----Output-----

Print $t$ integers, the $i$-th should be the answer for the $i$-th test case.


-----Examples-----

Input
5
1
9
10
34
880055535
Output
0
1
1
3
88005553


-----Note-----

The first interesting number is equal to $9$.
"""

def count_interesting_numbers(t: int, n_list: list) -> list:
    """
    Calculate the number of interesting integers x such that 1 <= x <= n for each given n.

    An integer x is considered interesting if S(x + 1) < S(x), where S(x) is the sum of digits of x.

    Parameters:
    t (int): The number of test cases.
    n_list (list): A list of integers where each integer n represents the upper limit for the test case.

    Returns:
    list: A list of integers where each integer is the count of interesting numbers for the corresponding n.
    """
    results = []
    for n in n_list:
        results.append(int((n + 1) // 10))
    return results