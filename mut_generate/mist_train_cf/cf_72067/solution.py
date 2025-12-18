"""
QUESTION:
Create a function named `rev_alt_words` that takes a string as input and returns the string with every second word reversed. For example, given the string "Welcome to the world of AI and Machine Learning", the output should be "Welcome ot the dlrow of AI dna Machine Learning".
"""

def rev_alt_words(string):
    # Splitting the string into a list of words.
    phrase = string.split(' ')
    
    # Going through every word in the list.
    for i in range(len(phrase)):
        # Checking if the word is at an even position (2nd, 4th, 6th, etc. word, zero-indexed).
        if i % 2 != 0:
            # Initialising the reversed word.
            reversed_word = ''
            
            # Reversing the current word.
            for char in phrase[i]:
                # This will add the character at the beginning of the reversed word.
                reversed_word = char + reversed_word
                
            # Replacing the word with its reversed version in the list.
            phrase[i] = reversed_word
            
    # Joining the list back into a string.
    return ' '.join(phrase)