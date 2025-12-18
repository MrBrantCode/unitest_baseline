"""
QUESTION:
Being stuck at home, Ray became extremely bored. To pass time, he asks Lord Omkar to use his time bending power: Infinity Clock! However, Lord Omkar will only listen to mortals who can solve the following problem:

You are given an array $a$ of $n$ integers. You are also given an integer $k$. Lord Omkar wants you to do $k$ operations with this array.

Define one operation as the following:   Set $d$ to be the maximum value of your array.  For every $i$ from $1$ to $n$, replace $a_{i}$ with $d-a_{i}$. 

The goal is to predict the contents in the array after $k$ operations. Please help Ray determine what the final sequence will look like!


-----Input-----

Each test contains multiple test cases. The first line contains the number of cases $t$ ($1 \le t \le 100$). Description of the test cases follows.

The first line of each test case contains two integers $n$ and $k$ ($1 \leq n \leq 2 \cdot 10^5, 1 \leq k \leq 10^{18}$) – the length of your array and the number of operations to perform.

The second line of each test case contains $n$ integers $a_{1},a_{2},...,a_{n}$ $(-10^9 \leq a_{i} \leq 10^9)$ – the initial contents of your array.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each case, print the final version of array $a$ after $k$ operations described above.


-----Example-----
Input
3
2 1
-199 192
5 19
5 -1 4 2 0
1 2
69

Output
391 0
0 6 1 3 5
0



-----Note-----

In the first test case the array changes as follows:

Initially, the array is $[-199, 192]$. $d = 192$.

After the operation, the array becomes $[d-(-199), d-192] = [391, 0]$.
"""

def predict_final_array(t, test_cases):
    results = []
    for case in test_cases:
        n, k, a = case
        if k % 2 != 0 or k == 1:
            k = 1
        else:
            k = 2
        d = max(a)
        M = 0
        while k:
            for i in range(n):
                a[i] = d - a[i]
                if a[i] >= M:
                    M = a[i]
            d = M
            k -= 1
        results.append(a)
    return results