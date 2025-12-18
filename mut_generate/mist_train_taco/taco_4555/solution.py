"""
QUESTION:
Your task is to write a program which reads a text and prints two words. The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters.

The text includes only alphabetical characters and spaces. A word is a sequence of letters which is separated by the spaces.



Input

A text is given in a line. You can assume the following conditions:

* The number of letters in the text is less than or equal to 1000.
* The number of letters in a word is less than or equal to 32.
* There is only one word which is arise most frequently in given text.
* There is only one word which has the maximum number of letters in given text.

Output

The two words separated by a space.

Example

Input

Thank you for your mail and your lectures


Output

your lectures
"""

def find_most_frequent_and_longest_word(text: str) -> tuple:
    word_list = text.split(' ')
    word_dict = {}
    longest_word_len = 0
    longest_word = ''
    high_freq_word_num = 0
    high_freq_word = ''
    
    for word in word_list:
        if longest_word_len < len(word):
            longest_word_len = len(word)
            longest_word = word
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
        if high_freq_word_num < word_dict[word]:
            high_freq_word_num = word_dict[word]
            high_freq_word = word
    
    return high_freq_word, longest_word