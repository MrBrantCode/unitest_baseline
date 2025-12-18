"""
QUESTION:
Reorder the words in a given sentence to match the order of their first occurrence in a provided dictionary. Write a function `reorder_sentence` that takes two parameters: `dictionary_order` and `sentence_to_rearrange`, and returns the reordered sentence as a string. The function should ignore case sensitivity and assume all words in the sentence appear in the dictionary.
"""

def reorder_sentence(dictionary_order, sentence_to_rearrange):
    # Convert dictionary and sentence to lowercase and split into list
    dict_list = dictionary_order.lower().split(" ")
    sentence_list = sentence_to_rearrange.lower().split(" ")
    
    # Sort the sentence list based on the dictionary list
    sorted_sentence = sorted(sentence_list, key=dict_list.index)
    
    # Join the sorted sentence to create a string
    sorted_sentence_str = " ".join(sorted_sentence)
    
    return sorted_sentence_str