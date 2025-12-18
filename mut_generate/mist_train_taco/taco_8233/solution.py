"""
QUESTION:
Let's define $f(x)$ for a positive integer $x$ as the length of the base-10 representation of $x$ without leading zeros. I like to call it a digital logarithm. Similar to a digital root, if you are familiar with that.

You are given two arrays $a$ and $b$, each containing $n$ positive integers. In one operation, you do the following:

pick some integer $i$ from $1$ to $n$;

assign either $f(a_i)$ to $a_i$ or $f(b_i)$ to $b_i$.

Two arrays are considered similar to each other if you can rearrange the elements in both of them, so that they are equal (e. g. $a_i = b_i$ for all $i$ from $1$ to $n$).

What's the smallest number of operations required to make $a$ and $b$ similar to each other?


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of testcases.

The first line of the testcase contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of elements in each of the arrays.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i < 10^9$).

The third line contains $n$ integers $b_1, b_2, \dots, b_n$ ($1 \le b_j < 10^9$).

The sum of $n$ over all testcases doesn't exceed $2 \cdot 10^5$.


-----Output-----

For each testcase, print the smallest number of operations required to make $a$ and $b$ similar to each other.


-----Examples-----

Input
4
1
1
1000
4
1 2 3 4
3 1 4 2
3
2 9 3
1 100 9
10
75019 709259 5 611271314 9024533 81871864 9 3 6 4865
9503 2 371245467 6 7 37376159 8 364036498 52295554 169
Output
2
0
2
18


-----Note-----

In the first testcase, you can apply the digital logarithm to $b_1$ twice.

In the second testcase, the arrays are already similar to each other.

In the third testcase, you can first apply the digital logarithm to $a_1$, then to $b_2$.
"""

def min_operations_to_make_similar(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a, b = case
        d1_digits = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        d2_digits = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        d1 = {}
        d2 = {}
        out = 0
        
        for x in a:
            if x == 1:
                continue
            if x not in d1:
                d1[x] = 1
            else:
                d1[x] += 1
        
        for x in b:
            if x == 1:
                continue
            if x in d1:
                d1[x] -= 1
                if d1[x] == 0:
                    del d1[x]
            elif x not in d2:
                d2[x] = 1
            else:
                d2[x] += 1
        
        for (x, y) in d1.items():
            k = len(str(x))
            if k == 1:
                d1_digits[x] += y
            else:
                d1_digits[k] += y
                out += y
        
        for (x, y) in d2.items():
            k = len(str(x))
            if k == 1:
                d2_digits[x] += y
            else:
                d2_digits[k] += y
                out += y
        
        for (x, y) in d1_digits.items():
            m = min(y, d2_digits[x])
            out += y - m + (d2_digits[x] - m)
        
        results.append(out)
    
    return results