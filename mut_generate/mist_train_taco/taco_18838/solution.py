"""
QUESTION:
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:


Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

def count_unique_bst(n: int) -> int:
    """
    Counts the number of structurally unique Binary Search Trees (BSTs) that can be formed with n nodes.

    Args:
        n (int): The number of nodes in the BST.

    Returns:
        int: The number of unique BSTs.
    """
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    
    # Memoization dictionary to store previously computed results
    hash_map = {}
    
    def helper(n):
        if n in hash_map:
            return hash_map[n]
        res_sum = 0
        for i in range(n):
            temp_sum = helper(i) * helper(n - (i + 1))
            res_sum += temp_sum
        hash_map[n] = res_sum
        return res_sum
    
    return helper(n)