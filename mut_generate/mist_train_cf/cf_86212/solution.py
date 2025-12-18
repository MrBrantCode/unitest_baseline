"""
QUESTION:
Create a function named `clean_and_sort` that takes a list `lst` as input, where the list contains both integers and strings. The function should return a new list containing only the integers from the input list, each incremented by 5, and sorted in descending order. Implement a sorting algorithm from scratch with a time complexity of O(n log n) and space complexity of O(n), where n is the length of the list. Do not use any built-in sorting functions or libraries.
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