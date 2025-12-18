"""
QUESTION:
Create a function named `find_anagrams` that takes in a list of words. The function should return a list of lists, where each sublist contains all possible anagrams of the corresponding word in the input list, sorted in alphabetical order. The function should have a time complexity of O(n*m*log(m)) and a space complexity of O(n*m), where n is the number of words in the input list and m is the average length of the words.
"""

def find_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    
    return [sorted(words) for words in anagram_dict.values()]