"""
QUESTION:
Create a function named `sort_string` that takes a list of strings as input, and returns a list of tuples where the first element of each tuple is the original string and the second element is its length. The list of tuples should be sorted in descending order by the string lengths.
"""

def sort_string(word_list):
  dictionary = dict()
  for word in word_list:
    dictionary[word] = len(word)
  sorted_dict = sorted(dictionary.items(), key = lambda x: x[1], reverse = True)
  return sorted_dict 