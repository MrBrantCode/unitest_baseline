"""
QUESTION:
Vitya is studying in the third grade. During the last math lesson all the pupils wrote on arithmetic quiz. Vitya is a clever boy, so he managed to finish all the tasks pretty fast and Oksana Fillipovna gave him a new one, that is much harder.

Let's denote a flip operation of an integer as follows: number is considered in decimal notation and then reverted. If there are any leading zeroes afterwards, they are thrown away. For example, if we flip 123 the result is the integer 321, but flipping 130 we obtain 31, and by flipping 31 we come to 13.

Oksana Fillipovna picked some number a without leading zeroes, and flipped it to get number ar. Then she summed a and ar, and told Vitya the resulting value n. His goal is to find any valid a.

As Oksana Fillipovna picked some small integers as a and ar, Vitya managed to find the answer pretty fast and became interested in finding some general algorithm to deal with this problem. Now, he wants you to write the program that for given n finds any a without leading zeroes, such that a + ar = n or determine that such a doesn't exist.

Input

The first line of the input contains a single integer n (1 ≤ n ≤ 10100 000).

Output

If there is no such positive integer a without leading zeroes that a + ar = n then print 0. Otherwise, print any valid a. If there are many possible answers, you are allowed to pick any.

Examples

Input

4


Output

2


Input

11


Output

10


Input

5


Output

0


Input

33


Output

21

Note

In the first sample 4 = 2 + 2, a = 2 is the only possibility.

In the second sample 11 = 10 + 1, a = 10 — the only valid solution. Note, that a = 01 is incorrect, because a can't have leading zeroes.

It's easy to check that there is no suitable a in the third sample.

In the fourth sample 33 = 30 + 3 = 12 + 21, so there are three possibilities for a: a = 30, a = 12, a = 21. Any of these is considered to be correct answer.
"""

def find_valid_a(n: int) -> str:
    def digits(n):
        rd = []
        while n:
            (n, d) = divmod(n, 10)
            rd.append(d)
        return list(reversed(rd))

    def _ifs(dn, i, j, ci, cj, al, ar):
        while i < j:
            di = dn[i] + 10 * ci
            dj = dn[j] - cj
            for (ci, cj) in ((0, 0), (0, 1), (1, 0), (1, 1)):
                d = di - ci
                if d < 0 or d > 18:
                    continue
                if dj + 10 * cj == d:
                    if d < 10:
                        if d == 0 and (not al):
                            return
                        al.append(d)
                        ar.append(0)
                    else:
                        al.append(9)
                        ar.append(d - 9)
                    break
            else:
                return
            i += 1
            j -= 1
        if i == j:
            d = dn[i] + 10 * ci - cj
            if d < 0 or d % 2:
                return
            al.append(d // 2)
        elif ci != cj:
            return
        return al + list(reversed(ar))

    def inv_fsum(dn):
        if dn[0] == 1:
            return _ifs(dn, 0, len(dn) - 1, 0, 0, [], []) or _ifs(dn, 1, len(dn) - 1, 1, 0, [], []) or [0]
        else:
            return _ifs(dn, 0, len(dn) - 1, 0, 0, [], []) or [0]

    dn = tuple(digits(n))
    result = inv_fsum(dn)
    return ''.join(map(str, result))