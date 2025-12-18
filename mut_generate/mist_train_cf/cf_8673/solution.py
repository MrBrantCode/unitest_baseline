"""
QUESTION:
Create a function called `capitalize_and_convert` that takes a sentence as input, capitalizes every word in the sentence, and converts words starting with a vowel to Pig Latin. The input sentence will consist of only lowercase letters, spaces, and numbers in the form of words, with a length not exceeding 100 characters and containing at least one word.
"""

def capitalize_and_convert(sentence):
    # Create a list of all the words in the sentence
    words = sentence.split()
    
    # Iterate over each word
    for i in range(len(words)):
        word = words[i]
        
        # Capitalize the first letter of the word
        capitalized_word = word.capitalize()
        
        # Check if the word starts with a vowel
        if capitalized_word[0] in ['A', 'E', 'I', 'O', 'U']:
            # Convert the word to Pig Latin
            pig_latin_word = capitalized_word[1:] + capitalized_word[0] + 'ay'
            words[i] = pig_latin_word
        else:
            words[i] = capitalized_word
    
    # Join the words back into a sentence
    capitalized_sentence = ' '.join(words)
    
    return capitalized_sentence