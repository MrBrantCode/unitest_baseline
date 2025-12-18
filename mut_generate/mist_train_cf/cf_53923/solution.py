"""
QUESTION:
Implement a function `cubic_dictionary(d)` that constructs a new dictionary from the given dictionary `d`. The function must use a single for loop to traverse the dictionary. Each alphanumeric key in the new dictionary must be the original key prefixed with the string "cube_of_". Each corresponding value must be the cube of the original value, and in case the cubic value turns out to be an even number, it should be replaced by -1.
"""

def cubic_dictionary(d):
    return {f"cube_of_{k}": v**3 if v**3 % 2 != 0 else -1 for k, v in d.items()}