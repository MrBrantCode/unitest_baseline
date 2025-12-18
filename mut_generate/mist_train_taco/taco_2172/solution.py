"""
QUESTION:
The only difference between the easy and the hard versions is the maximum value of $k$.

You are given an infinite sequence of form "112123123412345$\dots$" which consist of blocks of all consecutive positive integers written one after another. The first block consists of all numbers from $1$ to $1$, the second one — from $1$ to $2$, the third one — from $1$ to $3$, $\dots$, the $i$-th block consists of all numbers from $1$ to $i$. 

So the first $56$ elements of the sequence are "11212312341234512345612345671234567812345678912345678910". Elements of the sequence are numbered from one. For example, the $1$-st element of the sequence is $1$, the $3$-rd element of the sequence is $2$, the $20$-th element of the sequence is $5$, the $38$-th element is $2$, the $56$-th element of the sequence is $0$.

Your task is to answer $q$ independent queries. In the $i$-th query you are given one integer $k_i$. Calculate the digit at the position $k_i$ of the sequence.


-----Input-----

The first line of the input contains one integer $q$ ($1 \le q \le 500$) — the number of queries.

The $i$-th of the following $q$ lines contains one integer $k_i$ $(1 \le k_i \le 10^9)$ — the description of the corresponding query.


-----Output-----

Print $q$ lines. In the $i$-th line print one digit $x_i$ $(0 \le x_i \le 9)$ — the answer to the query $i$, i.e. $x_i$ should be equal to the element at the position $k_i$ of the sequence.


-----Examples-----
Input
5
1
3
20
38
56

Output
1
2
5
2
0

Input
4
2132
506
999999999
1000000000

Output
8
2
9
8



-----Note-----

Answers on queries from the first example are described in the problem statement.
"""

def find_digit_in_sequence(k: int) -> int:
    """
    Finds the digit at the specified position k in the infinite sequence "112123123412345...".

    Parameters:
    k (int): The position in the sequence (1-based index).

    Returns:
    int: The digit at the specified position k.
    """
    strs = []
    s_ps = [0]
    t_ps = [0]
    s_len = 0
    t_len = 0
    x = 0

    while t_len < k:
        x += 1
        xs = str(x)
        strs.append(xs)
        s_len += len(xs)
        s_ps.append(s_len)
        t_len += s_len
        t_ps.append(t_len)

    nn = k - t_ps[-2]
    si = bisect_left(s_ps, nn) - 1
    ss = strs[si] if si < len(strs) else None
    sci = nn - s_ps[si] - 1
    sc = ss[sci]

    return int(sc)