"""
QUESTION:
Neil has a [perfect binary tree] with N nodes, and an integer M. He can assign values to nodes. He calls the tree good if the following conditions are met:
Nodes' values are positive integers no more than M.
Nodes at even levels have values strictly more than their parents' values.
Nodes at odd levels have values strictly less than their parents's values.

How many ways can Neil assign values to all nodes to get a good perfect binary tree? Since the answer can be large, please output it under modulo 10^{9} + 7.

Note:
The root of the tree is at layer 1.
Two assignments are different if there is at least one node with different values in both assignments.
You may need to use 64-bit data types in your programming language to take input.

------ Input Format ------ 

- The first line of each input contains T - the number of test cases. The test cases then follow.
- The only line of each test case contains two space-separated integers N and M - the number of nodes on the tree and the maximum value of any node.

------ Output Format ------ 

For each test case, output on a single line the number of different assignment modulo 10^{9} + 7.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ M ≤ 1000$
$1 ≤ N < 2^{59}$
- It is guaranteed you can make a perfect binary tree with exactly $N$ nodes.

----- Sample Input 1 ------ 
1
3 3

----- Sample Output 1 ------ 
5
----- explanation 1 ------ 
- Test case $1$: Here are all the possible assignments.

![1-2-2]

![1-2-3]

![1-3-2]

![1-3-3]

![2-3-3]
"""

def count_good_assignments(N: int, M: int) -> int:
    mod = 10 ** 9 + 7

    def add(a, b):
        return (a % mod + b % mod) % mod

    def mul(a, b):
        return a % mod * (b % mod) % mod

    def sub(a, b):
        return (a - b + mod) % mod

    # Determine the height of the tree
    x = 0
    for i in range(60):
        if N >> i & 1:
            x = i

    # Initialize dp array
    dp = [0 for _ in range(M + 1)]
    for i in range(1, M + 1):
        dp[i] = 1

    # Fill dp array based on tree height
    for i in range(x - 1, -1, -1):
        prefix = [0 for _ in range(M + 1)]
        for j in range(1, M + 1):
            prefix[j] = add(prefix[j - 1], dp[j])
        for j in range(1, M + 1):
            if i & 1 == 0:
                this = sub(prefix[M], prefix[j])
                dp[j] = mul(this, this)
            else:
                this = prefix[j - 1]
                dp[j] = mul(this, this)

    # Calculate the final answer
    ans = 0
    for j in range(1, M + 1):
        ans = add(ans, dp[j])

    return ans