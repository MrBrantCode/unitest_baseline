"""
QUESTION:
Create a function named `count_and_positions` that accepts a string `s` and a character `c` as arguments. The function should return a tuple containing the count of the character `c` within the string `s` and a list of positions where `c` appears. If `c` is not found in `s`, the function should return a message indicating that the character is not present.
"""

def count_and_positions(s, c):
    # Initialize count and positions
    count = 0
    positions = []
    
    # iterate over the string
    for i in range(len(s)):
        if s[i] == c:
            count += 1
            positions.append(i)
            
    # handle the case where the char is not present
    if count == 0:
        return "Character not found in string."
        
    return count, positions