"""
QUESTION:
Implement a function `kth_smallest_element(root, k)` that finds the kth smallest element in a binary search tree and returns the element along with the number of comparisons made during the search process. The function should use an iterative approach, have a time complexity of O(log n + k), and a space complexity of O(h), where h is the height of the binary search tree. The function should take as input the root of the binary search tree and an integer k representing the rank of the element to be found.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kth_smallest_element(root, k):
    stack = []
    rank = 0
    comparisons = 0

    while True:
        while root is not None:
            stack.append(root)
            root = root.left

        if len(stack) == 0:
            break

        node = stack.pop()
        comparisons += 1
        rank += 1
        if rank == k:
            return node.data, comparisons
        
        root = node.right
    
    return None, comparisons