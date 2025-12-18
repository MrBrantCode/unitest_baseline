"""
QUESTION:
In "Takahashi-ya", a ramen restaurant, basically they have one menu: "ramen", but N kinds of toppings are also offered. When a customer orders a bowl of ramen, for each kind of topping, he/she can choose whether to put it on top of his/her ramen or not. There is no limit on the number of toppings, and it is allowed to have all kinds of toppings or no topping at all. That is, considering the combination of the toppings, 2^N types of ramen can be ordered.
Akaki entered Takahashi-ya. She is thinking of ordering some bowls of ramen that satisfy both of the following two conditions:
 - Do not order multiple bowls of ramen with the exactly same set of toppings.
 - Each of the N kinds of toppings is on two or more bowls of ramen ordered.
You are given N and a prime number M. Find the number of the sets of bowls of ramen that satisfy these conditions, disregarding order, modulo M. Since she is in extreme hunger, ordering any number of bowls of ramen is fine.

-----Constraints-----
 - 2 \leq N \leq 3000
 - 10^8 \leq M \leq 10^9 + 9
 - N is an integer.
 - M is a prime number.

-----Subscores-----
 - 600 points will be awarded for passing the test set satisfying N ≤ 50.

-----Input-----
Input is given from Standard Input in the following format:
N M

-----Output-----
Print the number of the sets of bowls of ramen that satisfy the conditions, disregarding order, modulo M.

-----Sample Input-----
2 1000000007

-----Sample Output-----
2

Let the two kinds of toppings be A and B. Four types of ramen can be ordered: "no toppings", "with A", "with B" and "with A, B". There are two sets of ramen that satisfy the conditions:
 - The following three ramen: "with A", "with B", "with A, B".
 - Four ramen, one for each type.
"""

def count_valid_ramen_sets(N, M):
    fact = [1] * (N + 1)
    rfact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = r = i * fact[i - 1] % M
        rfact[i] = pow(r, M - 2, M)
    memo = {}

    def f(N, K):
        if (N, K) in memo:
            return memo[N, K]
        if K == 0:
            return N == 0
        elif K == 1 or N == K:
            return 1
        r = memo[N, K] = (f(N - 1, K - 1) + K * f(N - 1, K)) % M
        return r

    S = [1]
    rev2 = pow(2, M - 2, M)
    base = pow(2, N, M)
    ans = 0
    S = [1]
    for K in range(N + 1):
        r = fact[N] * rfact[K] * rfact[N - K] % M
        r = r * pow(2, pow(2, N - K, M - 1), M) % M
        b = 1
        v = 0
        T = [0] * (K + 2)
        for L in range(K):
            T[L + 1] = s = (S[L] + (L + 1) * S[L + 1]) % M
            v += s * b
            b = b * base % M
        v += b
        T[K + 1] = 1
        S = T
        r = r * v % M
        if K % 2:
            ans -= r
        else:
            ans += r
        ans %= M
        base = base * rev2 % M
    return ans