"""
QUESTION:
Write a function `longest_palindrome(input_string)` that finds the longest palindromic substring of a given input string. The input string contains both uppercase and lowercase letters, and the solution must be case-sensitive. The function should return the longest palindromic substring.
"""

def longest_palindrome(input_string):
    size = len(input_string)
    
    # init table
    table = [[0 for x in range(size)] for y in range(size)]
    
    # Fill in table for single-character palindromes
    for i in range(size):
        table[i][i] = 1
        
    length = 1
    start = 0
    
    for gap in range(2, size+1):
        for i in range(size-gap+1):
            j = gap+i-1
            if gap ==2:
                if input_string[i] == input_string[j]:
                    table[i][j] = 1
            else:
                if input_string[i] == input_string[j] and table[i+1][j-1] == 1:
                    table[i][j] = 1
            if table[i][j] == 1 and gap > length:
                start = i
                length = gap
                
    return input_string[start:start+length]