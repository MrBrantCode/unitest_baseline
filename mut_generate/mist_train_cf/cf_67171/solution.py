"""
QUESTION:
Write a function `is_ratio_in_proportion` that takes two tuples of two integers each as input, representing two ratios, and returns `True` if the ratios are in proportion and `False` otherwise. The function should determine if the ratios are equivalent by dividing the first number by the second number for each ratio and checking if the resulting values are equal.
"""

def is_ratio_in_proportion(ratio1, ratio2):
  return ratio1[0] / ratio1[1] == ratio2[0] / ratio2[1]