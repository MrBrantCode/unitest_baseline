"""
QUESTION:
Design a function named `find_occurrences` that accepts two case-sensitive strings as input: `main_string` and `search_string`. The function should return two values: the frequency of `search_string` in `main_string` and a list of start indices where `search_string` appears in `main_string`.
"""

def find_occurrences(main_string, search_string):
    start_index = 0
    count = 0
    indices = []
    
    while True:
        start_index = main_string.find(search_string, start_index)

        if start_index == -1: break

        count += 1
        indices.append(start_index)

        start_index += 1
    
    return count, indices