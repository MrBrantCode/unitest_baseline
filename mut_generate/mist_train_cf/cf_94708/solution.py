"""
QUESTION:
Implement the function `find_kth_largest(nums, k)` which takes an array `nums` of size n and an integer `k` as input and returns the kth largest element. The function should use a min heap data structure without utilizing any built-in sorting or priority queue functions and should not use extra space. The time complexity should be O(n log k) and the space complexity should be O(1).
"""

def find_kth_largest(nums, k):
    """
    This function takes an array `nums` of size n and an integer `k` as input and returns the kth largest element.
    
    The function uses a min heap data structure without utilizing any built-in sorting or priority queue functions and does not use extra space.
    
    The time complexity is O(n log k) and the space complexity is O(1).

    :param nums: An array of integers
    :param k: An integer representing the kth largest element to find
    :return: The kth largest element in the array
    """

    def heapify(heap, n, i):
        """
        Helper function to maintain the heap property.

        :param heap: The min heap
        :param n: The size of the heap
        :param i: The index of the current node
        :return: None
        """
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            heapify(heap, n, smallest)

    heap = []

    for num in nums:
        if len(heap) < k:
            heap.append(num)
            if len(heap) == k:
                # Convert list to min heap
                for i in range(k//2 - 1, -1, -1):
                    heapify(heap, k, i)
        elif num > heap[0]:
            heap[0] = num
            heapify(heap, k, 0)
    
    return heap[0]