"""
QUESTION:
You are given n positive integers a_1, a_2, ..., a_{n}.

For every a_{i} you need to find a positive integer k_{i} such that the decimal notation of 2^{k}_{i} contains the decimal notation of a_{i} as a substring among its last min(100, length(2^{k}_{i})) digits. Here length(m) is the length of the decimal notation of m.

Note that you don't have to minimize k_{i}. The decimal notations in this problem do not contain leading zeros.


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 2 000) — the number of integers a_{i}.

Each of the next n lines contains a positive integer a_{i} (1 ≤ a_{i} < 10^11).


-----Output-----

Print n lines. The i-th of them should contain a positive integer k_{i} such that the last min(100, length(2^{k}_{i})) digits of 2^{k}_{i} contain the decimal notation of a_{i} as a substring. Integers k_{i} must satisfy 1 ≤ k_{i} ≤ 10^50.

It can be shown that the answer always exists under the given constraints. If there are multiple answers, print any of them.


-----Examples-----
Input
2
8
2

Output
3
1

Input
2
3
4857

Output
5
20
"""

def find_k_for_a(a: list) -> list:
    exp = 10
    results = []
    
    for ai in a:
        p10 = 1
        e10 = 0
        while p10 <= ai:
            p10 = p10 * 10
            e10 = e10 + 1
        
        b = 5 ** exp * ai % 2 ** e10
        b = (2 ** e10 - b) % 2 ** e10
        
        if b % 5 == 0:
            b = b + 2 ** e10
        
        ai = ai * 10 ** exp + b * 2 ** exp
        e10 = e10 + exp
        
        ans = -1
        cur = 2 ** (e10 + 5)
        
        for dig in range(1, e10 + 1):
            step = 4 * 5 ** (dig - 2)
            if dig == 1:
                step = 1
            
            b = ai % 10 ** dig
            
            for i in range(5):
                x = pow(2, cur, 10 ** dig)
                if b == x:
                    break
                cur = cur + step
            else:
                break
        else:
            ans = cur
        
        results.append(ans)
    
    return results