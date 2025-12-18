"""
QUESTION:
Sereja has two sequences a and b and number p. Sequence a consists of n integers a_1, a_2, ..., a_{n}. Similarly, sequence b consists of m integers b_1, b_2, ..., b_{m}. As usual, Sereja studies the sequences he has. Today he wants to find the number of positions q (q + (m - 1)·p ≤ n; q ≥ 1), such that sequence b can be obtained from sequence a_{q}, a_{q} + p, a_{q} + 2p, ..., a_{q} + (m - 1)p by rearranging elements.

Sereja needs to rush to the gym, so he asked to find all the described positions of q.


-----Input-----

The first line contains three integers n, m and p (1 ≤ n, m ≤ 2·10^5, 1 ≤ p ≤ 2·10^5). The next line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9). The next line contains m integers b_1, b_2, ..., b_{m} (1 ≤ b_{i} ≤ 10^9).


-----Output-----

In the first line print the number of valid qs. In the second line, print the valid values in the increasing order.


-----Examples-----
Input
5 3 1
1 2 3 2 1
1 2 3

Output
2
1 3

Input
6 3 2
1 3 2 2 3 1
1 2 3

Output
2
1 2
"""

def find_valid_positions(n, m, p, a, b):
    def hash_elem(x):
        x = x * 1662634645 + 32544235 & 4294967295
        x = (x >> 13) + (x << 19) & 4294967295
        x = x * 361352451 & 4294967295
        return x
    
    c = [hash_elem(elem) for elem in a]
    c_new = [sum([c[q + p * i] for i in range(m)]) for q in range(min(p, max(0, n - (m - 1) * p)))]
    
    for q in range(p, n - (m - 1) * p):
        prev = c_new[q - p]
        c_new.append(prev - c[q - p] + c[q + p * (m - 1)])
    
    b_check = sum([hash_elem(elem) for elem in b])
    ans1 = 0
    ans = []
    
    for q in range(n - (m - 1) * p):
        c_check = c_new[q]
        if b_check != c_check:
            continue
        else:
            ans1 += 1
            ans.append(q + 1)
    
    return ans1, ans