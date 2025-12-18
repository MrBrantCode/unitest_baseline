"""
QUESTION:
Write a function `reverse_sentence` that takes a string as input, reverses the order of the words in the string, and also reverses each individual word within the string. The function should handle punctuation correctly by keeping it attached to the word it is associated with.
"""

def reverse_sentence(sentence):
    ##
    # Utility function to reverse individual words
    # Handles punctuation correctly.
    ##
    def reverse_word(word):
        # creating list of punctuation characters
        punctuation = [' ','.','!',':',';','?','-','–','(',')']
        rev_word = ''
        for i in range(len(word)):
            if word[i] not in punctuation:
                rev_word = word[i] + rev_word
            else:
                rev_word = word[i] + rev_word + word[i+1:]
                break
        return rev_word

    words = sentence.split(' ')
    rev_sentence = ' '.join(word for word in words[::-1])
    words = rev_sentence.split(' ')
    rev_words = [reverse_word(word) for word in words]
    return ' '.join(word for word in rev_words)