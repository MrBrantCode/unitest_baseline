"""
QUESTION:
Implement a function named `bubbleSort` that takes an array of strings as input and returns the sorted array in lexicographical order. The function should be optimized to stop iterating if the array is already sorted, and it should have a time complexity of O(n) in the best-case scenario when the input array is already sorted.
"""

def bubbleSort(array):
   n = len(array)
   for pass_num in range(n-1, 0, -1):
       swapped = False
       for i in range(pass_num):
           if array[i] > array[i+1]:
               swapped = True
               temp = array[i]
               array[i] = array[i + 1]
               array[i + 1] = temp
       if not swapped:
           break 
   return array