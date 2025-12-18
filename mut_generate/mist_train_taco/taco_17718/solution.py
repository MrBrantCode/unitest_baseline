"""
QUESTION:
In Republic of AtCoder, Snuke Chameleons (Family: Chamaeleonidae, Genus: Bartaberia) are very popular pets. Ringo keeps N Snuke Chameleons in a cage.

A Snuke Chameleon that has not eaten anything is blue. It changes its color according to the following rules:

* A Snuke Chameleon that is blue will change its color to red when the number of red balls it has eaten becomes strictly larger than the number of blue balls it has eaten.
* A Snuke Chameleon that is red will change its color to blue when the number of blue balls it has eaten becomes strictly larger than the number of red balls it has eaten.



Initially, every Snuke Chameleon had not eaten anything. Ringo fed them by repeating the following process K times:

* Grab either a red ball or a blue ball.
* Throw that ball into the cage. Then, one of the chameleons eats it.



After Ringo threw in K balls, all the chameleons were red. We are interested in the possible ways Ringo could have thrown in K balls. How many such ways are there? Find the count modulo 998244353. Here, two ways to throw in balls are considered different when there exists i such that the color of the ball that are thrown in the i-th throw is different.

Constraints

* 1 \leq N,K \leq 5 \times 10^5
* N and K are integers.

Input

Input is given from Standard Input in the following format:


N K


Output

Print the possible ways Ringo could have thrown in K balls, modulo 998244353.

Examples

Input

2 4


Output

7


Input

3 7


Output

57


Input

8 3


Output

0


Input

8 10


Output

46


Input

123456 234567


Output

857617983
"""

def count_ball_throwing_ways(n, k):
    MOD = 998244353
    
    if n > k:
        return 0
    
    if n == 1:
        return pow(2, k - 1, MOD)
    
    (pf, kf) = (1, 1)
    for m in range(2, k + 1):
        pf = kf
        kf *= m
        kf %= MOD
    
    inv = pow(kf, MOD - 2, MOD)
    invs = [1] * (k + 1)
    invs[k] = inv
    
    for m in range(k, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    
    ans = 0
    
    if k & 1 == 0:
        r = k >> 1
        s = k - n + 1
        ans = pf * (invs[r] * invs[r - 1] - invs[s] * invs[k - s - 1]) % MOD
    
    for r in range(k // 2 + 1, k + 1):
        if r * 2 >= n + k:
            ans += kf * invs[r] * invs[k - r]
        else:
            s = r * 2 - n + 1
            ans += kf * (invs[r] * invs[k - r] - invs[s] * invs[k - s])
        ans %= MOD
    
    return ans