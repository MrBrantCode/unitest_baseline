"""
QUESTION:
Implement a function called `remove_repetitive_substrings` that takes an array of strings as input and returns the array with all repetitive substrings of length 3 or more removed from each string. The function should remove all occurrences of the repetitive substrings, including overlapping instances.
"""

def remove_repetitive_substrings(array):
    for i in range(len(array)):
        for length in reversed(range(3, len(array[i])+1)): 
            for start_index in range(0, len(array[i])-length+1):
                substring = array[i][start_index:start_index+length]
                if array[i].count(substring) > 1:
                    array[i] = array[i].replace(substring, '')
    return array