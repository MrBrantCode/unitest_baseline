"""
QUESTION:
Implement a function `efficient_sort` that takes an array and a boolean `almost_sorted` as input, and returns the sorted array. The function should select the most efficient sorting algorithm (Merge Sort, Quick Sort, or Heap Sort) based on the array's characteristics, such as size and whether it is almost sorted. The function should choose Merge Sort when the array is small or almost sorted, and Quick Sort when the array is large and not almost sorted, with Heap Sort as a fall-back option if needed.
"""

def efficient_sort(arr, almost_sorted):
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return merge(merge_sort(left), merge_sort(right))

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def heap_sort(arr):
        import heapq
        heapq.heapify(arr)
        return [heapq.heappop(arr) for _ in range(len(arr))]

    n = len(arr)
    if n <= 10:
        return merge_sort(arr)
    elif almost_sorted:
        return merge_sort(arr)
    else:
        return quick_sort(arr)