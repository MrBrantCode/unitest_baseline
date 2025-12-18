"""
QUESTION:
Polycarp has $n$ coins, the value of the $i$-th coin is $a_i$. It is guaranteed that all the values are integer powers of $2$ (i.e. $a_i = 2^d$ for some non-negative integer number $d$).

Polycarp wants to know answers on $q$ queries. The $j$-th query is described as integer number $b_j$. The answer to the query is the minimum number of coins that is necessary to obtain the value $b_j$ using some subset of coins (Polycarp can use only coins he has). If Polycarp can't obtain the value $b_j$, the answer to the $j$-th query is -1.

The queries are independent (the answer on the query doesn't affect Polycarp's coins).


-----Input-----

The first line of the input contains two integers $n$ and $q$ ($1 \le n, q \le 2 \cdot 10^5$) — the number of coins and the number of queries.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ — values of coins ($1 \le a_i \le 2 \cdot 10^9$). It is guaranteed that all $a_i$ are integer powers of $2$ (i.e. $a_i = 2^d$ for some non-negative integer number $d$).

The next $q$ lines contain one integer each. The $j$-th line contains one integer $b_j$ — the value of the $j$-th query ($1 \le b_j \le 10^9$).


-----Output-----

Print $q$ integers $ans_j$. The $j$-th integer must be equal to the answer on the $j$-th query. If Polycarp can't obtain the value $b_j$ the answer to the $j$-th query is -1.


-----Example-----
Input
5 4
2 4 8 2 4
8
5
14
10

Output
1
-1
3
2
"""

from collections import Counter

def min_coins_for_queries(coins, queries):
    # Count the occurrences of each coin value
    coin_counts = Counter(coins)
    
    # Prepare a list to store the count of coins for each power of 2
    counts = [0] * 32
    for value, count in coin_counts.items():
        counts[value.bit_length() - 1] = count
    
    results = []
    
    for bj in queries:
        ans = 0
        for i in reversed(range(32)):
            count = min(bj >> i, counts[i])
            ans += count
            bj -= count << i
        if bj != 0:
            results.append(-1)
        else:
            results.append(ans)
    
    return results