"""
QUESTION:
Create a function called `recurDig` within a class that takes a dictionary and a key as parameters, and recursively searches for the key in the dictionary and its nested dictionaries. The function should return the corresponding value if the key is found, otherwise return `None`. The function should be tested in another function called `errorHandleFunc` within the same class, along with exception handling to catch and print any runtime errors. The `errorHandleFunc` function should also attempt to access an index out of range in a list and a non-existent key in a dictionary to test the exception handling. The code should be able to handle any potential runtime errors gracefully.
"""

def recurDig(dictData, key):
    for k, v in dictData.items():    
        if k == key:
            return v
        elif isinstance(v, dict):    
            found = recurDig(v, key)
            if found is not None:   
                return found
    return None