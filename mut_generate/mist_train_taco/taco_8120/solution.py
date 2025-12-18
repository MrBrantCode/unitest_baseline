"""
QUESTION:
You are given array a with n integers and m queries. The i-th query is given with three integers l_{i}, r_{i}, x_{i}.

For the i-th query find any position p_{i} (l_{i} ≤ p_{i} ≤ r_{i}) so that a_{p}_{i} ≠ x_{i}.


-----Input-----

The first line contains two integers n, m (1 ≤ n, m ≤ 2·10^5) — the number of elements in a and the number of queries.

The second line contains n integers a_{i} (1 ≤ a_{i} ≤ 10^6) — the elements of the array a.

Each of the next m lines contains three integers l_{i}, r_{i}, x_{i} (1 ≤ l_{i} ≤ r_{i} ≤ n, 1 ≤ x_{i} ≤ 10^6) — the parameters of the i-th query.


-----Output-----

Print m lines. On the i-th line print integer p_{i} — the position of any number not equal to x_{i} in segment [l_{i}, r_{i}] or the value  - 1 if there is no such number.


-----Examples-----
Input
6 4
1 2 1 1 3 5
1 4 1
2 6 2
3 4 1
3 4 2

Output
2
6
-1
4
"""

def find_non_matching_position(a, queries):
    n = len(a)
    p = [n] * n
    stk = []
    
    # Preprocess the array to find the next position where the value changes
    for i in range(n):
        while stk and a[stk[-1]] != a[i]:
            p[stk.pop()] = i
        stk.append(i)
    
    results = []
    
    # Process each query
    for (l, r, x) in queries:
        l -= 1  # Convert to 0-based index
        r -= 1  # Convert to 0-based index
        
        if a[l] != x:
            results.append(l + 1)  # Convert back to 1-based index
        elif p[l] <= r:
            results.append(p[l] + 1)  # Convert back to 1-based index
        else:
            results.append(-1)
    
    return results