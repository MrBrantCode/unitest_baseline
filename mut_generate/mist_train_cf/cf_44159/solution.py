"""
QUESTION:
Create a function named `example_func` that takes a list `lst` as input. The function should iterate through the list, and for each integer element found, it should append '5' to the integer after converting it to a string. Non-integer elements, including floating-point numbers and strings, should be left unchanged and copied to the output list as is. The function should return the resulting list without modifying the original list.
"""

def example_func(lst):
   result = []
   for element in lst:
      if type(element) == int:
         result.append(str(element) + '5')
      else:
         result.append(element)
   return result