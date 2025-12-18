"""
QUESTION:
Create a function called `pos_neg_zero` that takes an integer `num` as input and returns a string indicating whether the number is positive, negative, or zero.
"""

def entrance(num):
  if num > 0:
    return "positive"
  elif num < 0:
    return "negative"
  else:
    return "zero"