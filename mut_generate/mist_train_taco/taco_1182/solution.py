"""
QUESTION:
Karl is developing a key storage service. Each user has a positive integer key.

Karl knows that storing keys in plain text is bad practice. So, instead of storing a key, he decided to store a fingerprint of a key. However, using some existing fingerprint algorithm looked too boring to him, so he invented his own one.

Karl's fingerprint is calculated by the following process: divide the given integer by 2, then divide the result by 3, then divide the result by 4, and so on, until we get a result that equals zero (we are speaking about integer division each time). The fingerprint is defined as the multiset of the remainders of these divisions. 

For example, this is how Karl's fingerprint algorithm is applied to the key 11: 11 divided by 2 has remainder 1 and result 5, then 5 divided by 3 has remainder 2 and result 1, and 1 divided by 4 has remainder 1 and result 0. Thus, the key 11 produces the sequence of remainders [1, 2, 1] and has the fingerprint multiset \{1, 1, 2\}.

Ksenia wants to prove that Karl's fingerprint algorithm is not very good. For example, she found that both keys 178800 and 123456 produce the fingerprint of \{0, 0, 0, 0, 2, 3, 3, 4\}. Thus, users are at risk of fingerprint collision with some commonly used and easy to guess keys like 123456.

Ksenia wants to make her words more persuasive. She wants to calculate the number of other keys that have the same fingerprint as the keys in the given list of some commonly used keys. Your task is to help her.

Input

The first line contains an integer t (1 ≤ t ≤ 50 000) — the number of commonly used keys to examine. Each of the next t lines contains one integer k_i (1 ≤ k_i ≤ 10^{18}) — the key itself. 

Output

For each of the keys print one integer — the number of other keys that have the same fingerprint. 

Example

Input


3
1
11
123456


Output


0
1
127

Note

The other key with the same fingerprint as 11 is 15. 15 produces a sequence of remainders [1, 1, 2]. So both numbers have the fingerprint multiset \{1, 1, 2\}.
"""

import math as m
import collections

def calculate_fingerprint_collisions(keys):
    def solve(arr, n):
        d = collections.Counter(arr)
        tu = 1
        mau = 1
        a = [0] * 22
        for i in arr:
            a[i] += 1
        for i in range(1, len(a)):
            a[i] += a[i - 1]
        for i in range(2, n + 2):
            tu *= a[i - 1] - i + 2
        for i in d.values():
            mau *= f[i]
        return tu // mau
    
    f = [1]
    for i in range(1, 22):
        f.append(f[-1] * i)
    
    results = []
    
    for n in keys:
        arr = []
        i = 2
        while n:
            arr.append(n % i)
            n //= i
            i += 1
        arr.sort()
        pro = solve(arr, len(arr))
        if 0 in arr:
            arr.pop(0)
            tru = solve(arr, len(arr))
            pro -= tru
        results.append(pro - 1)
    
    return results