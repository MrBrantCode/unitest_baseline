"""
QUESTION:
Write a function `find_palindromic_substrings(inputString)` that takes a string `inputString` as input and returns a list of all palindromic substrings of length greater than or equal to 4. Overlapping substrings are allowed.
"""

def find_palindromic_substrings(inputString):
    substrings = []
    
    # Check all possible substrings of length 4 or greater
    for i in range(len(inputString)):
        for j in range(i + 3, len(inputString)):
            substring = inputString[i:j+1]
            
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                substrings.append(substring)
    
    return substrings