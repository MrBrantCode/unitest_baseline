"""
QUESTION:
Create a function called `word_dic` that takes a list of words as input. The function should return a dictionary where each word in the list is a key, and its corresponding value is a list containing the length of the word, the number of vowels in the word, and the word spelled backwards. Treat the letter "y" as a consonant.
"""

def word_dic(word_list):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    result_dic = {}
    for word in word_list:
        reverse_word = word[::-1]
        length = len(word)
        vowels = sum([1 for char in word.lower() if char in vowel_list])
        result_dic[word] = [length, vowels, reverse_word]
    return result_dic