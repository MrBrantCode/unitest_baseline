"""
QUESTION:
Construct a function `construct_palindromic_string(string, N)` that takes a string and an integer N as input, and returns the Nth palindromic string. The palindromic string should have at least 3 characters and must contain at least one uppercase letter and one lowercase letter. The function should check for valid inputs, where N is greater than or equal to 1 and the string length is greater than or equal to 2. If the input is invalid, return "Invalid input".
"""

def construct_palindromic_string(string, N):
    # Check if N is less than 1 or string length is less than 2
    if N < 1 or len(string) < 2:
        return "Invalid input"
    
    # Create an empty list to store palindromic strings
    palindromes = []
    
    # Iterate from 3 to N (inclusive) to construct palindromic strings
    for i in range(3, N + 1):
        # Create the first half of the palindromic string
        first_half = string[:i//2]
        
        # Create the second half of the palindromic string by reversing the first half
        second_half = first_half[::-1]
        
        # Combine the first half, second half, and the middle character(s) if the length is odd
        if i % 2 != 0:
            middle = string[i//2]
            palindromes.append(first_half + middle + second_half)
        else:
            palindromes.append(first_half + second_half)
    
    # Return the Nth palindromic string
    return palindromes[N-3] if N >= 3 else "No palindromic string exists"