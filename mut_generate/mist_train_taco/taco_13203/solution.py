"""
QUESTION:
Simon has an array a_1, a_2, ..., a_{n}, consisting of n positive integers. Today Simon asked you to find a pair of integers l, r (1 ≤ l ≤ r ≤ n), such that the following conditions hold:  there is integer j (l ≤ j ≤ r), such that all integers a_{l}, a_{l} + 1, ..., a_{r} are divisible by a_{j};  value r - l takes the maximum value among all pairs for which condition 1 is true; 

Help Simon, find the required pair of numbers (l, r). If there are multiple required pairs find all of them.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 3·10^5).

The second line contains n space-separated integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^6).


-----Output-----

Print two integers in the first line — the number of required pairs and the maximum value of r - l. On the following line print all l values from optimal pairs in increasing order.


-----Examples-----
Input
5
4 6 9 3 6

Output
1 3
2 

Input
5
1 3 5 7 9

Output
1 4
1 

Input
5
2 3 5 7 11

Output
5 0
1 2 3 4 5 



-----Note-----

In the first sample the pair of numbers is right, as numbers 6, 9, 3 are divisible by 3.

In the second sample all numbers are divisible by number 1.

In the third sample all numbers are prime, so conditions 1 and 2 are true only for pairs of numbers (1, 1), (2, 2), (3, 3), (4, 4), (5, 5).
"""

def find_optimal_pairs(n, array):
    # Extend the array with 1s at the beginning and end to simplify boundary checks
    t = [1] + array + [1]
    p = [True] * (n + 2)
    s = 0
    q = []
    
    for i in range(1, n + 1):
        if p[i]:
            a = b = i
            d = t[i]
            if d == 1:
                s = n - 1
                q = [1]
                break
            while t[a - 1] % d == 0:
                a -= 1
            while t[b + 1] % d == 0:
                b += 1
                p[b] = False
            d = b - a
            if d > s:
                s = d
                q = [a]
            elif d == s:
                q.append(a)
    
    return len(q), s, q