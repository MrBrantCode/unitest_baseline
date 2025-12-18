"""
QUESTION:
Professor GukiZ has two arrays of integers, a and b. Professor wants to make the sum of the elements in the array a s_{a} as close as possible to the sum of the elements in the array b s_{b}. So he wants to minimize the value v = |s_{a} - s_{b}|.

In one operation professor can swap some element from the array a and some element from the array b. For example if the array a is [5, 1, 3, 2, 4] and the array b is [3, 3, 2] professor can swap the element 5 from the array a and the element 2 from the array b and get the new array a [2, 1, 3, 2, 4] and the new array b [3, 3, 5].

Professor doesn't want to make more than two swaps. Find the minimal value v and some sequence of no more than two swaps that will lead to the such value v. Professor makes swaps one by one, each new swap he makes with the new arrays a and b.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 2000) — the number of elements in the array a.

The second line contains n integers a_{i} ( - 10^9 ≤ a_{i} ≤ 10^9) — the elements of the array a.

The third line contains integer m (1 ≤ m ≤ 2000) — the number of elements in the array b.

The fourth line contains m integers b_{j} ( - 10^9 ≤ b_{j} ≤ 10^9) — the elements of the array b.


-----Output-----

In the first line print the minimal value v = |s_{a} - s_{b}| that can be got with no more than two swaps.

The second line should contain the number of swaps k (0 ≤ k ≤ 2).

Each of the next k lines should contain two integers x_{p}, y_{p} (1 ≤ x_{p} ≤ n, 1 ≤ y_{p} ≤ m) — the index of the element in the array a and the index of the element in the array b in the p-th swap.

If there are several optimal solutions print any of them. Print the swaps in order the professor did them.


-----Examples-----
Input
5
5 4 3 2 1
4
1 1 1 1

Output
1
2
1 1
4 2

Input
5
1 2 3 4 5
1
15

Output
0
0

Input
5
1 2 3 4 5
4
1 2 3 4

Output
1
1
3 1
"""

from bisect import bisect_left

def minimize_sum_difference(a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    delta = sum_b - sum_a
    ans = abs(delta)
    ans_swap = []
    
    # Try single swaps
    for i in range(len(a)):
        for j in range(len(b)):
            new_sum_a = sum_a - a[i] + b[j]
            new_sum_b = sum_b + a[i] - b[j]
            if abs(new_sum_a - new_sum_b) < ans:
                ans = abs(new_sum_a - new_sum_b)
                ans_swap = [(i + 1, j + 1)]
    
    # Prepare dictionary for double swaps
    d = {}
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            d[b[i] + b[j]] = (i + 1, j + 1)
    
    val = [-10**13, -10**13] + sorted(d.keys()) + [10**13, 10**13]
    
    # Try double swaps
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            ap = a[i] + a[j]
            req = (delta + ap * 2) // 2
            k = bisect_left(val, req)
            for k in range(k - 1, k + 2):
                if abs(delta + ap * 2 - val[k] * 2) < ans:
                    ans = abs(delta + ap * 2 - val[k] * 2)
                    ans_swap = [(i + 1, d[val[k]][0]), (j + 1, d[val[k]][1])]
    
    return ans, len(ans_swap), ans_swap