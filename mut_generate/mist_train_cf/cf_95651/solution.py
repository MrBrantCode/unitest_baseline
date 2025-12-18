"""
QUESTION:
Create a function 'subStr' that takes a string and two indices (start and end) as input and returns the substring from the start index (inclusive) to the end index (exclusive). The function should have a time complexity of O(n), where n is the length of the string. The function must handle the edge cases where the start index is greater than the end index (returning an empty string) and where the end index is greater than the length of the string (returning a substring from the start index to the end of the string).
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