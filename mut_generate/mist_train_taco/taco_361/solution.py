"""
QUESTION:
Let a_1, …, a_n be an array of n positive integers. In one operation, you can choose an index i such that a_i = i, and remove a_i from the array (after the removal, the remaining parts are concatenated).

The weight of a is defined as the maximum number of elements you can remove.

You must answer q independent queries (x, y): after replacing the x first elements of a and the y last elements of a by n+1 (making them impossible to remove), what would be the weight of a?

Input

The first line contains two integers n and q (1 ≤ n, q ≤ 3 ⋅ 10^5) — the length of the array and the number of queries.

The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) — elements of the array.

The i-th of the next q lines contains two integers x and y (x, y ≥ 0 and x+y < n).

Output

Print q lines, i-th line should contain a single integer — the answer to the i-th query.

Examples

Input


13 5
2 2 3 9 5 4 6 5 7 8 3 11 13
3 1
0 0
2 4
5 0
0 12


Output


5
11
6
1
0


Input


5 2
1 4 1 2 4
0 0
1 0


Output


2
0

Note

Explanation of the first query:

After making first x = 3 and last y = 1 elements impossible to remove, a becomes [×, ×, ×, 9, 5, 4, 6, 5, 7, 8, 3, 11, ×] (we represent 14 as × for clarity).

Here is a strategy that removes 5 elements (the element removed is colored in red):

  * [×, ×, ×, 9, \color{red}{5}, 4, 6, 5, 7, 8, 3, 11, ×] 
  * [×, ×, ×, 9, 4, 6, 5, 7, 8, 3, \color{red}{11}, ×] 
  * [×, ×, ×, 9, 4, \color{red}{6}, 5, 7, 8, 3, ×] 
  * [×, ×, ×, 9, 4, 5, 7, \color{red}{8}, 3, ×] 
  * [×, ×, ×, 9, 4, 5, \color{red}{7}, 3, ×] 
  * [×, ×, ×, 9, 4, 5, 3, ×] (final state) 



It is impossible to remove more than 5 elements, hence the weight is 5.
"""

def calculate_max_removals(n, q, a, queries):
    class Fenwick:
        def __init__(self, size):
            self.size = size
            self.tree = [0] * (size + 1)

        def add(self, idx, val):
            idx = int(idx)
            while idx <= self.size:
                self.tree[idx] += val
                idx += idx & -idx

        def sum(self, idx):
            ret = 0
            idx = int(idx)
            while idx > 0:
                ret += self.tree[idx]
                idx -= idx & -idx
            return ret

    # Adjust the array a to match the problem's requirement
    a = [a[i] - (i + 1) for i in range(n)]
    
    # Prepare the queries
    query = [[] for _ in range(n + 1)]
    for i in range(q):
        (x, y) = queries[i]
        (l, r) = (x, n - y - 1)
        query[r].append((l, i))
    
    # Initialize the Fenwick tree
    ft = Fenwick(n + 1)
    ans = [0 for _ in range(q + 3)]
    
    # Process each element in the array
    for r in range(n):
        ob = a[r]
        if ob <= 0:
            if ft.sum(1) >= -ob:
                (low, high) = (0, r)
                while low + 1 < high:
                    mid = low + high >> 1
                    if ft.sum(mid + 1) >= -ob:
                        low = mid
                    else:
                        high = mid
                idx = high if ft.sum(high + 1) >= -ob else low
                ft.add(1, 1)
                ft.add(idx + 2, -1)
        
        # Process each query for the current index
        for qr in query[r]:
            ans[qr[1]] = ft.sum(qr[0] + 1)
    
    # Return the results for all queries
    return ans[:q]