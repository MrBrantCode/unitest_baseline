"""
QUESTION:
Calculate the total number of possible binary trees with n nodes, where each left subtree has a prime number of nodes and each right subtree has a Fibonacci number of nodes. Define a function `countTrees(n)` to solve this problem, where n is the total number of nodes in the binary tree. The Fibonacci sequence starts from 0, i.e., `fib(0) = 0` and `fib(1) = 1`.
"""

def countTrees(n):
    def prime(m):
        if m < 2:
            return m == 2
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                return False
        return True

    def fib(m):
        if m <= 1:
            return m
        a, b = 0, 1
        for _ in range(2, m + 1):
            a, b = b, a + b
        return b

    if n <= 1:
        return 1
    
    count = 0
    for i in range(0, n):
        left_nodes = i
        right_nodes = n - 1 - left_nodes
        if prime(left_nodes) and fib(right_nodes) == right_nodes:
            count += countTrees(left_nodes) * countTrees(right_nodes)
    
    return count