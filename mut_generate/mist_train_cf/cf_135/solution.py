"""
QUESTION:
Write a function `get_descendant_sum` that takes the root of a binary tree as input and returns the sum of values of all descendant nodes that are at an even level and whose values are divisible by a prime number. The time complexity of the function should not exceed O(n), where n is the number of nodes in the tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_descendant_sum(root, level=0, sum=0):
    if root is None:
        return sum
    if level % 2 != 0 and is_prime(root.value):
        sum += root.value
    sum = get_descendant_sum(root.left, level + 1, sum)
    sum = get_descendant_sum(root.right, level + 1, sum)
    return sum