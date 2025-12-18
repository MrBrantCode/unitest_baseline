"""
QUESTION:
We have a string S consisting of uppercase English letters. Additionally, an integer N will be given.
Shift each character of S by N in alphabetical order (see below), and print the resulting string.
We assume that A follows Z. For example, shifting A by 2 results in C (A \to B \to C), and shifting Y by 3 results in B (Y \to Z \to A \to B).

-----Constraints-----
 - 0 \leq N \leq 26
 - 1 \leq |S| \leq 10^4
 - S consists of uppercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
N
S

-----Output-----
Print the string resulting from shifting each character of S by N in alphabetical order.

-----Sample Input-----
2
ABCXYZ

-----Sample Output-----
CDEZAB

Note that A follows Z.
"""

def shift_string_by_n(N: int, S: str) -> str:
    # List of uppercase English letters
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Convert the input string to a list of characters
    S_list = list(S)
    
    # List to store the resulting characters
    result = []
    
    # Iterate over each character in the input string
    for char in S_list:
        # Find the index of the current character in the letters list
        current_index = letters.index(char)
        
        # Calculate the new index after shifting by N positions
        new_index = (current_index + N) % 26
        
        # Append the new character to the result list
        result.append(letters[new_index])
    
    # Join the result list into a string and return it
    return ''.join(result)