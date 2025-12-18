"""
QUESTION:
Write a function named `punct_count` that counts and returns the total number of punctuation marks and the count of each type of punctuation mark in a given string. The function should consider the following punctuation marks: full stop (.), comma (,), exclamation mark (!), question mark (?), apostrophe ('), and semicolon (;). The function should be able to handle multiple input sentences. The output should be printed in a formatted way for better overview.
"""

def punct_count(sentence):
    punctuation = ['.',',','!','?',"'",';']
    total_counts = 0
    counts_dict = {}
    for punct in punctuation:
        punct_count = sentence.count(punct)
        total_counts += punct_count
        if punct_count > 0:
            counts_dict[punct] = punct_count
    return total_counts, counts_dict