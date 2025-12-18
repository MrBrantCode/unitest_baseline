"""
QUESTION:
At the children's day, the child came to Picks's house, and messed his house up. Picks was angry at him. A lot of important things were lost, in particular the favorite set of Picks.

Fortunately, Picks remembers something about his set S:  its elements were distinct integers from 1 to limit;  the value of $\sum_{x \in S} \text{lowbit}(x)$ was equal to sum; here lowbit(x) equals 2^{k} where k is the position of the first one in the binary representation of x. For example, lowbit(10010_2) = 10_2, lowbit(10001_2) = 1_2, lowbit(10000_2) = 10000_2 (binary representation). 

Can you help Picks and find any set S, that satisfies all the above conditions?


-----Input-----

The first line contains two integers: sum, limit (1 ≤ sum, limit ≤ 10^5).


-----Output-----

In the first line print an integer n (1 ≤ n ≤ 10^5), denoting the size of S. Then print the elements of set S in any order. If there are multiple answers, print any of them.

If it's impossible to find a suitable set, print -1.


-----Examples-----
Input
5 5

Output
2
4 5

Input
4 3

Output
3
2 3 1

Input
5 1

Output
-1



-----Note-----

In sample test 1: lowbit(4) = 4, lowbit(5) = 1, 4 + 1 = 5.

In sample test 2: lowbit(1) = 1, lowbit(2) = 2, lowbit(3) = 1, 1 + 2 + 1 = 4.
"""

def find_order(limit):
    order = 0
    while limit > 1:
        limit = limit >> 1
        order += 1
    return order

def find_set_with_lowbit_sum(sum_value, limit):
    order = find_order(limit)
    ans = []
    while sum_value != 0:
        if order == -1:
            return [-1]
        multiplier = 1
        base = 2 ** order
        cur_num = base * multiplier
        while cur_num <= limit and base <= sum_value:
            ans.append(cur_num)
            sum_value -= base
            multiplier += 2
            cur_num = base * multiplier
        order -= 1
    return ans