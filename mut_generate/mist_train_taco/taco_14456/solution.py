"""
QUESTION:
Aayush has recently started teaching Latin Dance. Today, he will be teaching Salsa. For this, he needs to divide the people attending his dance class into pairs. Usually in Salsa, the dance pairs consist of one girl and one boy. But Aayush doesn't find this convention very interesting. He is rather more concerned about the IQ of people who are members of the same pair. Precisely, if the sums of digits of the IQ score of the two people forming a pair are co-prime, then the pair will be $\text{awkward}$ according to Aayush. For example IQ scores 12 (1+2=3) and 22 (2+2=4) form an awkward pair.

The IQ scores of all the people attending the Salsa class are pairwise distinct. The lowest IQ is $\text{L}$ and the largest IQ is $\text{R}$. Moreover, there are exactly $\text{R-L+1}$ people attending the Salsa class. Aayush wants to know the number of ways in which an awkward pair can be formed modulo $10^{9}+7$. Two ways are different if at least one of the members in the pairs formed is different.

------ Input ------
The first line contains a single interger $\text{T}$ - the number of testcases.

Each of the following $\text{T}$ lines contains two space separated integers $\text{L}$ and $\text{R}$, as described in the problem.

------ Output ------
For every test case, print an integer answer modulo $10^{9}+7$.

------ Constraints  ------
$1 ≤ \text{T} ≤ 10$

$1 ≤ \text{L, R} ≤ 10^{18}$

------ Sample Input ------
	2
	5 8
	7 10

------ Sample Output ------
	5
	6
"""

def onedsum(a):
    ds = 0
    while a > 9:
        (a, u) = divmod(a, 10)
        ds += u
    return ds + a

def rangetodsum(lo, hi):
    (lod, lom) = divmod(lo, 10)
    (hid, him) = divmod(hi, 10)
    if lod == hid:
        dlo = onedsum(lod)
        dsum = {dlo + i: 1 for i in range(lom, him + 1)}
    else:
        dlo = onedsum(lod)
        dsum = {dlo + i: 1 for i in range(lom, 10)}
        dhi = onedsum(hid)
        for h in range(dhi, dhi + him + 1):
            if h in dsum:
                dsum[h] += 1
            else:
                dsum[h] = 1
        lod += 1
        hid -= 1
        if lod <= hid:
            rsum = rangetodsum(lod, hid)
            for r in rsum:
                for u in range(10):
                    k = r + u
                    if k in dsum:
                        dsum[k] += rsum[r]
                    else:
                        dsum[k] = rsum[r]
    return dsum

def count_awkward_pairs(L, R):
    mdl = 1000000007
    dsum = rangetodsum(L, R)
    dlst = list(dsum.items())
    awk = 0
    if 1 in dsum:
        awk = dsum[1] * (dsum[1] - 1) // 2
    for ix1 in range(len(dlst) - 1):
        a = dlst[ix1]
        for ix2 in range(ix1 + 1, len(dlst)):
            b = dlst[ix2]
            (f, g) = (a[0], b[0])
            while f > 0:
                (g, f) = (f, g % f)
            if g == 1:
                awk += a[1] * b[1]
                awk %= mdl
    return awk