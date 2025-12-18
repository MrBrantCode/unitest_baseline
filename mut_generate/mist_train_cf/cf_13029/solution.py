"""
QUESTION:
Implement a function `is_binary_heap` that checks whether a given array represents a binary heap. The array is 0-indexed, and for any given index i, the left child of the node at index i is stored at index 2*i + 1, and the right child is stored at index 2*i + 2. The function should take as input a list of integers and a boolean indicating whether the heap is a min-heap or a max-heap, and return a boolean indicating whether the array represents a valid binary heap of the specified type.
"""

def is_binary_heap(heap, is_min_heap):
    """
    Checks whether a given array represents a binary heap.

    Args:
    heap (list): A list of integers representing the heap.
    is_min_heap (bool): A boolean indicating whether the heap is a min-heap or a max-heap.

    Returns:
    bool: A boolean indicating whether the array represents a valid binary heap of the specified type.
    """
    def is_valid_heap(index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index >= len(heap):
            return True  # No more children to check

        if is_min_heap:
            return (heap[index] <= heap[left_child_index] if left_child_index < len(heap) else True) and \
                   (heap[index] <= heap[right_child_index] if right_child_index < len(heap) else True) and \
                   is_valid_heap(left_child_index) and is_valid_heap(right_child_index)
        else:
            return (heap[index] >= heap[left_child_index] if left_child_index < len(heap) else True) and \
                   (heap[index] >= heap[right_child_index] if right_child_index < len(heap) else True) and \
                   is_valid_heap(left_child_index) and is_valid_heap(right_child_index)

    return is_valid_heap(0)