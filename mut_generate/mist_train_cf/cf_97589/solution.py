"""
QUESTION:
Replace Informal Words

Write a function named `replace_informal_words` that takes two parameters: a sentence and a dictionary of informal words with their corresponding replacements. The function should return the sentence with all informal words replaced with their alternatives. The function must handle any number of informal words in the dictionary.
"""

def replace_informal_words(sentence, informal_words):
 """
 Replace informal words in a given sentence with their alternatives.

 Parameters:
 sentence (str): The input sentence.
 informal_words (dict): A dictionary of informal words and their replacements.

 Returns:
 str: The sentence with all informal words replaced.
 """
 for word in informal_words:
  sentence = sentence.replace(word, informal_words[word])
 return sentence