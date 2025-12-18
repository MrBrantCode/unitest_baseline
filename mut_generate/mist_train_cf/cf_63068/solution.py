"""
QUESTION:
Write a function `reverse_every_second_word` that takes a string `s` as input and returns a new string where every second word is reversed. The function should not use any inbuilt Python functions or modules to reverse the words. The time complexity of the solution should be better than O(n²).
"""

def reverse_every_second_word(s):
    def reverse_string(word):
        result = ""
        for character in word:
            result = character + result
        return result

    words = s.split(' ')
    for i in range(1, len(words), 2):
        words[i] = reverse_string(words[i])
    return ' '.join(words)