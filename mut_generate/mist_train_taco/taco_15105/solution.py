"""
QUESTION:
A positive integer is magical if it is divisible by either A or B.
Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.
 



Example 1:
Input: N = 1, A = 2, B = 3
Output: 2


Example 2:
Input: N = 4, A = 2, B = 3
Output: 6


Example 3:
Input: N = 5, A = 2, B = 4
Output: 10


Example 4:
Input: N = 3, A = 6, B = 4
Output: 8

 
Note:

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000
"""

def nth_magical_number(N: int, A: int, B: int) -> int:
    const = 10 ** 9 + 7
    
    def NOD(a, b):
        if a == b:
            return a
        c = max(a, b)
        d = a + b - c
        c = c % d
        c = c if c > 0 else d
        return NOD(c, d)
    
    nod = NOD(A, B)
    nok = int(A * B / nod)
    (C, D) = (min(A, B), max(A, B))
    k_C = nok // C
    k_D = nok // D
    k = k_C + k_D - 1
    div = N // k
    mod = N - div * k
    k_C_cur = mod * k_C // k
    k_D_cur = mod - k_C_cur
    
    while True:
        C_num = k_C_cur * C
        D_num = k_D_cur * D
        if -C < C_num - D_num < D:
            return (div * nok + max(C_num, D_num)) % const
        elif C_num - D_num <= -C:
            k_D_cur -= 1
            k_C_cur += 1
        else:
            k_D_cur += 1
            k_C_cur -= 1