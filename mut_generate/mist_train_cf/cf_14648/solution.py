"""
QUESTION:
Write a function called `find_anagram_pairs` that takes a list of English words as input and returns a list of pairs of words that are anagrams of each other. The function should consider only pairs of words that exist in the input list.
"""

def find_anagram_pairs(word_list):
    anagram_pairs = []
    word_dict = {}
    
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]
            
    for words in word_dict.values():
        if len(words) > 1:
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    anagram_pairs.append((words[i], words[j]))
                    
    return anagram_pairs