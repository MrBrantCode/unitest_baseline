"""
QUESTION:
Create a function named `build_min_heap` that takes an array as input and returns a tuple containing the array transformed into a min heap and the smallest value present in the heap. The function should be able to handle duplicate values, negative numbers, zero, and floating point numbers within the array, and it should be efficient enough to process large arrays of up to 10^6 elements. The implementation should not use any built-in heap functions or libraries. 

Additionally, implement two more functions: `insert_into_heap` that inserts a new element into the min heap while preserving the min heap property, and `extract_smallest` that removes and returns the smallest element from the heap while preserving the min heap property.
"""

def build_min_heap(array):
    def parent(i):
        return (i - 1) // 2

    def left_child(i):
        return 2 * i + 1

    def right_child(i):
        return 2 * i + 2

    def heapify_down(heap, i):
        left = left_child(i)
        right = right_child(i)
        smallest = i
        if left < len(heap) and heap[i] > heap[left]:
            smallest = left
        if right < len(heap) and heap[smallest] > heap[right]:
            smallest = right
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            heapify_down(heap, smallest)

    heap = array[:]
    for i in range((len(array)-2)//2, -1, -1):
        heapify_down(heap, i)
    return (heap, heap[0])


def insert_into_heap(heap, key):
    def heapify_up(heap, i):
        while i != 0 and heap[(i - 1) // 2] > heap[i]:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
            i = (i - 1) // 2
    heap.append(key)
    heapify_up(heap, len(heap) - 1)


def extract_smallest(heap):
    def heapify_down(i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(heap) and heap[i] > heap[left]:
            smallest = left
        if right < len(heap) and heap[smallest] > heap[right]:
            smallest = right
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            heapify_down(smallest)
    root_value = heap[0]
    heap[0] = heap[len(heap)-1]
    heap.pop()
    heapify_down(0)
    return root_value