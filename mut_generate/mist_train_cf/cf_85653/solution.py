"""
QUESTION:
Write a function called `bubble_sort` that sorts an unsorted list of integers in ascending order without using built-in sorting functions. The function should take a list of integers as input and return the sorted list. Analyze the time complexity of the implemented function.
"""

def bubble_sort(numbers):
   for i in range(len(numbers)):
      for j in range(0, len(numbers) - i - 1):
         if numbers[j] > numbers[j + 1] :
               numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
   return numbers