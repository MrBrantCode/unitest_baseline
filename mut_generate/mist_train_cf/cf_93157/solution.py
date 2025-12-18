"""
QUESTION:
Write a function named `generate_strings` that generates all possible strings of a given length `n` using the characters A, B, and C, with the restriction that each character must occur at least once. The function should return a list of all possible strings.
"""

def generate_strings(n):
    # Base case
    if n == 3:
        return ['ABC']
    
    # Generate strings recursively
    sub_strings = generate_strings(n-1)
    strings = []
    
    for sub_string in sub_strings:
        # Determine the positions of A, B, and C in the sub-string
        a_pos = sub_string.find('A')
        b_pos = sub_string.find('B')
        c_pos = sub_string.find('C')
        
        # Generate all possible strings by filling the remaining positions
        for i in range(len(sub_string)+1):
            new_string = sub_string[:i] + 'A' + sub_string[i:]
            if i != a_pos and new_string.count('A') > 1:
                strings.append(new_string)
            
            new_string = sub_string[:i] + 'B' + sub_string[i:]
            if i != b_pos and new_string.count('B') > 1:
                strings.append(new_string)
            
            new_string = sub_string[:i] + 'C' + sub_string[i:]
            if i != c_pos and new_string.count('C') > 1:
                strings.append(new_string)
    
    return strings