"""
QUESTION:
Write a function `replace_words` that takes an input string and a dictionary of replacement words as input, and returns the modified string with all instances of the words in the dictionary replaced. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string. The replacement dictionary should support multiple replacement words.
"""

def replace_words(input_string, replacement_words):
    words = input_string.split()
    for i in range(len(words)):
        if words[i] in replacement_words:
            words[i] = replacement_words[words[i]]
    output_string = ' '.join(words)
    return output_string