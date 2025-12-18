"""
QUESTION:
You are given an array of $n$ integers $a_1, a_2, \ldots, a_n$. The integers are either $1$ or $-1$. You have to perform the following operation exactly once on the array $a$:

Choose an index $i$ ($1 \leq i < n$) and flip the signs of $a_i$ and $a_{i+1}$. Here, flipping the sign means $-1$ will be $1$ and $1$ will be $-1$.

What is the maximum possible value of $a_1 + a_2 + \ldots + a_n$ after applying the above operation?


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 500$). Description of the test cases follows.

The first line of each test case contains a single integer $n$ ($2 \le n \le 10^5$), the length of the array $a$.

The next line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($a_i = 1$ or $a_i = -1$).

The sum of $n$ over all cases doesn't exceed $10^5$.


-----Output-----

For each test case, print the maximum possible sum of the array $a$ you can get in a separate line.


-----Examples-----

Input
4
5
-1 1 1 -1 -1
5
1 1 -1 -1 -1
2
1 1
4
1 -1 -1 1
Output
3
3
-2
4


-----Note-----

In the first case, we can choose index $4$ and flip the signs of $a_4$ and $a_5$. After this operation, the sum will be $-1+1+1+1+1 = 3$. We can't make the sum larger than this.

In the third case, the only option is to choose the index $1$.
"""

def max_possible_sum_after_flip(ai: list) -> int:
    """
    Calculate the maximum possible sum of the array after performing the specified flip operation.

    Parameters:
    ai (list): A list of integers where each integer is either 1 or -1.

    Returns:
    int: The maximum possible sum of the array after performing the flip operation.
    """
    n = len(ai)
    s = sum(ai)
    h = False
    
    for j in range(n - 1):
        if (ai[j] == -1) and (ai[j + 1] == -1):
            h = True
            return s + 4
            break
    
    if not h:
        if ai.count(-1) == 0:
            return s - 4
        else:
            return s