"""
QUESTION:
Write a function `reverse_sentence(sentence)` that takes a sentence as input, reverses the order of the words, and also reverses the letters within each word. The function should handle cases with multiple spaces between words, leading or trailing spaces, and special characters in the sentence, and it should not use any built-in functions or libraries that directly solve the problem.
"""

def reverse_sentence(sentence):
    # Initialize an empty list to store the reversed words
    reversed_words = []
    
    # Initialize variables to keep track of the start and end index of each word
    start = 0
    end = 0
    
    # Iterate through each character in the sentence
    for i in range(len(sentence)):
        # If a space is encountered, it means the end of a word
        if sentence[i] == ' ':
            # Extract the word from the sentence and reverse it
            word = sentence[start:end][::-1]
            
            # Append the reversed word to the list
            reversed_words.append(word)
            
            # Update the start and end index for the next word
            start = i + 1
            end = i + 1
        else:
            # If it's not a space, update the end index
            end += 1
    
    # Extract the last word from the sentence and reverse it
    word = sentence[start:end][::-1]
    
    # Append the reversed word to the list
    reversed_words.append(word)
    
    # Join the reversed words with spaces to form the reversed sentence
    reversed_sentence = ' '.join(reversed(reversed_words))
    
    # Return the reversed sentence
    return reversed_sentence