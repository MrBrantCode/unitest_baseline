"""
QUESTION:
Define a function `solve(N)` where `N` is an integer. Given a positive integer `N`, calculate the cumulative sum `S(N)` of all `n <= 2^N` where Eric can secure a win, modulo `1,000,000,007`, in a game where two players take turns inscribing numbers on a blackboard, ensuring the total sum does not surpass `2n`, and Eric wins if the count of `1`s is even. Use dynamic programming to optimize the solution.
"""

def entance(N, p=10**9+7):
    f = [[[[0, 0] for _ in range(2)] for _ in range(70)] for _ in range(70)]
    f[0][0][0][1] = 1
    two = [1]
    for i in range(1, 70):
        two.append(two[-1]*2%p)
    for i in range(N):
        for j in range(i+1):
            for k in range(2):
                for l in range(2):
                    if not f[i][j][k][l]:
                        continue
                    for a in range(2):
                        for b in range(min(a+1, 2)):
                            if j+a > i+1 or k and b < a or l and j+a+b > i+1:
                                continue
                            f[i+1][j+a][a==b][l and j+a+b==i+2] = (f[i+1][j+a][a==b][l and j+a+b==i+2] + f[i][j][k][l])%p
    ans = 0
    for i in range(N):
        for j in range(i+1):
            ans = (ans + two[N-i-1]*f[i][j][0][0])%p
            if i+j&1:
                ans = (ans + two[N-i-1]*f[i][j][0][1])%p
    return ans