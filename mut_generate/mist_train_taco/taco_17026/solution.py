"""
QUESTION:
Given is an integer N. Find the minimum possible positive integer k such that (1+2+\cdots+k) is a multiple of N. It can be proved that such a positive integer k always exists.

Constraints

* 1 \leq N \leq 10^{15}
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N


Output

Print the answer in a line.

Examples

Input

11


Output

10


Input

20200920


Output

1100144
"""

def find_min_k_for_sum_multiple(N):
    if N == 1:
        return 1
    
    n_copy = N
    if N % 2 == 0:
        ans = 2 * N - 1
        N *= 2
    else:
        ans = N - 1
    
    factors = []
    for p in range(2, N):
        if p * p > N:
            if N > 1:
                factors.append(N)
            break
        if N % p == 0:
            cnt = 0
            while N % p == 0:
                cnt += 1
                N //= p
            factors.append(p ** cnt)
    
    from itertools import product
    
    for tf in product([True, False], repeat=len(factors)):
        (a, b) = (1, 1)
        for i in range(len(factors)):
            if tf[i]:
                a *= factors[i]
            else:
                b *= factors[i]
        if a == 1 or b == 1:
            continue
        if a < b:
            (a, b) = (b, a)
        l = []
        quo = []
        while a % b > 1:
            l.append(a)
            a = b
            quo.append(0)
            (quo[-1], b) = divmod(l[-1], b)
        (x, y) = (1, a // b)
        flag = True
        while l:
            if flag:
                x += y * quo.pop()
                b = l.pop()
            else:
                y += x * quo.pop()
                a = l.pop()
            flag = not flag
        if ans > b * y:
            ans = b * y
    
    return ans