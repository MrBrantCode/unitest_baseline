"""
QUESTION:
Find the length of the longest continuous segment of a unique character in an arbitrary string using an iterative approach. The function should handle unicode characters and whitespace (' ') and count sequence lengths for either case sensitive or insensitive cases. The function should accept an input string and an optional boolean flag 'case_sensitive' that defaults to True, indicating whether the function should consider characters of different cases as equal or not.
"""

def longest_substring_of_unique_character(input_string, case_sensitive=True):
    max_count = 0
    count = 1
    max_substr = ''
    substr = input_string[0] if len(input_string) else ''
    
    for i in range(1, len(input_string)):
        cur_char = input_string[i]
        prev_char = input_string[i-1]

        if not case_sensitive:
            cur_char = cur_char.lower()
            prev_char = prev_char.lower()

        if cur_char == prev_char:
            count += 1
            substr += input_string[i]
        else:
            if count > max_count:
                max_count = count
                max_substr = substr
            
            count = 1
            substr = input_string[i]

    if count > max_count:
        max_count = count
        max_substr = substr
    
    return max_substr