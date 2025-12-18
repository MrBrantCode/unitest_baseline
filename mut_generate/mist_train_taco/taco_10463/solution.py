"""
QUESTION:
Little girl Margarita is a big fan of competitive programming. She especially loves problems about arrays and queries on them.

Recently, she was presented with an array $a$ of the size of $10^9$ elements that is filled as follows:   $a_1 = -1$  $a_2 = 2$  $a_3 = -3$  $a_4 = 4$  $a_5 = -5$  And so on ... 

That is, the value of the $i$-th element of the array $a$ is calculated using the formula $a_i = i \cdot (-1)^i$.

She immediately came up with $q$ queries on this array. Each query is described with two numbers: $l$ and $r$. The answer to a query is the sum of all the elements of the array at positions from $l$ to $r$ inclusive.

Margarita really wants to know the answer to each of the requests. She doesn't want to count all this manually, but unfortunately, she couldn't write the program that solves the problem either. She has turned to you — the best programmer.

Help her find the answers!


-----Input-----

The first line contains a single integer $q$ ($1 \le q \le 10^3$) — the number of the queries.

Each of the next $q$ lines contains two integers $l$ and $r$ ($1 \le l \le r \le 10^9$) — the descriptions of the queries.


-----Output-----

Print $q$ lines, each containing one number — the answer to the query. 


-----Example-----
Input
5
1 3
2 5
5 5
4 4
2 3

Output
-2
-2
-5
4
-1



-----Note-----

In the first query, you need to find the sum of the elements of the array from position $1$ to position $3$. The sum is equal to $a_1 + a_2 + a_3 = -1 + 2 -3 = -2$.

In the second query, you need to find the sum of the elements of the array from position $2$ to position $5$. The sum is equal to $a_2 + a_3 + a_4 + a_5 = 2 -3 + 4 - 5 = -2$.

In the third query, you need to find the sum of the elements of the array from position $5$ to position $5$. The sum is equal to $a_5 = -5$.

In the fourth query, you need to find the sum of the elements of the array from position $4$ to position $4$. The sum is equal to $a_4 = 4$.

In the fifth query, you need to find the sum of the elements of the array from position $2$ to position $3$. The sum is equal to $a_2 + a_3 = 2 - 3 = -1$.
"""

def calculate_query_sum(l: int, r: int) -> int:
    """
    Calculate the sum of elements in the array from position `l` to position `r` inclusive.
    
    The array is defined such that:
    - a_i = i * (-1)^i
    
    Parameters:
    l (int): The starting index of the query (1-based index).
    r (int): The ending index of the query (1-based index).
    
    Returns:
    int: The sum of the elements from position `l` to position `r`.
    """
    s = 0
    if l == r:
        if l % 2:
            return -l
        else:
            return l
    else:
        if l % 2 == 0:
            s += l
            l += 1
        if r % 2:
            s -= r
            r -= 1
        if l == r:
            if l % 2:
                s -= l
            else:
                s += l
        else:
            n = r - l + 1
            n //= 2
            s += n * (l + 1 + r) // 2
            s -= n * (l + r - 1) // 2
        return s