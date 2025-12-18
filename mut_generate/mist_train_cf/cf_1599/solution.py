"""
QUESTION:
Find the k most frequent elements in a given dictionary. The function, `find_k_most_frequent(my_dict, k)`, should return a list of the k most frequent elements in `my_dict` based on their values. If multiple elements have the same highest frequency, return all of them. If the dictionary is empty, return an empty list. 

The dictionary `my_dict` will only contain lowercase letters as keys and values with lengths between 1 and 10 characters. The value of `k` will always be a positive integer between 1 and 100, and the dictionary will always contain at least `k` distinct elements with a total of 1 to 1000 elements.
"""

def find_k_most_frequent(my_dict, k):
    result = []
    if not my_dict:
        return result
    
    frequency = {}
    for element in my_dict.values():
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    for key, _ in sorted_frequency:
        result.append(key)
        if len(result) == k:
            break
    
    return result