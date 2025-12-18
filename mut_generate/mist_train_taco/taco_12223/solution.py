"""
QUESTION:
Problem

There are $ N $ Amidakuji with 3 vertical lines.
No matter which line you start from, the Amidakuji that ends at the starting line is considered a good Amidakuji.
You can select one or more Amidakuji and connect them vertically in any order.
Output "yes" if you can make a good Amidakuji, otherwise output "no".

There are $ w_i $ horizontal lines in the $ i $ th Amidakuji.
$ a_ {i, j} $ indicates whether the $ j $ th horizontal bar from the top of Amidakuji $ i $ extends from the central vertical line to the left or right.
If $ a_ {i, j} $ is 0, it means that it extends to the left, and if it is 1, it means that it extends to the right.

Constraints

The input satisfies the following conditions.

* $ 1 \ le N \ le 50 $
* $ 0 \ le w_i \ le 100 $
* $ a_ {i, j} $ is 0 or 1

Input

The input is given in the following format.


$ N $
$ w_1 $ $ a_ {1,1} $ $ a_ {1,2} $ ... $ a_ {1, w_1} $
$ w_2 $ $ a_ {2,1} $ $ a_ {2,2} $ ... $ a_ {2, w_2} $
...
$ w_N $ $ a_ {N, 1} $ $ a_ {N, 2} $ ... $ a_ {N, w_N} $


All inputs are given as integers.
$ N $ is given on the first line.
$ W_i $ and $ w_i $ $ a_ {i, j} $ are given on the following $ N $ line, separated by blanks.

Output

If you can make a good Amidakuji, it outputs "yes", otherwise it outputs "no".

Examples

Input

3
2 0 0
1 1
5 1 0 0 1 0


Output

yes


Input

2
1 1
1 0


Output

no
"""

def can_make_good_amidakuji(N, w, a):
    def amida(line):
        res = [0, 1, 2]
        for i in line:
            if i:
                (res[1], res[2]) = (res[2], res[1])
            else:
                (res[0], res[1]) = (res[1], res[0])
        return res

    def func(x, line, flag):
        if line == [0, 1, 2] and flag:
            return True
        for i in range(27):
            if x[i] == 0:
                continue
            swaps = tolist(i)
            x[i] -= 1
            res = func(x, [line[swaps[0]], line[swaps[1]], line[swaps[2]]], True)
            x[i] += 1
            if res:
                return True
        return False

    toint = lambda x: x[0] * 9 + x[1] * 3 + x[2]
    tolist = lambda x: [x // 9, x % 9 // 3, x % 3]

    if N >= 7:
        return 'yes'

    amidas = [amida(a[i]) for i in range(N)]
    aa = [0 for _ in range(27)]
    for i in amidas:
        aa[toint(i)] += 1

    flag = False
    for i in range(27):
        if aa[i] == 0:
            continue
        line = [0, 1, 2]
        for j in range(aa[i]):
            swaps = tolist(i)
            line = [line[swaps[0]], line[swaps[1]], line[swaps[2]]]
            if line == [0, 1, 2]:
                flag = True
                break
    if flag:
        return 'yes'

    if func(aa, [0, 1, 2], False):
        return 'yes'

    return 'no'