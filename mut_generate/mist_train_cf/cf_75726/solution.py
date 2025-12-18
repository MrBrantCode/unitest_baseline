"""
QUESTION:
Create a function called `count_freq` that takes a list of elements (which can be of different data types, including nested lists) as input. The function should return a dictionary where the keys are the unique elements from the input list and the values are their respective frequencies. The function should be able to handle nested lists recursively.
"""

def count_freq(arr, freq=None):
    if freq is None:
        freq = {}
    
    for element in arr:
        if isinstance(element, list):
            freq = count_freq(element, freq)
        else:
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1
                
    return freq