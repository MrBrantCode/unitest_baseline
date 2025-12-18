"""
QUESTION:
Create a function `QuickSortTree` that implements a self-balancing binary search tree with methods to insert elements, sort an array, and perform in-order traversal. The sorting algorithm should have a time complexity of O(nlogn) and the tree should support deletion of elements while maintaining its sorted order and self-balancing properties. The function should handle potential errors or exceptions during the sorting process and include unit tests to verify correctness. The output should be the sorted array in ascending order.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def QuickSortTree(array):
    if not array:
        return []
    
    def insert(value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                insert(value, node.right)

    def sort(low, high, array):
        if low < high:
            pivot_index = partition(array, low, high)
            sort(low, pivot_index - 1, array)
            sort(pivot_index + 1, high, array)

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def in_order_traversal(node):
        result = []
        if node.left:
            result += in_order_traversal(node.left)
        result.append(node.value)
        if node.right:
            result += in_order_traversal(node.right)
        return result

    root = Node(array[0])
    for value in array[1:]:
        insert(value, root)
    
    return in_order_traversal(root)