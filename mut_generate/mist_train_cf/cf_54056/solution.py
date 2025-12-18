"""
QUESTION:
Create a function called `multimode` that takes a numerical array as input and returns the mode(s) of the array along with their frequency. The function should be able to handle both unimodal and multimodal data. Implement the function using Python, utilizing the necessary libraries such as numpy and pandas, or other alternatives if needed. The solution should be able to handle scenarios where the input data exhibits more than one mode.
"""

from collections import Counter

def multimode(data):
    counts = dict(Counter(data))
    maxCount = max(counts.values())
    
    if list(counts.values()).count(maxCount) == 1:
        # for unimodal data
        mode = [key for key, value in counts.items() if value == maxCount]
    else:
        # for multimodal data
        mode = [key for key, value in counts.items() if value == maxCount]
    return mode, maxCount