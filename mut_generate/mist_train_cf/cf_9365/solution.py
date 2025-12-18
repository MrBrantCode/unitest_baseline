"""
QUESTION:
Create a function `replace_words` that takes two parameters: an input string and a dictionary of replacement words. The function should replace all instances of the words in the dictionary with their corresponding replacement words in the input string, and return the modified string. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def replace_words(input_string, replacement_words):
    # Split the input string into individual words
    words = input_string.split()
    
    # Iterate over each word and replace it if it's in the replacement words dictionary
    for i in range(len(words)):
        if words[i] in replacement_words:
            words[i] = replacement_words[words[i]]
    
    # Join the words back together into a string
    output_string = ' '.join(words)
    
    return output_string