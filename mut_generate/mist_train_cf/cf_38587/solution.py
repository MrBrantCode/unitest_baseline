"""
QUESTION:
Write a function `num2bin` that takes a positive integer `num` as input and returns a list representing the binary digits of the input number. The function should handle the case when the input number is 0 by returning [0].
"""

import numpy as np

def num2bin(num):
    if num == 0:
        return [0]
    else:
        pow_max = int(np.floor(np.log2(num)))
        pow_list = [k for k in range(pow_max, -1, -1)]  
        bin_list = []

        for power in pow_list:
            if num >= 2 ** power:
                bin_list.append(1)
                num -= 2 ** power
            else:
                bin_list.append(0)

        return bin_list