"""
QUESTION:
Create a function `remove_repeats` that takes a list of strings as input and returns a modified list where all repeating substrings of length 3 or more are removed. The function should consider overlapping chunks and remove the earlier occurrence of the repeating substring.
"""

def remove_repeats(input_list):
    output_list = []

    for word in input_list:
        processed_word = ""
        
        while len(word) >= 3:
            chunk = word[0:3] 
            rest_of_word = word[3:] 
            
            if chunk not in rest_of_word:
                processed_word += chunk
            else:
                while chunk in rest_of_word:
                    chunk = chunk[:-1]
                    if not chunk:
                        break
                processed_word += chunk
            word = rest_of_word 
            
        processed_word += word 
        output_list.append(processed_word)
        
    return output_list