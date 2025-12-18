"""
QUESTION:
Implement the `quickSort` function to sort a list of elements using the quick sort algorithm, ensuring an optimal time complexity. The function should take a list of elements as input and return a new list with the elements in ascending order. The function should work for lists of any length, including empty lists and lists with duplicate elements.
"""

def quickSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr.pop()
    items_greater = []
    items_lower = []
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)