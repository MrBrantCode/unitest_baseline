"""
QUESTION:
You are given a permutation p_1, p_2, …, p_n.

In one move you can swap two adjacent values.

You want to perform a minimum number of moves, such that in the end there will exist a subsegment 1,2,…, k, in other words in the end there should be an integer i, 1 ≤ i ≤ n-k+1 such that p_i = 1, p_{i+1} = 2, …, p_{i+k-1}=k.

Let f(k) be the minimum number of moves that you need to make a subsegment with values 1,2,…,k appear in the permutation.

You need to find f(1), f(2), …, f(n).

Input

The first line of input contains one integer n (1 ≤ n ≤ 200 000): the number of elements in the permutation.

The next line of input contains n integers p_1, p_2, …, p_n: given permutation (1 ≤ p_i ≤ n).

Output

Print n integers, the minimum number of moves that you need to make a subsegment with values 1,2,…,k appear in the permutation, for k=1, 2, …, n.

Examples

Input


5
5 4 3 2 1


Output


0 1 3 6 10 


Input


3
1 2 3


Output


0 0 0
"""

def calculate_minimum_moves(n, permutation):
    # Initialize necessary data structures
    pos = [0] * (n + 1)
    pb = [0] * (n + 1)
    ps = [0] * (n + 1)
    
    # Helper functions for Fenwick Tree (Binary Indexed Tree) operations
    def add(bit, i, val):
        while i <= n:
            bit[i] += val
            i += i & -i

    def sum(bit, i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & -i
        return res

    def find(bit, sum_val):
        i, t = 0, 0
        if sum_val == 0:
            return 0
        for k in range(17, -1, -1):
            i += 1 << k
            if i <= n and t + bit[i] < sum_val:
                t += bit[i]
            else:
                i -= 1 << k
        return i + 1
    
    # Precompute positions and initialize variables
    for i in range(1, n + 1):
        pos[permutation[i - 1]] = i
    
    invSum = 0
    totalSum = 0
    result = []
    
    # Main loop to compute the result
    for i in range(1, n + 1):
        totalSum += pos[i]
        invSum += i - sum(pb, pos[i]) - 1
        add(pb, pos[i], 1)
        add(ps, pos[i], pos[i])
        
        mid = find(pb, i // 2)
        if i % 2 == 1:
            mid2 = find(pb, i // 2 + 1)
            seqSum = (i + 1) * (i // 2) // 2
        else:
            mid2 = mid
            seqSum = i * (i // 2) // 2
        
        leftSum = sum(ps, mid)
        rightSum = totalSum - sum(ps, mid2)
        
        result.append(rightSum - leftSum - seqSum + invSum)
    
    return result