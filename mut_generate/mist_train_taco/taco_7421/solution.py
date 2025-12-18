"""
QUESTION:
It's another Start[c]up finals, and that means there is pizza to order for the onsite contestants. There are only 2 types of pizza (obviously not, but let's just pretend for the sake of the problem), and all pizzas contain exactly S slices.

It is known that the i-th contestant will eat si slices of pizza, and gain ai happiness for each slice of type 1 pizza they eat, and bi happiness for each slice of type 2 pizza they eat. We can order any number of type 1 and type 2 pizzas, but we want to buy the minimum possible number of pizzas for all of the contestants to be able to eat their required number of slices. Given that restriction, what is the maximum possible total happiness that can be achieved?

Input

The first line of input will contain integers N and S (1 ≤ N ≤ 105, 1 ≤ S ≤ 105), the number of contestants and the number of slices per pizza, respectively. N lines follow.

The i-th such line contains integers si, ai, and bi (1 ≤ si ≤ 105, 1 ≤ ai ≤ 105, 1 ≤ bi ≤ 105), the number of slices the i-th contestant will eat, the happiness they will gain from each type 1 slice they eat, and the happiness they will gain from each type 2 slice they eat, respectively.

Output

Print the maximum total happiness that can be achieved.

Examples

Input

3 12
3 5 7
4 6 7
5 9 5


Output

84


Input

6 10
7 4 7
5 8 8
12 5 8
6 11 6
3 3 7
5 9 6


Output

314

Note

In the first example, you only need to buy one pizza. If you buy a type 1 pizza, the total happiness will be 3·5 + 4·6 + 5·9 = 84, and if you buy a type 2 pizza, the total happiness will be 3·7 + 4·7 + 5·5 = 74.
"""

def calculate_max_happiness(N, S, contestants):
    def cns(ts, s):
        if ts % s == 0:
            return ts
        else:
            return (ts // s + 1) * s

    tsr = sum(si for si, _, _ in contestants)
    da = [[] for _ in range(100005)]
    db = [[] for _ in range(100005)]

    for i, (si, ai, bi) in enumerate(contestants):
        if ai > bi:
            da[ai - bi].append(i)
        else:
            db[bi - ai].append(i)

    tsa = cns(tsr, S)

    def calculate_happiness(da, db):
        a = 0
        c1 = 0
        for i in range(100000, -1, -1):
            for j in da[i]:
                a += contestants[j][0] * contestants[j][1]
                c1 += contestants[j][0]

        c1r = cns(c1, S) - c1
        c2r = tsa - cns(c1, S)

        for i in range(100000, -1, -1):
            for j in db[i]:
                if contestants[j][0] > c2r:
                    a += c2r * contestants[j][2]
                    a += (contestants[j][0] - c2r) * contestants[j][1]
                    c2r = 0
                else:
                    a += contestants[j][0] * contestants[j][2]
                    c2r -= contestants[j][0]

        return a

    a1 = calculate_happiness(da, db)
    a2 = calculate_happiness(db, da)

    return max(a1, a2)