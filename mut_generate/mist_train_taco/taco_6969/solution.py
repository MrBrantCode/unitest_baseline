"""
QUESTION:
In Takahashi's mind, there is always an integer sequence of length 2 \times 10^9 + 1: A = (A_{-10^9}, A_{-10^9 + 1}, ..., A_{10^9 - 1}, A_{10^9}) and an integer P.

Initially, all the elements in the sequence A in Takahashi's mind are 0, and the value of the integer P is 0.

When Takahashi eats symbols `+`, `-`, `>` and `<`, the sequence A and the integer P will change as follows:

* When he eats `+`, the value of A_P increases by 1;
* When he eats `-`, the value of A_P decreases by 1;
* When he eats `>`, the value of P increases by 1;
* When he eats `<`, the value of P decreases by 1.



Takahashi has a string S of length N. Each character in S is one of the symbols `+`, `-`, `>` and `<`. He chose a pair of integers (i, j) such that 1 \leq i \leq j \leq N and ate the symbols that are the i-th, (i+1)-th, ..., j-th characters in S, in this order. We heard that, after he finished eating, the sequence A became the same as if he had eaten all the symbols in S from first to last. How many such possible pairs (i, j) are there?

Constraints

* 1 \leq N \leq 250000
* |S| = N
* Each character in S is `+`, `-`, `>` or `<`.

Input

Input is given from Standard Input in the following format:


N
S


Output

Print the answer.

Examples

Input

5
+>+<-


Output

3


Input

5
+>+-<


Output

5


Input

48
-+><<><><><>>>+-<<>->>><<><<-+<>><+<<>+><-+->><<


Output

475
"""

from collections import defaultdict

def count_valid_subsequences(n, s, xs, m):
    ans = [10 ** 9] * (n + 1)
    for x in xs:
        p = 0
        h = 0
        y = 1
        r = pow(x, m - 2, m)
        pos = [0] * (n + 1)
        hashes = [0] * (n + 1)
        for (i, c) in enumerate(s, start=1):
            if c == '>':
                p += 1
                y = y * x % m
            elif c == '<':
                p -= 1
                y = y * r % m
            elif c == '+':
                h = (h + y) % m
            else:
                h = (h - y) % m
            pos[i] = p
            hashes[i] = h
        pow_x = [1]
        for _ in range(max(pos)):
            pow_x.append(pow_x[-1] * x % m)
        mp = min(pos)
        if mp < 0:
            pow_x.append(pow(r, -mp, m))
            for _ in range(-mp - 1):
                pow_x.append(pow_x[-1] * x % m)
        ideal = hashes[-1]
        required = defaultdict(lambda : 0)
        for (i, (p, h)) in enumerate(zip(pos, hashes)):
            ans[i] = min(ans[i], required[h])
            req = (ideal * pow_x[p] + h) % m
            required[req] += 1
    return sum(ans)