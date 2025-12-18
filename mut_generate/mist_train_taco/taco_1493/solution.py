"""
QUESTION:
Little penguin Polo likes permutations. But most of all he likes permutations of integers from 0 to n, inclusive.

For permutation p = p_0, p_1, ..., p_{n}, Polo has defined its beauty — number $(0 \oplus p_{0}) +(1 \oplus p_{1}) + \cdots +(n \oplus p_{n})$.

Expression $x \oplus y$ means applying the operation of bitwise excluding "OR" to numbers x and y. This operation exists in all modern programming languages, for example, in language C++ and Java it is represented as "^" and in Pascal — as "xor".

Help him find among all permutations of integers from 0 to n the permutation with the maximum beauty.


-----Input-----

The single line contains a positive integer n (1 ≤ n ≤ 10^6).


-----Output-----

In the first line print integer m the maximum possible beauty. In the second line print any permutation of integers from 0 to n with the beauty equal to m.

If there are several suitable permutations, you are allowed to print any of them.


-----Examples-----
Input
4

Output
20
0 2 1 4 3
"""

def find_max_beauty_permutation(n):
    n += 1  # Adjust n to include 0 to n
    s = n
    t, r = [], list(range(n))[::-1]
    k = 2 ** 20
    
    while s:
        while k >= 2 * s:
            k //= 2
        t = r[n - s:n + s - k] + t
        s = k - s
    
    max_beauty = n * n - n
    permutation = t
    
    return max_beauty, permutation