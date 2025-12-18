"""
QUESTION:
Vasya has got an array consisting of $n$ integers, and two integers $k$ and $len$ in addition. All numbers in the array are either between $1$ and $k$ (inclusive), or equal to $-1$. The array is good if there is no segment of $len$ consecutive equal numbers.

Vasya will replace each $-1$ with some number from $1$ to $k$ (inclusive) in such a way that the resulting array is good. Tell him the number of ways to do this replacement. Since the answer may be large, print it modulo $998244353$.


-----Input-----

The first line contains three integers $n, k$ and $len$ ($1 \le n \le 10^5, 1 \le k \le 100, 1 \le len \le n$).

The second line contains $n$ numbers — the array. Each number is either $-1$ or between $1$ and $k$ (inclusive).


-----Output-----

Print one integer — the number of ways to replace each $-1$ with some number from $1$ to $k$ (inclusive) so the array is good. The answer may be large, so print it modulo $998244353$.


-----Examples-----
Input
5 2 3
1 -1 1 -1 2

Output
2

Input
6 3 2
1 1 -1 -1 -1 -1

Output
0

Input
10 42 7
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1

Output
645711643



-----Note-----

Possible answers in the first test:   $[1, 2, 1, 1, 2]$;  $[1, 2, 1, 2, 2]$. 

There is no way to make the array good in the second test, since first two elements are equal.

There are too many answers in the third test, so we won't describe any of them.
"""

def count_good_arrays(n, k, leng, array):
    if leng == 1:
        return 0
    
    mod = 998244353
    array.insert(0, 0)
    
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    sumdp = [0 for _ in range(n + 1)]
    sumdp[0] = 1
    count = [0 for _ in range(k + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if array[i] == -1 or array[i] == j:
                dp[i][j] = sumdp[i - 1]
                count[j] += 1
                if count[j] >= leng:
                    dp[i][j] -= sumdp[i - leng] - dp[i - leng][j]
                dp[i][j] %= mod
                sumdp[i] += dp[i][j]
                sumdp[i] %= mod
            else:
                count[j] = 0
    
    return sumdp[n]