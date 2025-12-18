"""
QUESTION:
Create a function called `even_odd` that takes an integer as input. The function should return "even" if the input number is even, a multiple of 3, and greater than 10. Otherwise, it should return "odd".
"""

def even_odd(number):
  if number % 2 == 0 and number % 3 == 0 and number > 10:
    return "even"
  else:
    return "odd"