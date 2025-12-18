"""
QUESTION:
Implement a function `quick_sort` that sorts a double-ended queue (deque) in ascending order, handling duplicate elements correctly. The function should take a deque and two indices `low` and `high` as input, and sort the elements within the specified range. The function should not return anything, but instead modify the original deque in place.
"""

def quick_sort(deque, low, high): 
    def partition(deque, low, high): 
        pivot = deque[high]
        i = low - 1
        for j in range(low, high):
            if deque[j] <= pivot:
                i += 1
                deque[i], deque[j] = deque[j], deque[i]
        deque[i+1], deque[high] = deque[high], deque[i+1]
        return i + 1

    if low < high: 
        pivot_index = partition(deque, low, high) 
        quick_sort(deque, low, pivot_index-1) 
        quick_sort(deque, pivot_index+1, high)