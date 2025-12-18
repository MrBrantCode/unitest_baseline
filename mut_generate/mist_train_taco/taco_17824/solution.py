"""
QUESTION:
Squirrel Liss is interested in sequences. She also has preferences of integers. She thinks n integers a_1, a_2, ..., a_{n} are good.

Now she is interested in good sequences. A sequence x_1, x_2, ..., x_{k} is called good if it satisfies the following three conditions:  The sequence is strictly increasing, i.e. x_{i} < x_{i} + 1 for each i (1 ≤ i ≤ k - 1).  No two adjacent elements are coprime, i.e. gcd(x_{i}, x_{i} + 1) > 1 for each i (1 ≤ i ≤ k - 1) (where gcd(p, q) denotes the greatest common divisor of the integers p and q).  All elements of the sequence are good integers. 

Find the length of the longest good sequence.


-----Input-----

The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 10^5) — the number of good integers. The second line contains a single-space separated list of good integers a_1, a_2, ..., a_{n} in strictly increasing order (1 ≤ a_{i} ≤ 10^5; a_{i} < a_{i} + 1).


-----Output-----

Print a single integer — the length of the longest good sequence.


-----Examples-----
Input
5
2 3 4 6 9

Output
4

Input
9
1 2 3 5 6 7 8 9 10

Output
4



-----Note-----

In the first example, the following sequences are examples of good sequences: [2; 4; 6; 9], [2; 4; 6], [3; 9], [6]. The length of the longest good sequence is 4.
"""

def find_longest_good_sequence_length(good_integers):
    d = {}
    for a in good_integers:
        (z, l) = (0, [])
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313):
            if not a % p:
                l.append(p)
                x = d.get(p, 0)
                if z < x:
                    z = x
                a //= p
                while not a % p:
                    a //= p
                if a == 1:
                    break
        else:
            l.append(a)
            x = d.get(a, 0)
            if z < x:
                z = x
        d.update(dict.fromkeys(l, z + 1))
    return max(d.values())