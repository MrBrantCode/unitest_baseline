"""
QUESTION:
Implement the function `reverse_words(sentence)` that takes a string as input, splits it into words, reverses the order of the words, and also reverses each word individually. You cannot use any built-in string or array reversal methods. The function should return the resulting string, preserving original punctuation and capitalization, and without any leading or trailing spaces.
"""

def reverse_words(sentence):
  # Split the words by spaces
  words = sentence.split(' ')

  # Initialize an empty list to store the reversed words
  reversed_words = []

  # Reverse each word manually and store it in the reversed_words list
  for word in words:
    reversed_word = ''
    for char in word:
      reversed_word = char + reversed_word
    reversed_words.append(reversed_word)

  # Initialize an empty string to store the reversed sentence
  reversed_sentence = ''

  # Concatenate the reversed words in reverse order
  for i in range(len(reversed_words)):
    reversed_sentence = reversed_words[-i-1] + ' ' + reversed_sentence

  return reversed_sentence.strip()