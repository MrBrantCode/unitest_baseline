"""
QUESTION:
Create a function called `mostFrequent` that takes an array of names as input and returns the name that appears most frequently in the array. If there are multiple names with the same highest frequency, any of them can be returned. The input array is non-empty and contains only strings.
"""

def mostFrequent(arr):
    frequency_map = {}
    
    for name in arr:
        if name in frequency_map:
            frequency_map[name] += 1
        else:
            frequency_map[name] = 1
    
    return max(frequency_map, key=frequency_map.get)