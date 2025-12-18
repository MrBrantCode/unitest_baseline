"""
QUESTION:
Implement a function named `quick_sort` that sorts an array of elements using the Quick sort algorithm. The function should take an array as input and return the sorted array. Use recursion to break down the problem into smaller sub-arrays and sort them.
"""

def quick_sort(array):
   if len(array) <= 1:
       return array
   else:
       pivot = array.pop()
   items_greater = []
   items_lower = []
   for item in array:
       if item > pivot:
           items_greater.append(item)
       else:
           items_lower.append(item)
   return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)