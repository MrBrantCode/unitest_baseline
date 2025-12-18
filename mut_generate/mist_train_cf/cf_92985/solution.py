"""
QUESTION:
Create a function named `find_most_frequent_word` that takes a sentence as input and returns the most frequent word in the sentence. The sentence is case sensitive and words are separated by a single space. The function should not use any built-in functions or libraries for string manipulation or counting occurrences. If there are multiple words with the same highest frequency, the function can return any of them.
"""

def find_most_frequent_word(sentence):
    words = []
    current_word = ""
    
    for char in sentence:
        if char == " ":
            words.append(current_word)
            current_word = ""
        else:
            current_word += char
    
    words.append(current_word)  # Add the last word
    
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    most_frequent_word = ""
    highest_count = 0
    
    for word, count in word_counts.items():
        if count > highest_count:
            most_frequent_word = word
            highest_count = count
    
    return most_frequent_word