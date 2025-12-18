"""
QUESTION:
Implement the function `three_sum(array, target)`: Given an array of integers and a target number, return all unique sets of three numbers in the array that sum up to the target number. The function should take two parameters: `array` (a list of integers) and `target` (an integer). The function should return a list of lists, where each sublist contains three numbers that add up to the target.
"""

def three_sum(array, target):
   result_sets = [] 
   for i in range(len(array) - 2):
       for j in range(i+1, len(array) - 1):
           for k in range(j+1, len(array)):
               if array[i] + array[j] + array[k] == target: 
                   result_sets.append([array[i], array[j], array[k]])
   return result_sets 