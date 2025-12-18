"""
QUESTION:
Create a function `shared_elements(arr1, arr2)` that takes two lists of integers `arr1` and `arr2` as input and returns a dictionary where the keys are the shared elements found in both arrays and the values are dictionaries containing the frequency of each shared element in `arr1` and `arr2`. The function should only include elements that are present in both arrays in the output dictionary.
"""

def shared_elements(arr1, arr2):
    frequency_dict = {}
    for item in arr1:
        if item in arr2:
            if item in frequency_dict:
                frequency_dict[item]['arr1'] += 1
            else:
                frequency_dict[item] = {'arr1': 1, 'arr2': 0}
                
    for item in arr2:
        if item in arr1:
            if item in frequency_dict:
                frequency_dict[item]['arr2'] += 1
            else:
                frequency_dict[item] = {'arr1': 0, 'arr2': 1}
                
    return frequency_dict