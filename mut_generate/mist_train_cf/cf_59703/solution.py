"""
QUESTION:
Create a function `rearrange(strings, indices)` that takes two inputs: an array of strings and an array of integers. The function should return an array with the strings at the same indices as the integers. If the integer is negative, reverse the string at the corresponding positive index.
"""

def rearrange(strings, indices):
    result = []
    for index in indices:
        if index < 0:
            result.append(strings[-index-1][::-1])
        else:
            result.append(strings[index])
    return result