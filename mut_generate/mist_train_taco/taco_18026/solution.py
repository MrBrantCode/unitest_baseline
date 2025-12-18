"""
QUESTION:
Phoenix loves beautiful arrays. An array is beautiful if all its subarrays of length $k$ have the same sum. A subarray of an array is any sequence of consecutive elements.

Phoenix currently has an array $a$ of length $n$. He wants to insert some number of integers, possibly zero, into his array such that it becomes beautiful. The inserted integers must be between $1$ and $n$ inclusive. Integers may be inserted anywhere (even before the first or after the last element), and he is not trying to minimize the number of inserted integers.


-----Input-----

The input consists of multiple test cases. The first line contains an integer $t$ ($1 \le t \le 50$) — the number of test cases.

The first line of each test case contains two integers $n$ and $k$ ($1 \le k \le n \le 100$).

The second line of each test case contains $n$ space-separated integers ($1 \le a_i \le n$) — the array that Phoenix currently has. This array may or may not be already beautiful.


-----Output-----

For each test case, if it is impossible to create a beautiful array, print -1. Otherwise, print two lines.

The first line should contain the length of the beautiful array $m$ ($n \le m \le 10^4$). You don't need to minimize $m$.

The second line should contain $m$ space-separated integers ($1 \le b_i \le n$) — a beautiful array that Phoenix can obtain after inserting some, possibly zero, integers into his array $a$. You may print integers that weren't originally in array $a$.

If there are multiple solutions, print any. It's guaranteed that if we can make array $a$ beautiful, we can always make it with resulting length no more than $10^4$.


-----Example-----
Input
4
4 2
1 2 2 1
4 3
1 2 2 1
3 2
1 2 3
4 4
4 3 4 2

Output
5
1 2 1 2 1
4
1 2 2 1
-1
7
4 3 2 1 4 3 2


-----Note-----

In the first test case, we can make array $a$ beautiful by inserting the integer $1$ at index $3$ (in between the two existing $2$s). Now, all subarrays of length $k=2$ have the same sum $3$. There exists many other possible solutions, for example:   $2, 1, 2, 1, 2, 1$  $1, 2, 1, 2, 1, 2$ 

In the second test case, the array is already beautiful: all subarrays of length $k=3$ have the same sum $5$.

In the third test case, it can be shown that we cannot insert numbers to make array $a$ beautiful.

In the fourth test case, the array $b$ shown is beautiful and all subarrays of length $k=4$ have the same sum $10$. There exist other solutions also.
"""

def create_beautiful_array(n, k, a):
    aset = set(a)
    if len(aset) > k:
        return -1
    elif len(aset) == k:
        m = n * k
        beautiful_array = []
        aset = list(aset)
        for i in range(n):
            beautiful_array.extend(aset)
        return m, beautiful_array
    else:
        ns = list(range(1, k + 1))
        q = 0
        while len(aset) != k:
            aset.add(ns[q])
            q += 1
        aset = list(aset)
        m = n * k
        beautiful_array = []
        for i in range(n):
            beautiful_array.extend(aset)
        return m, beautiful_array