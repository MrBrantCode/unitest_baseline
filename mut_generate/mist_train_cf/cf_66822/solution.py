"""
QUESTION:
Create a function `longest_common_prefix(str1, str2)` that finds the longest common prefix of two input strings `str1` and `str2`. The function should handle cases where either string is null or only contains whitespace, returning a corresponding error message. The function should also be efficient for longer strings.
"""

def longest_common_prefix(str1, str2):
    if not str1 or str1.isspace() or not str2 or str2.isspace():
        return "One of the strings is either null or only contains whitespaces."
      
    else:
        common_prefix = ""
        for char1, char2 in zip(str1, str2):
            if char1 == char2:
                common_prefix += char1
            else:
                break
              
        return common_prefix