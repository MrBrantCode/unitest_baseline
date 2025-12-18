"""
QUESTION:
Create a function `permute_string(string)` that generates and prints all unique permutations of the input string without using any built-in functions or libraries for permutation generation. The function should handle duplicate characters in the string by skipping duplicate permutations.
"""

def permute_string(string):
    # Convert the string to a list of characters
    chars = list(string)
    n = len(chars)
    
    # Helper function to swap characters at two indices
    def swap(i, j):
        chars[i], chars[j] = chars[j], chars[i]
    
    # Helper function to generate permutations recursively
    def generate_permutations(start):
        if start == n - 1:
            # Reached the end, print the permutation
            print("".join(chars))
            return
        
        # Keep track of characters already encountered
        encountered = set()
        for i in range(start, n):
            if chars[i] in encountered:
                # Skip duplicate characters
                continue
            
            # Mark the current character as encountered
            encountered.add(chars[i])
            
            # Swap the current character with the start character
            swap(start, i)
            
            # Generate permutations for the remaining characters
            generate_permutations(start + 1)
            
            # Swap back the characters
            swap(start, i)
    
    # Start generating permutations from index 0
    generate_permutations(0)