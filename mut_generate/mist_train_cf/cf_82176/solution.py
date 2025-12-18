"""
QUESTION:
Write a function named `compare_sentences` that takes two lists of sentences as input and returns a dictionary. The dictionary should contain characters that appear in the same positions within corresponding sentences in both lists, along with their respective total counts across all pairs. The function should consider case sensitivity and punctuation, and ignore extra sentences in the longer list if the two lists are of unequal length.
"""

from collections import defaultdict

def compare_sentences(list1, list2):
    result = defaultdict(int)
    # length of the shorter list
    min_len = min(len(list1), len(list2))
    
    for i in range(min_len):
        sentence1 = list1[i]
        sentence2 = list2[i]
        # iterate over each character in corresponding sentences
        for j in range(min(len(sentence1), len(sentence2))):
            if sentence1[j] == sentence2[j]:
                result[sentence1[j]] += 1
                
    # return result as a normal dict
    return dict(result)