"""
QUESTION:
Ashish has an array $a$ of size $n$.

A subsequence of $a$ is defined as a sequence that can be obtained from $a$ by deleting some elements (possibly none), without changing the order of the remaining elements.

Consider a subsequence $s$ of $a$. He defines the cost of $s$ as the minimum between:   The maximum among all elements at odd indices of $s$.  The maximum among all elements at even indices of $s$. 

Note that the index of an element is its index in $s$, rather than its index in $a$. The positions are numbered from $1$. So, the cost of $s$ is equal to $min(max(s_1, s_3, s_5, \ldots), max(s_2, s_4, s_6, \ldots))$.

For example, the cost of $\{7, 5, 6\}$ is $min( max(7, 6), max(5) ) = min(7, 5) = 5$.

Help him find the minimum cost of a subsequence of size $k$.


-----Input-----

The first line contains two integers $n$ and $k$ ($2 \leq k \leq n \leq 2 \cdot 10^5$)  — the size of the array $a$ and the size of the subsequence.

The next line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq 10^9$)  — the elements of the array $a$.


-----Output-----

Output a single integer  — the minimum cost of a subsequence of size $k$.


-----Examples-----
Input
4 2
1 2 3 4

Output
1
Input
4 3
1 2 3 4

Output
2
Input
5 3
5 3 4 2 6

Output
2
Input
6 4
5 3 50 2 4 5

Output
3


-----Note-----

In the first test, consider the subsequence $s$ = $\{1, 3\}$. Here the cost is equal to $min(max(1), max(3)) = 1$.

In the second test, consider the subsequence $s$ = $\{1, 2, 4\}$. Here the cost is equal to $min(max(1, 4), max(2)) = 2$.

In the fourth test, consider the subsequence $s$ = $\{3, 50, 2, 4\}$. Here the cost is equal to $min(max(3, 2), max(50, 4)) = 3$.
"""

def find_min_cost_subsequence(n, k, a):
    def can_form_subsequence(mid_value):
        # Check if we can form a subsequence of size k with the given mid_value as the cost
        odd_count = 0
        even_count = 0
        for i in range(n):
            if even_count < k // 2 and a[i] <= mid_value:
                even_count += 1
            elif odd_count < (k + 1) // 2 and a[i] <= mid_value:
                odd_count += 1
        
        return even_count >= k // 2 and odd_count >= (k + 1) // 2

    # Binary search to find the minimum cost
    low, high = 1, max(a)
    while low < high:
        mid = (low + high) // 2
        if can_form_subsequence(mid):
            high = mid
        else:
            low = mid + 1
    
    return low