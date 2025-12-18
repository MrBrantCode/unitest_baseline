"""
QUESTION:
The subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

You are given an integer $n$. 

You have to find a sequence $s$ consisting of digits $\{1, 3, 7\}$ such that it has exactly $n$ subsequences equal to $1337$.

For example, sequence $337133377$ has $6$ subsequences equal to $1337$:   $337\underline{1}3\underline{3}\underline{3}7\underline{7}$ (you can remove the second and fifth characters);  $337\underline{1}\underline{3}3\underline{3}7\underline{7}$ (you can remove the third and fifth characters);  $337\underline{1}\underline{3}\underline{3}37\underline{7}$ (you can remove the fourth and fifth characters);  $337\underline{1}3\underline{3}\underline{3}\underline{7}7$ (you can remove the second and sixth characters);  $337\underline{1}\underline{3}3\underline{3}\underline{7}7$ (you can remove the third and sixth characters);  $337\underline{1}\underline{3}\underline{3}3\underline{7}7$ (you can remove the fourth and sixth characters). 

Note that the length of the sequence $s$ must not exceed $10^5$.

You have to answer $t$ independent queries.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10$) — the number of queries. 

Next $t$ lines contains a description of queries: the $i$-th line contains one integer $n_i$ ($1 \le n_i \le 10^9$).


-----Output-----

For the $i$-th query print one string $s_i$ ($1 \le |s_i| \le 10^5$) consisting of digits $\{1, 3, 7\}$. String $s_i$ must have exactly $n_i$ subsequences $1337$. If there are multiple such strings, print any of them.


-----Example-----
Input
2
6
1

Output
113337
1337
"""

def generate_sequences(t: int, queries: list) -> list:
    """
    Generates sequences of digits {1, 3, 7} such that each sequence has exactly `n` subsequences equal to "1337".

    Parameters:
    t (int): The number of queries.
    queries (list): A list of integers where each integer represents the value of `n` for each query.

    Returns:
    list: A list of strings where each string is the sequence `s` for the corresponding query.
    """
    results = []
    for n in queries:
        if n <= 10 ** 5 - 3:
            results.append('1' * n + '337')
            continue
        b = 0
        while True:
            total = (b + 2) * (b + 1) // 2
            if 0 <= n - total and n - total + b + 4 <= 10 ** 5:
                a = n - total
                results.append('133' + '7' * a + '3' * b + '7')
                break
            b += 1
    return results