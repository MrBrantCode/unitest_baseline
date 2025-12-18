"""
QUESTION:
Implement a function `kth_smallest(node, k)` that searches for the kth smallest element in a binary search tree with a time complexity of O(log n + k) and space complexity of O(h), where h is the height of the binary search tree. The function should return the kth smallest element and the number of comparisons made during the search process.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def kth_smallest(node, k):
    if node is None:
        return None, 0
    
    comparisons = 0
    stack = []
    count = 0
    while True:
        while node is not None:
            stack.append(node)
            node = node.left
        
        if stack:
            node = stack.pop()
            count += 1
            comparisons += 1
            
            if count == k:
                return node.value, comparisons
            
            node = node.right
        else:
            break
    
    return None, comparisons