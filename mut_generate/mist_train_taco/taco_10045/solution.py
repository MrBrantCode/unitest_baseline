"""
QUESTION:
While discussing a proper problem A for a Codeforces Round, Kostya created a cyclic array of positive integers $a_1, a_2, \ldots, a_n$. Since the talk was long and not promising, Kostya created a new cyclic array $b_1, b_2, \ldots, b_{n}$ so that $b_i = (a_i \mod a_{i + 1})$, where we take $a_{n+1} = a_1$. Here $mod$ is the modulo operation. When the talk became interesting, Kostya completely forgot how array $a$ had looked like. Suddenly, he thought that restoring array $a$ from array $b$ would be an interesting problem (unfortunately, not A).


-----Input-----

The first line contains a single integer $n$ ($2 \le n \le 140582$) — the length of the array $a$.

The second line contains $n$ integers $b_1, b_2, \ldots, b_{n}$ ($0 \le b_i \le 187126$).


-----Output-----

If it is possible to restore some array $a$ of length $n$ so that $b_i = a_i \mod a_{(i \mod n) + 1}$ holds for all $i = 1, 2, \ldots, n$, print «YES» in the first line and the integers $a_1, a_2, \ldots, a_n$ in the second line. All $a_i$ should satisfy $1 \le a_i \le 10^{18}$. We can show that if an answer exists, then an answer with such constraint exists as well.

It it impossible to restore any valid $a$, print «NO» in one line.

You can print each letter in any case (upper or lower).


-----Examples-----
Input
4
1 3 1 0

Output
YES
1 3 5 2

Input
2
4 4

Output
NO



-----Note-----

In the first example:  $1 \mod 3 = 1$  $3 \mod 5 = 3$  $5 \mod 2 = 1$  $2 \mod 1 = 0$
"""

def restore_array_a(n, b):
    if n == 2:
        if b[0] == b[1] and b[0] == 0:
            return "YES", [1, 1]
        else:
            return "NO",
    
    i = n - 1
    while b[i - 1] >= b[i] and i > 0:
        i -= 1
    
    if i == 0 and b[0] == b[n - 1]:
        if b[0] != 0:
            return "NO",
        else:
            return "YES", [1] * n
    
    k = i + 1
    b.insert(0, b[n - 1])
    a = [None] * (n + 1)
    a[k] = b[k]
    
    for i in range(k - 1, 0, -1):
        a[i] = b[i] + a[i + 1]
        while a[i] <= b[i - 1]:
            a[i] = a[i] + a[i + 1]
    
    b.pop(0)
    a.pop(0)
    
    if k == n:
        return "YES", a[:n]
    
    a[n - 1] = a[0] + b[n - 1]
    while a[n - 1] <= b[n - 2]:
        a[n - 1] = a[n - 1] + a[0]
    
    i = n - 2
    while a[i] is None:
        a[i] = b[i] + a[i + 1]
        while a[i] <= b[i - 1]:
            a[i] = a[i] + a[i + 1]
        i -= 1
    
    if k <= n - 2 and a[k] <= a[k + 1]:
        a[k] = a[k] + a[k + 1]
    
    if k == n - 1 and a[k] <= a[0]:
        a[k] = a[k] + a[0]
    
    return "YES", a[:n]