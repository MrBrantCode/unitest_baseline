"""
QUESTION:
Write a function `rearrange_sentence(sentence, lexicon)` that takes a sentence string and a list of words (lexicon) as input, and returns a rearranged sentence string where the words appear in the order of their first occurrence in the lexicon. The function should handle sentences of variable lengths and a lexicon of up to 10,000 words, and it should be optimized to handle possible duplicate words within the input string and the lexicon.
"""

def rearrange_sentence(sentence, lexicon):
    # Split the sentence string into a list of words
    sentence = sentence.split(" ") 
    
    # Prepare a map of words to their corresponding indices in the lexicon.
    word_index_map = {word: index for index, word in enumerate(lexicon)}
    
    # Filter the sentence words that exist in the lexicon.
    sentence = [word for word in sentence if word in word_index_map]
    
    # Sort the sentence words based on their indices in the lexicon.
    sentence.sort(key=lambda word: word_index_map[word])
    
    # Join the sorted words to obtain the rearranged sentence.
    rearranged_sentence = " ".join(sentence)
    
    return rearranged_sentence