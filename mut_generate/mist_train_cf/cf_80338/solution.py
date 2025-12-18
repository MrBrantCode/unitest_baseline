"""
QUESTION:
Write a recursive function named `print_words_in_reverse_order` that takes a list of sentences and an optional index parameter (default value is 0) and prints each word of every sentence in reverse order. The index parameter should be used to track the current sentence being processed in the list.
"""

def print_words_in_reverse_order(sentence_list, index = 0):
    # Base case: if the list is empty, return nothing
    if index == len(sentence_list):
        return
    else:
        # Split the sentence into words
        words = sentence_list[index].split()
        # Print the words in reverse order
        for word in reversed(words):
            print(word)
        # Move to next sentence in the list
        print_words_in_reverse_order(sentence_list, index + 1)