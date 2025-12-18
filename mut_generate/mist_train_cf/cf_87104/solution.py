"""
QUESTION:
Construct an array of N elements from a given string of length N, where each element contains only unique characters. If any character is repeated in the string, ignore it and do not include it in the array. The function must have a time complexity of O(N) and a space complexity of O(N). 

Implement the function `construct_array(string)`.
"""

def construct_array(string):
    array = set()
    for char in string:
        if char not in array:
            array.add(char)
    return list(array)