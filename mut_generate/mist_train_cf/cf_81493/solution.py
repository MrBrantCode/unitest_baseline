"""
QUESTION:
Create a function called `repeat_strings` that takes a dictionary where keys are strings and values are numbers, and a target string that contains one of the keys from the dictionary followed by an index.

For each key in the dictionary, if the key matches the string part of the target string, repeat the key the number of times specified by the index in the target string. Otherwise, repeat the key the number of times specified by its corresponding value in the dictionary.

Return a list of the repeated strings. The function should have a time complexity of O(n), where n is the number of keys in the dictionary.
"""

def repeat_strings(dict, target_str):
    target_key = target_str[:-1]
    target_val = int(target_str[-1])

    results = []
    for key, val in dict.items():
        times = target_val if key == target_key else val
        results.extend([key] * times)
        
    return results