"""
QUESTION:
Two's company, three's a crowd!
It's been one year since Chef met his brother. Last year, his younger brother came to visit him during this time of the year. This year, the Chef is planning to go visit his brother. Chef's brother has planned to throw a "Welcome Party" for him. He wants to invite people from his neighbourhood (i.e. from the street where he lives). There are N houses on the street in a single line (not considering the brother's house). He wants the party to be fun and he will not like to invite people who might spoil the mood of the party. If people are invited from three consecutive houses on the street, they might create trouble. As they say, three's a crowd! He doesn't want to ruin the Chef's Welcome Party and so he will not want to send invites to any three consecutive houses. He wants you to tell him how many ways are there for him to go wrong. Note that he can play safe by not inviting anyone to avoid a crowd.

-----Input:-----
First line of the input contains a single integer T, the number of test cases.

Each test case contains a line containing a single integer N described above.

-----Output:-----
For each test case output a single integer denoting the number of ways the brother can go wrong with planning the party.

The answer can get quite large. So output the total number of ways modulo 109+7.

-----Constraints:-----
1<=T<=10000
1<=N<=1015

-----Example:-----Input:
2
3
4

Output:
1
3

Explanation:
Case 1: The only way he can go wrong is by inviting all the houses.
Case 2: First way of getting wrong is by inviting houses (1,2,3). Second way to get wrong is by inviting houses (2,3,4). Third way of going wrong is by inviting all 4 houses i.e. (1,2,3,4).
"""

MOD = 1000000007

def mult(a, b):
    rsp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                rsp[i][j] += a[i][k] * b[k][j]
                rsp[i][j] %= MOD
    return rsp

ident = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
powers = [m]
for _ in range(53):
    p = powers[-1]
    powers.append(mult(p, p))

def pow2(e):
    y = ident
    i = 0
    for p in powers:
        if e & 1 << i:
            y = mult(p, y)
        i += 1
    return y

def calculate_wrong_invitations(T, N):
    results = []
    for n in N:
        if n < 3:
            results.append(0)
            continue
        r = pow(2, n, MOD)
        b = pow2(n - 2)
        r -= 4 * b[0][0] % MOD
        r -= 2 * b[1][0] % MOD
        r -= b[2][0]
        r = (MOD + r) % MOD
        results.append(r)
    return results