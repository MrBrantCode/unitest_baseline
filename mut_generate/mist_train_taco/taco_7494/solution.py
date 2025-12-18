"""
QUESTION:
Snuke has decided to play a game, where the player runs a railway company.
There are M+1 stations on Snuke Line, numbered 0 through M.
A train on Snuke Line stops at station 0 and every d-th station thereafter, where d is a predetermined constant for each train.
For example, if d = 3, the train stops at station 0, 3, 6, 9, and so forth.
There are N kinds of souvenirs sold in areas around Snuke Line. The i-th kind of souvenirs can be purchased when the train stops at one of the following stations: stations l_i, l_i+1, l_i+2, ..., r_i.
There are M values of d, the interval between two stops, for trains on Snuke Line: 1, 2, 3, ..., M.
For each of these M values, find the number of the kinds of souvenirs that can be purchased if one takes a train with that value of d at station 0.
Here, assume that it is not allowed to change trains.

-----Constraints-----
 - 1 ≦ N ≦ 3 × 10^{5}
 - 1 ≦ M ≦ 10^{5}
 - 1 ≦ l_i ≦ r_i ≦ M

-----Input-----
The input is given from Standard Input in the following format:
N M
l_1 r_1
:
l_{N} r_{N}

-----Output-----
Print the answer in M lines. The i-th line should contain the maximum number of the kinds of souvenirs that can be purchased if one takes a train stopping every i-th station.

-----Sample Input-----
3 3
1 2
2 3
3 3

-----Sample Output-----
3
2
2

 - If one takes a train stopping every station, three kinds of souvenirs can be purchased: kind 1, 2 and 3.
 - If one takes a train stopping every second station, two kinds of souvenirs can be purchased: kind 1 and 2.
 - If one takes a train stopping every third station, two kinds of souvenirs can be purchased: kind 2 and 3.
"""

def count_souvenirs_for_trains(N, M, souvenirs):
    class BitSum:
        def __init__(self, n):
            self.n = n + 3
            self.table = [0] * (self.n + 1)

        def add(self, i, x):
            i += 1
            while i <= self.n:
                self.table[i] += x
                i += i & -i

        def sum(self, i):
            i += 1
            res = 0
            while i > 0:
                res += self.table[i]
                i -= i & -i
            return res

    dlr = []
    for l, r in souvenirs:
        dlr.append((r - l + 1, l, r + 1))
    dlr.sort()
    
    bit = BitSum(M + 1)
    i = 0
    result = []
    
    for k in range(1, M + 1):
        while i < N and dlr[i][0] <= k:
            d, l, r = dlr[i]
            bit.add(l, 1)
            bit.add(r, -1)
            i += 1
        result.append(N - i + sum((bit.sum(a) for a in range(k, M + 1, k))))
    
    return result