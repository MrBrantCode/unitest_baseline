"""
QUESTION:
Write a function `cubed_dict` that accepts a sequence of integers and returns a dictionary where each integer is a key and its corresponding value is the cube of the integer. The function must use recursion and cannot utilize built-in Python functions or features like list comprehension, dictionary comprehension, or the standard loop structure.
"""

def cubed_dict(seq, i=0, res=None):
    if res is None:
        res = {}
    if i == len(seq):
        return res
    else:
        res[seq[i]] = seq[i]**3
        return cubed_dict(seq, i+1, res=res)