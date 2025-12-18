"""
QUESTION:
Create a function `scale_sigmoid(num, factor)` that scales a number `num` by the given `factor` using the sigmoid function `f(x) = 1 / (1 + e^(-x))`. The function should take two parameters, `num` and `factor`, with `factor` having a default value.
"""

import math

def entrance(num, factor=0.5):
    scaled_num = num * factor
    return 1 / (1 + math.exp(-scaled_num))