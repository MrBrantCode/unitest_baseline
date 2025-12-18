"""
QUESTION:
Implement a function `clean_and_sort(lst)` that takes a list of integers and strings as input, filters out the strings, increments each integer by 5, and returns the resulting list of integers in descending order. The time complexity should be O(n log n) and the space complexity should be O(n), where n is the length of the list. You must implement your own sorting algorithm from scratch without using any built-in sorting functions or libraries.
"""

def clean_and_sort(lst):
   result = []
   for element in lst:
      if type(element) == int:
         result.append(element + 5)
   n = len(result)
   for i in range(n):
      for j in range(0, n-i-1):
         if result[j] < result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]
   return result