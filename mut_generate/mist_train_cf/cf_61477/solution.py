"""
QUESTION:
Implement a function `unique_values(arr)` that takes an array of mixed data types (integers and strings) as input and returns an array of unique values. The function should consider string numbers ("10", "125", etc.) as separate entities from integers (10, 125, etc.). The solution should have a linear time complexity of O(n), where n is the length of the input array.
"""

def unique_values(arr):
   seen = {}
   result = []
   for item in arr:
       if item not in seen:
           seen[item] = True
           result.append(item)
   return result