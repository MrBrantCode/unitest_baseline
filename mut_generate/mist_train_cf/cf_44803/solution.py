"""
QUESTION:
Write a function named `multiply_num` that takes an array of numbers as input and returns the product of all numbers in the array. The function must use a `while` loop to iterate through the array. If the input array is empty, the function should return a message indicating that there are no elements to multiply.
"""

def multiply_num(n):
   if len(n) == 0:
      return "No elements to multiply"
   result = 1
   i = 0
   while i < len(n):
      result *= n[i]
      i += 1
   return result