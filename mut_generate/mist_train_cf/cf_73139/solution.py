"""
QUESTION:
Write a function `detectDupes` that takes a tuple as input and returns a dictionary where the keys are the duplicate elements from the tuple and the values are their corresponding counts. The function should not use any built-in Python libraries.
"""

def detectDupes(t):
    count = {}
    
    for i in t:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    duplicates = {k: v for k, v in count.items() if v > 1}
    
    return duplicates