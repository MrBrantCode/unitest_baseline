"""
QUESTION:
Implement a function `generate_permutations` that generates all unique permutations of the given string without using built-in permutation generation functions or libraries. The function should be able to handle input strings of length up to 10 characters and generate unique permutations even if the input string contains duplicate characters. The function should minimize recursive calls and reduce time complexity.
"""

def generate_permutations(string):
    # Create a dictionary to store the frequency of each character in the string
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    
    # Create a list to store the unique permutations
    permutations = []
    
    # Generate permutations recursively
    def generate_permutations_helper(prefix, freq, remaining, permutations):
        # Base case: if there are no more characters remaining, add the prefix to the list of permutations
        if remaining == 0:
            permutations.append(prefix)
            return
        
        # Recursive case: iterate through the characters in the frequency dictionary
        for char in freq:
            # If the character is still available for selection, generate permutations with it
            if freq[char] > 0:
                # Decrement the frequency of the character
                freq[char] -= 1
                # Recursively generate permutations with the updated frequency dictionary and remaining count
                generate_permutations_helper(prefix + char, freq, remaining - 1, permutations)
                # Increment the frequency of the character back to its original value
                freq[char] += 1
                
    generate_permutations_helper("", freq, len(string), permutations)
    return permutations