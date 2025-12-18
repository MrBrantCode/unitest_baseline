"""
QUESTION:
Create a function called "string_length" that takes a string as input and returns its length. The input string can contain multiple lines and special characters, including Unicode characters. The function should not rely on built-in length calculation functions and should remove any leading or trailing whitespaces before calculating the length. Implement the function's logic to count characters manually.
"""

def string_length(s):
    s = s.strip()  
    count = 0  
    
    for char in s:  
        count += 1  
        
    return count  