"""
QUESTION:
Create a function `reverse_word(word)` that takes a string `word` as input. The function should reverse the input string and count the total number of vowels in the reversed string, considering only lowercase vowels 'a', 'e', 'i', 'o', 'u'. The function should return the total number of letters in the input string, the reversed string, and the total number of vowels in the reversed string. The input string may contain spaces, punctuation, and uppercase letters.
"""

def reverse_word(word):
    word = list(word)
    reversed_word = ['']*len(word)
    count = 0

    for i in range(len(word)):
        reversed_word[i] = word[-1-i]
        if reversed_word[i] in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    reversed_word = "".join(reversed_word)
    return len(word), reversed_word, count