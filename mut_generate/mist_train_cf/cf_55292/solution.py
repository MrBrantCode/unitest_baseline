"""
QUESTION:
Write a function called `find_subsegments(s)` that takes a string `s` as input and returns a list of tuples, where each tuple contains the start index, end index, and the sub-segment string of uninterrupted identical characters in the string. The function should run in O(n) time complexity, where n is the length of the string, and handle strings with special characters and digits in a case-sensitive manner.
"""

def find_subsegments(s):
    """
    This function finds all uninterrupted sub-segments of identical characters in a given string.
    
    Parameters:
    s (str): The input string to find sub-segments in.
    
    Returns:
    list: A list of tuples, where each tuple contains the start index, end index, and the sub-segment string.
    """
    sub_segments = []
    start = 0
    end = 0
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            end = i
        else:
            sub_segments.append((start, end, s[start:end+1]))
            start = i
            end = i
            
    sub_segments.append((start, end, s[start:end+1]))
    return sub_segments