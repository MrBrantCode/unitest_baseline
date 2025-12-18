"""
QUESTION:
You are given an array consisting of $n$ integers $a_1, a_2, \dots , a_n$ and an integer $x$. It is guaranteed that for every $i$, $1 \le a_i \le x$.

Let's denote a function $f(l, r)$ which erases all values such that $l \le a_i \le r$ from the array $a$ and returns the resulting array. For example, if $a = [4, 1, 1, 4, 5, 2, 4, 3]$, then $f(2, 4) = [1, 1, 5]$.

Your task is to calculate the number of pairs $(l, r)$ such that $1 \le l \le r \le x$ and $f(l, r)$ is sorted in non-descending order. Note that the empty array is also considered sorted.


-----Input-----

The first line contains two integers $n$ and $x$ ($1 \le n, x \le 10^6$) — the length of array $a$ and the upper limit for its elements, respectively.

The second line contains $n$ integers $a_1, a_2, \dots a_n$ ($1 \le a_i \le x$).


-----Output-----

Print the number of pairs $1 \le l \le r \le x$ such that $f(l, r)$ is sorted in non-descending order.


-----Examples-----
Input
3 3
2 3 1

Output
4

Input
7 4
1 3 1 2 2 4 3

Output
6



-----Note-----

In the first test case correct pairs are $(1, 1)$, $(1, 2)$, $(1, 3)$ and $(2, 3)$.

In the second test case correct pairs are $(1, 3)$, $(1, 4)$, $(2, 3)$, $(2, 4)$, $(3, 3)$ and $(3, 4)$.
"""

def count_sorted_pairs(n, x, a):
    mi = [x + 1] * (x + 1)
    ma = [0] * (x + 1)
    trie = [0] * (1 << 23)
    m = 4
    trie[0] = x + 1
    
    for i in a:
        at = 0
        mii = x + 1
        maa = 0
        for j in range(19, -1, -1):
            if i & 1 << j:
                if not trie[at + 3]:
                    trie[at + 3] = m
                    at = m
                    trie[m] = i
                    trie[m + 1] = i
                    m += 4
                else:
                    at = trie[at + 3]
                    trie[at] = min(trie[at + 0], i)
                    trie[at + 1] = max(trie[at + 1], i)
            else:
                if trie[at + 3]:
                    mii = trie[trie[at + 3]]
                    if not maa:
                        maa = trie[trie[at + 3] + 1]
                if not trie[at + 2]:
                    trie[at + 2] = m
                    at = m
                    trie[m] = i
                    trie[m + 1] = i
                    m += 4
                else:
                    at = trie[at + 2]
                    trie[at] = min(trie[at + 0], i)
                    trie[at + 1] = max(trie[at + 1], i)
        mi[i] = min(mi[i], mii)
        ma[i] = max(ma[i], maa)
    
    fi = 0
    for i in range(x, 0, -1):
        if mi[i] != x + 1:
            fi = i
            break
    
    ans = 0
    g = x + 1
    for i in range(1, x + 1):
        ans += x - max(i, fi) + 1
        if i == g:
            break
        fi = max(fi, ma[i])
        g = min(g, mi[i])
    
    return ans