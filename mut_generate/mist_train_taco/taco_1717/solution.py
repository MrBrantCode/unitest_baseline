"""
QUESTION:
Once upon a time in the thicket of the mushroom forest lived mushroom gnomes. They were famous among their neighbors for their magic mushrooms. Their magic nature made it possible that between every two neighboring mushrooms every minute grew another mushroom with the weight equal to the sum of weights of two neighboring ones. 

The mushroom gnomes loved it when everything was in order, that's why they always planted the mushrooms in one line in the order of their weights' increasing. Well... The gnomes planted the mushrooms and went to eat. After x minutes they returned and saw that new mushrooms had grown up, so that the increasing order had been violated. The gnomes replanted all the mushrooms in the correct order, that is, they sorted the mushrooms in the order of the weights' increasing. And went to eat again (those gnomes were quite big eaters). What total weights modulo p will the mushrooms have in another y minutes?

Input

The first line contains four integers n, x, y, p (1 ≤ n ≤ 106, 0 ≤ x, y ≤ 1018, x + y > 0, 2 ≤ p ≤ 109) which represent the number of mushrooms, the number of minutes after the first replanting, the number of minutes after the second replanting and the module. The next line contains n integers ai which represent the mushrooms' weight in the non-decreasing order (0 ≤ ai ≤ 109).

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d).

Output

The answer should contain a single number which is the total weights of the mushrooms modulo p in the end after x + y minutes.

Examples

Input

2 1 0 657276545
1 2


Output

6


Input

2 1 1 888450282
1 2


Output

14


Input

4 5 0 10000
1 2 3 4


Output

1825
"""

def calculate_mushroom_weights(n, x, y, p, weights):
    def mod(x):
        return (x % p + p) % p

    def matmul(a, b):
        n = len(a)
        c = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % p
        return c

    def matpow(b, p):
        n = len(b)
        res = [[0 if x != y else 1 for x in range(n)] for y in range(n)]
        while p:
            if p & 1:
                res = matmul(res, b)
            b = matmul(b, b)
            p >>= 1
        return res

    weights = sorted(weights)
    if n == 1:
        return weights[0]

    b = matpow([[1, -1], [0, 3]], x)
    sum0 = matmul([[weights[0] + weights[-1], sum(weights)], [0, 0]], b)[0][1]
    b = matpow([[0, 1], [1, 1]], x)
    maxa = matmul([[weights[-2], weights[-1]], [0, 0]], b)[0][1]
    b = matpow([[1, -1], [0, 3]], y)
    sum1 = matmul([[weights[0] + maxa, sum0], [0, 0]], b)[0][1]

    return mod(sum1)