"""
QUESTION:
Write a function `longest_substring(input_string)` that finds the length of the longest substring in a given string of alphanumeric characters that contains only numeric characters and has a sum of digits that is a multiple of 5. The input string may have a maximum length of 1000 characters and the function should have a time complexity of O(n), where n is the length of the input string.
"""

def longest_substring(s):
    start = 0
    end = 0
    sum_of_digits = 0
    longest_length = 0

    while end < len(s):
        if s[end].isdigit():
            sum_of_digits += int(s[end])
            
            if sum_of_digits % 5 == 0:
                longest_length = max(longest_length, end - start + 1)
        else:
            while start < end and (not s[start].isdigit() or sum_of_digits % 5 != 0):
                if s[start].isdigit():
                    sum_of_digits -= int(s[start])
                start += 1
        
        end += 1
    
    return longest_length