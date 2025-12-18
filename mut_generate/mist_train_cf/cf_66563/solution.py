"""
QUESTION:
Create a function named `specialized_BST_sort` that takes an array of integers and decimals as input and returns the array sorted in a unique order using a Binary Search Tree (BST) protocol. The sequence of sorting must start with the smallest number, followed by the maximum residual number, then the minimum residual number from the remaining ones, and continue with this pattern. The function should handle arrays of any size, including empty arrays, and arrays with duplicate values.
"""

def specialized_BST_sort(arr):
    if not arr: return []
   
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BST:
        def __init__(self):
            self.root = None

        def insert(self, value):
            if not self.root:
                self.root = Node(value)
            else:
                self._insert(self.root, value)

        def _insert(self, current_node, value):
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = Node(value)
                else:
                    self._insert(current_node.left, value)
            else:
                if not current_node.right:
                    current_node.right = Node(value)
                else:
                    self._insert(current_node.right, value)

        def get_sorted_elements(self):
            return self._get_sorted_elements(self.root)

        def _get_sorted_elements(self, current_node, results=None):
            if results is None:
                results = []
            if current_node:
                self._get_sorted_elements(current_node.left, results)
                results.append(current_node.value)
                self._get_sorted_elements(current_node.right, results)
            return results

    bst = BST()
    for el in arr:
        bst.insert(el)
        
    sorted_elements = bst.get_sorted_elements()
    result = []
    while sorted_elements:
        result.append(sorted_elements.pop(0))
        if sorted_elements:
            result.append(sorted_elements.pop())
    return result