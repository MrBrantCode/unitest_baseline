"""
QUESTION:
Today, as a friendship gift, Bakry gave Badawy $n$ integers $a_1, a_2, \dots, a_n$ and challenged him to choose an integer $X$ such that the value $\underset{1 \leq i \leq n}{\max} (a_i \oplus X)$ is minimum possible, where $\oplus$ denotes the bitwise XOR operation.

As always, Badawy is too lazy, so you decided to help him and find the minimum possible value of $\underset{1 \leq i \leq n}{\max} (a_i \oplus X)$.


-----Input-----

The first line contains integer $n$ ($1\le n \le 10^5$).

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($0 \le a_i \le 2^{30}-1$).


-----Output-----

Print one integer — the minimum possible value of $\underset{1 \leq i \leq n}{\max} (a_i \oplus X)$.


-----Examples-----
Input
3
1 2 3

Output
2

Input
2
1 5

Output
4



-----Note-----

In the first sample, we can choose $X = 3$.

In the second sample, we can choose $X = 5$.
"""

def find_min_max_xor(l, ans=0, pow_=30):
    if pow_ == -1:
        return ans
    one = []
    zero = []
    for i in l:
        if i & 1 << pow_ != 0:
            one.append(i)
        else:
            zero.append(i)
    if zero == [] or one == []:
        return find_min_max_xor(l, ans, pow_ - 1)
    else:
        return min(find_min_max_xor(zero, ans + (1 << pow_), pow_ - 1), 
                   find_min_max_xor(one, ans + (1 << pow_), pow_ - 1))