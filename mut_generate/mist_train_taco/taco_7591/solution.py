"""
QUESTION:
You are given an array $a$ consisting of $n$ integers $a_1, a_2, \dots, a_n$.

Your problem is to find such pair of indices $i, j$ ($1 \le i < j \le n$) that $lcm(a_i, a_j)$ is minimum possible.

$lcm(x, y)$ is the least common multiple of $x$ and $y$ (minimum positive number such that both $x$ and $y$ are divisors of this number).


-----Input-----

The first line of the input contains one integer $n$ ($2 \le n \le 10^6$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^7$), where $a_i$ is the $i$-th element of $a$.


-----Output-----

Print two integers $i$ and $j$ ($1 \le i < j \le n$) such that the value of $lcm(a_i, a_j)$ is minimum among all valid pairs $i, j$. If there are multiple answers, you can print any.


-----Examples-----
Input
5
2 4 8 3 6

Output
1 2

Input
5
5 2 11 3 7

Output
2 4

Input
6
2 5 10 1 10 2

Output
1 4
"""

def find_min_lcm_pair(a, n):
    INF = 10 ** 18
    lim = max(a) + 1
    counter = [0] * lim
    
    for num in a:
        counter[num] += 1
    
    mini = INF
    n1, n2 = INF, INF
    
    for i in range(1, lim):
        m, m1 = INF, INF
        for j in range(i, lim, i):
            if counter[j] >= 2:
                m, m1 = j, j
                break
            if counter[j] == 1:
                if m == INF:
                    m = j
                elif m1 == INF:
                    m1 = j
                    break
        
        z = m * m1 // i
        if z < mini:
            mini = z
            n1, n2 = m, m1
    
    ind1, ind2 = -1, -1
    for i in range(n):
        if ind1 == -1 and n1 == a[i]:
            ind1 = i + 1
        elif ind2 == -1 and n2 == a[i]:
            ind2 = i + 1
    
    if ind1 > ind2:
        ind1, ind2 = ind2, ind1
    
    return ind1, ind2