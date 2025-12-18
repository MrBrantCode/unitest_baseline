"""
QUESTION:
Write a function named `generate_permutations` that takes a string `s` as input and returns all unique permutations of the string in lexicographic order. The function should handle strings with up to 15 characters, including duplicates, and use a time complexity of O(n! * log(n)) and a space complexity of O(n), where n is the length of the input string. The function should not use any built-in libraries or functions for generating permutations.
"""

def generate_permutations(s):
    # Convert string to list of characters
    chars = list(s)
    
    # Sort the characters in lexicographic order
    chars.sort()
    
    # Helper function to backtrack and generate permutations
    def backtrack(start):
        # Base case: when start index reaches the end, we have a permutation
        if start == len(chars):
            yield ''.join(chars)
            return
        
        # Set to keep track of used characters
        used = set()
        
        for i in range(start, len(chars)):
            # Skip duplicate characters
            if chars[i] in used:
                continue
            
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursive call to generate permutations for the remaining characters
            yield from backtrack(start + 1)
            
            # Undo the swap
            chars[start], chars[i] = chars[i], chars[start]
            
            # Add the character to the set of used characters
            used.add(chars[i])
    
    # Call the helper function and return the permutations in lexicographic order
    return sorted(set(backtrack(0)))