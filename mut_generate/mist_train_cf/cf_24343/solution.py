"""
QUESTION:
Write a function named `create_heap` to implement a Heap data structure. The function should take a list of elements and return a heap where every node is either greater than or equal to or less than its children. The heap should be represented as a list of elements.
"""

def create_heap(lst):
    """
    This function creates a heap from a given list of elements.
    
    :param lst: A list of elements
    :return: A heap where every node is either greater than or equal to or less than its children
    """
    
    def heapify(lst, n, i, is_max):
        """
        Helper function to heapify a subtree rooted at index i
        
        :param lst: The list representing the heap
        :param n: The size of the heap
        :param i: The index of the root of the subtree
        :param is_max: Whether the heap is a max heap or a min heap
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if is_max:
            if left < n and lst[left] > lst[largest]:
                largest = left
            if right < n and lst[right] > lst[largest]:
                largest = right
        else:
            if left < n and lst[left] < lst[largest]:
                largest = left
            if right < n and lst[right] < lst[largest]:
                largest = right
        
        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            heapify(lst, n, largest, is_max)
    
    n = len(lst)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i, True)
    
    # Convert max heap to min heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i, False)
    
    return lst