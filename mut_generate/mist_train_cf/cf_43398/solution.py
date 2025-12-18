"""
QUESTION:
Write a function `eliminate_characters` that takes a string as input and returns a tuple containing a distinct string with no repeated characters, a dictionary of character frequencies, and the processing time. The function should not use built-in or third-party libraries or methods for string manipulation, except for measuring the processing time.
"""

import time

def eliminate_characters(string):
    start_time = time.time()
    frequency = {}
    new_string = ''
    
    for char in string:
        if char not in frequency:
            frequency[char] = 1
            new_string += char 
        else:
            frequency[char] += 1
            
    end_time = time.time()
    processing_time = end_time - start_time
    
    return new_string, frequency, processing_time