"""
QUESTION:
Given a binary heap implementation of Priority Queue. Extract the maximum element from the queue i.e. remove it from the Queue and return it's value. 
 
Example 1:
Input: 4 2 8 16 24 2 6 5
Output: 24
Priority Queue after extracting maximum: 16 8 6 5 2 2 4
Example 2:
Input: 64 12 8 48 5
Output: 64
Priority Queue after extracting maximum: 48 12 8 5
 
Your Task:
Complete the function extractMax() which extracts the maximum element, i.e. remove it from the Queue and return it's value.
 
Expected Time Complexity: O(logN)
Expected Space Complexity: O(N)
 
Constraints:
1<=N<=500
"""

def extract_max(heap, size):
    """
    Extracts the maximum element from a binary heap and returns it.

    Parameters:
    - heap (list): A list representing the binary heap.
    - size (int): The current size of the heap.

    Returns:
    - int: The maximum element extracted from the heap.
    """
    if size == 0:
        raise ValueError("Heap is empty")
    
    max_element = heap[0]
    heap[0] = heap[size - 1]
    size -= 1
    shift_down(heap, size, 0)
    
    return max_element

def shift_down(heap, size, index):
    """
    Shifts down the element at the given index to maintain the heap property.

    Parameters:
    - heap (list): A list representing the binary heap.
    - size (int): The current size of the heap.
    - index (int): The index of the element to shift down.
    """
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    
    if left < size and heap[left] > heap[largest]:
        largest = left
    
    if right < size and heap[right] > heap[largest]:
        largest = right
    
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        shift_down(heap, size, largest)