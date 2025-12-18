"""
QUESTION:
Create a function `count_chars(multi_array)` to count the frequency of each character in a given multi-dimensional array. The function should return a dictionary where keys are unique characters and values are their respective frequencies. The input multi-dimensional array can contain any number of sub-arrays and any number of characters in each sub-array.
"""

def entance(multi_array):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}
    
    # Iterate over the multi-dimensional array
    for row in multi_array:
        for item in row:
            # If the character is already in the dictionary, increment its count
            if item in char_frequency:
                char_frequency[item] += 1
            # If the character is not in the dictionary, add it with count 1
            else:
                char_frequency[item] = 1
                
    return char_frequency