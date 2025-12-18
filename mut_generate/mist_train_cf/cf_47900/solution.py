"""
QUESTION:
Create a function `complex_string_manipulations(s1, s2, s3, limit)` that takes three strings `s1`, `s2`, `s3`, and an optional integer `limit` (defaulting to 100) as input. The function should return a string that is the result of concatenating `s1` in uppercase, the reverse of `s2`, and the reverse of `s3`, separated by '@' and '#'. If the combined length of `s1`, `s2`, and `s3` exceeds the specified `limit`, the function should return an error message "Error: Combined length of strings is over limit".
"""

def complex_string_manipulations(s1, s2, s3, limit=100):
    combined_string = s1 + s2 + s3
    if len(combined_string) > limit:
        return "Error: Combined length of strings is over limit"
    else:
        rev_s2 = s2[::-1]
        upper_s1 = s1.upper()
        rev_s3 = s3[::-1]
        return upper_s1 + '@' + rev_s2 + '#' + rev_s3