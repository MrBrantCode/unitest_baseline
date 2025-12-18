"""
QUESTION:
Create a function called `string_segment` that takes a string `sentence` as input and returns a dictionary where the keys are the unique alphabetic characters in the string and the values are their corresponding frequencies. The function should ignore whitespace and special characters, and it should be case sensitive. Do not use any high-level functions or libraries for character segmentation and frequency counting.
"""

def string_segment(sentence):
    result = {}
    for char in sentence:
        if char.isalpha():  
            if char not in result:
                result[char] = 1  
            else:
                result[char] += 1  
    return result