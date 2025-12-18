"""
QUESTION:
Mahmoud has an array a consisting of n integers. He asked Ehab to find another array b of the same length such that:

  b is lexicographically greater than or equal to a.  b_{i} ≥ 2.  b is pairwise coprime: for every 1 ≤ i < j ≤ n, b_{i} and b_{j} are coprime, i. e. GCD(b_{i}, b_{j}) = 1, where GCD(w, z) is the greatest common divisor of w and z. 

Ehab wants to choose a special array so he wants the lexicographically minimal array between all the variants. Can you find it?

An array x is lexicographically greater than an array y if there exists an index i such than x_{i} > y_{i} and x_{j} = y_{j} for all 1 ≤ j < i. An array x is equal to an array y if x_{i} = y_{i} for all 1 ≤ i ≤ n.


-----Input-----

The first line contains an integer n (1 ≤ n ≤ 10^5), the number of elements in a and b.

The second line contains n integers a_1, a_2, ..., a_{n} (2 ≤ a_{i} ≤ 10^5), the elements of a.


-----Output-----

Output n space-separated integers, the i-th of them representing b_{i}.


-----Examples-----
Input
5
2 3 5 4 13

Output
2 3 5 7 11 
Input
3
10 3 7

Output
10 3 7 


-----Note-----

Note that in the second sample, the array is already pairwise coprime so we printed it.
"""

def find_lexicographically_minimal_coprime_array(n, a):
    MAX_NUM = 2000000
    prime_str = '2      3      5      7     11     13     17     19     23     29 ' + '31     37     41     43     47     53     59     61     67     71 ' + '73     79     83     89     97    101    103    107    109    113 ' + '127    131    137    139    149    151    157    163    167    173 ' + '179    181    191    193    197    199    211    223    227    229 ' + '233    239    241    251    257    263    269    271    277    281 ' + '283    293    307    311    313    317 '
    prime_list = [int(p) for p in prime_str.split()]
    used = [False] * MAX_NUM

    def record(x):
        t = []
        for p in prime_list:
            if x % p == 0:
                while x % p == 0:
                    x = x // p
                t.append(p)
                if x == 1:
                    break
        if x != 1:
            t.append(x)
        for ti in t:
            for i in range(ti, MAX_NUM, ti):
                used[i] = True

    b = []
    for ai in a:
        if not used[ai]:
            b.append(ai)
            record(ai)
        else:
            temp = ai + 1
            while used[temp]:
                temp += 1
            b.append(temp)
            record(temp)
            break

    temp = 2
    while len(b) < len(a):
        while used[temp]:
            temp += 1
        b.append(temp)
        record(temp)

    return b