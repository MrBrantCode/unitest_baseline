"""
QUESTION:
Create a function called `create_dict` that takes a string of text as input and returns a dictionary where the keys are the unique words in the text and the values are the corresponding word frequencies. The function should be case-sensitive and consider 'dogs' and 'Dogs' as two different words. There should be no restriction on the size of the input string.
"""

def create_dict(text):
  text_list = text.split(' ')
  count_dict = {}
  for word in text_list:
    count_dict[word] = count_dict.get(word, 0) + 1
  return count_dict