"""
QUESTION:
There are n coins labeled from 1 to n. Initially, coin c_i is on position i and is facing upwards ((c_1, c_2, ..., c_n) is a permutation of numbers from 1 to n). You can do some operations on these coins. 

In one operation, you can do the following:

  * Choose 2 distinct indices i and j.

  * Then, swap the coins on positions i and j.

  * Then, flip both coins on positions i and j. (If they are initially faced up, they will be faced down after the operation and vice versa)




Construct a sequence of at most n+1 operations such that after performing all these operations the coin i will be on position i at the end, facing up.

Note that you do not need to minimize the number of operations.

Input

The first line contains an integer n (3 ≤ n ≤ 2 ⋅ 10^5) — the number of coins.

The second line contains n integers c_1,c_2,...,c_n (1 ≤ c_i ≤ n, c_i ≠ c_j for i≠ j).

Output

In the first line, output an integer q (0 ≤ q ≤ n+1) — the number of operations you used.

In the following q lines, output two integers i and j (1 ≤ i, j ≤ n, i ≠ j) — the positions you chose for the current operation.

Examples

Input


3
2 1 3


Output


3
1 3
3 2
3 1


Input


5
1 2 3 4 5


Output


0

Note

Let coin i facing upwards be denoted as i and coin i facing downwards be denoted as -i.

The series of moves performed in the first sample changes the coins as such:

  * [~~~2,~~~1,~~~3] 
  * [-3,~~~1,-2] 
  * [-3,~~~2,-1] 
  * [~~~1,~~~2,~~~3] 



In the second sample, the coins are already in their correct positions so there is no need to swap.
"""

def reorder_coins(n, coins):
    A = [0] + coins  # Adjusting the list to be 1-indexed
    seen = [0] * (n + 1)
    cycles = []
    ans = []
    
    # Identify cycles
    for i in range(1, n + 1):
        cur = []
        j = i
        while not seen[j]:
            cur.append(j)
            seen[j] = 1
            j = A[j]
        if len(cur) > 1:
            cycles.append(cur)
    
    # Function to perform swap and record operation
    def swap(x, y):
        A[x], A[y] = A[y], A[x]
        ans.append((x, y))
    
    # Process cycles in pairs
    for i in range(1, len(cycles), 2):
        X, Y = cycles[i - 1], cycles[i]
        swap(X[0], Y[0])
        for x in X[1:]:
            swap(x, Y[0])
        for y in Y[1:]:
            swap(y, X[0])
        swap(X[0], Y[0])
    
    # Handle the last cycle if the number of cycles is odd
    if len(cycles) % 2:
        X = cycles[-1]
        if len(X) > 2:
            for x in X[:-2]:
                swap(x, X[-1])
            swap(X[0], X[-2])
            swap(X[-2], X[-1])
            swap(X[0], X[-1])
        else:
            Y = []
            for i in range(1, n + 1):
                if i != X[0] and i != X[1]:
                    break
            swap(i, X[0])
            swap(i, X[1])
            swap(i, X[0])
    
    operations_count = len(ans)
    return operations_count, ans