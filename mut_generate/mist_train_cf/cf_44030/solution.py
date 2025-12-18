"""
QUESTION:
Create a Python method `min_subsequence` that takes an input string and returns the minimal length subsequence encompassing all unique alphabetic entities contained within the input string. The input string contains only alphabetic characters. The method should return the shortest subsequence possible.
"""

def min_subsequence(input_string):
    unique_characters = set(input_string) 
    counter, start, start_index, minimum_length = 0, 0, -1, 10000000000000
    current_count = dict.fromkeys(unique_characters, 0) 

    for end in range(len(input_string)): 

        current_count[input_string[end]] += 1

        if current_count[input_string[end]] == 1: 
            counter += 1

        if counter == len(unique_characters): 
            while current_count[input_string[start]] > 1: 
                if current_count[input_string[start]] > 1: 
                    current_count[input_string[start]] -= 1
                start += 1

            length_window = end - start + 1
            if minimum_length > length_window: 
                minimum_length = length_window 
                start_index = start 

    return input_string[start_index : start_index + minimum_length] 