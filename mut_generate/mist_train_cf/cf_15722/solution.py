"""
QUESTION:
Implement the `replace_words` function, which takes two parameters: `input_string` and `replacement_words`. The function should replace all instances of words in `input_string` with their corresponding replacement words from the `replacement_words` dictionary. The function should not use any built-in string manipulation functions or regular expressions, and it should have a time complexity of O(n^2) and a space complexity of O(n), where n is the length of the input string.
"""

def replace_words(input_string, replacement_words):
    # Split the input string into a list of words
    words = input_string.split()
    
    # Iterate over each word in the list
    for i in range(len(words)):
        # Check if the current word is in the replacement words
        if words[i] in replacement_words:
            # Replace the word with the corresponding replacement word
            words[i] = replacement_words[words[i]]
    
    # Join the words back into a string with spaces
    output_string = ' '.join(words)
    
    return output_string