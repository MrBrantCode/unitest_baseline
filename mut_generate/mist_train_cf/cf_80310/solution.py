"""
QUESTION:
Create a function called `find_substring` that takes two parameters, `main_string` and `sub_string`, and returns a dictionary with the following keys: 'exists', 'count', and 'indices'. The function should determine if `sub_string` exists within `main_string`, count the number of occurrences, and record the starting indices of each occurrence. The function must be implemented without using pre-existing string functions. The comparison should be case-sensitive.
"""

def find_substring(main_string, sub_string):
    substring_len = len(sub_string)
    main_string_len = len(main_string)
    
    result = {'exists': False, 'count': 0, 'indices': []}
    
    for i in range(main_string_len - substring_len + 1):
        if main_string[i : i + substring_len] == sub_string:
            result['exists'] = True
            result['count'] += 1
            result['indices'].append(i)
            
    return result