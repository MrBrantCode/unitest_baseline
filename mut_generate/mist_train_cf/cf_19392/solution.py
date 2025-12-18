"""
QUESTION:
Create a function 'subStr' that takes a string and two indices, start and end, as input and returns a substring. The substring should start at the start index (inclusive) and end at the end index (exclusive). The function must handle edge cases where the start index is greater than the end index, and where the end index is greater than the length of the string. The function should have a time complexity of O(n), where n is the length of the string, and cannot use built-in substring functions or libraries.
"""

def subStr(string, start, end):
    substring = ""  
    if start > end:  
        return substring  
    
    if end > len(string):  
        end = len(string)  
    
    for i in range(start, end):  
        substring += string[i]  
    
    return substring 