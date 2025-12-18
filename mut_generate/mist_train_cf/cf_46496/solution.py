"""
QUESTION:
Create a function called `substring_reversal` that takes three parameters: a string and two indices (start and end). The function should return a substring of the string based on the provided start and end indices, then reverse the extracted substring. If the start index is greater than the end index, reverse the direction of the substring. The function should handle negative indices by converting them to their corresponding positive indices and raise an error if the indices are out of bounds.
"""

def substring_reversal(string, start, end):
    try:
        if start < 0: 
            start += len(string)   # convert negative index to positive
        if end < 0: 
            end += len(string)     # convert negative index to positive

        # return the reversed substring
        return string[start:end][::-1] if start < end else string[end:start][::-1]
    except IndexError:
        return 'Error: Index out of bounds'