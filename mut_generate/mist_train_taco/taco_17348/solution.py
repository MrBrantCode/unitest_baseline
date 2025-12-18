"""
QUESTION:
Witua is a little student from the University of Lviv. He enjoys studying math. Witua knows a lot of famous mathematicians like Eratosthenes, Pythagoras, Fermat, Diophantus, Furko, Gauss and so on. However, his favorite one is Euler. The only thing Witua likes more than Euler is Euler’s totient function φ. He is exploring the nature of this function. One of the steps of his work is finding φ(i)/i for all 2≤i≤N. He doesn’t need to know every such value, but Witua wonders for what value i, is φ(i)/i the maximum he can get? Help little student to find such i that φ(i)/i is maximum among all the  2≤i≤N.

-----Input-----
The first line contains single integer T - the number of test cases. Each of the next T lines contains a single integer N. 

-----Output-----
For every test case output i such that φ(i)/i is maximum among all i (2≤i≤N) in a separate line.

-----Constrains-----
T (1≤T≤500 )

N(2≤N≤10^18)


-----Example-----
Input:
3
2
3
4

Output:
2
3
3

Explanationφ(2)/2=1/2
φ(3)/3=2/3
φ(4)/4=2/4
"""

def bigmod(x, n, mod):
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * x % mod
        n >>= 1
        x = x * x % mod
    return ans

def check_composite(n, a, d, s):
    x = bigmod(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for r in range(s - 1):
        x = x * x % n
        if x == 1:
            return True
        if x == n - 1:
            return False
    return True

def MillerRabin(n, iter=1):
    if n < 2:
        return False
    r = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        r += 1
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in primes:
        if n == a:
            return True
        elif n % a == 0:
            return False
        if check_composite(n, a, d, r) == True:
            return False
    return True

def find_max_phi_ratio_index(T, N_list):
    results = []
    for n in N_list:
        if n == 2:
            results.append(2)
            continue
        if n % 2 == 0:
            n -= 1
        while not MillerRabin(n):
            n -= 2
        results.append(n)
    return results