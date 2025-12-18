"""
QUESTION:
Write a function `reverse_sentence` that takes a string `sentence` as input, reverses the order of the words in the sentence, and also reverses the letters within each word. The function should handle cases with multiple spaces between words, leading or trailing spaces, and special characters. The function should not use any built-in functions or libraries that directly solve the problem.
"""

def reverse_sentence(sentence):
    reversed_words = []
    start = 0
    end = 0
    
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            word = sentence[start:end][::-1]
            reversed_words.append(word)
            start = i + 1
            end = i + 1
        else:
            end += 1
    
    word = sentence[start:end][::-1]
    reversed_words.append(word)
    
    reversed_sentence = ' '.join(reversed_words[::-1])
    return reversed_sentence