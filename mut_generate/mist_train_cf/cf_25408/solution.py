"""
QUESTION:
Implement three different sorting functions - `bubble_sort`, `insertion_sort`, and `heap_sort` - that take a list of integers as input and return the sorted list. Each function should sort the list in ascending order. Assume that the input list contains only integers.
"""

### Bubble Sort algorithm
def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

### Insertion Sort algorithm
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

### Heap Sort algorithm
def heapify(lst, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2 
  
    if l < n and lst[i] < lst[l]:
        largest = l
  
    if r < n and lst[largest] < lst[r]:
        largest = r
  
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)

def heap_sort(lst):
    for i in range(len(lst) // 2 - 1, -1, -1):
        heapify(lst, len(lst), i)
   
    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst