"""
QUESTION:
Write a function `count_sentences(s)` that takes a string `s` as input and returns the count of sentences contained within that string. The function should assume that sentences are separated by full stops ('.'). However, the full stops within abbreviations or decimal numbers should not be considered as sentence endings. The function should raise an error if the input is not a string.
"""

import re

def count_sentences(s):
    """Develop a function named 'count_sentences', that takes a string as an input,
    and returns the count of sentences contained within that string. The function should assume that 
    sentences are separated by full stops ('.'). However, the full stops within abbreviations or decimal 
    numbers should not be considered as sentence endings.
    """
    
    try:
      # Using regular expressions to count the number of sentences in a string.
      # Ignore abbreviations or decimal numbers during counting.
      count = len(re.findall(r"[A-Z][^.!?]*[.!?]", s, re.IGNORECASE))
    except TypeError as e:
      # Catching & handling the error if the input is not a string.
      print(f"TypeError: {e}")
      print("The input provided should be a string. Please provide a string input and try again.")
    except Exception as e:
      # Handle other types of exceptions.
      print(f"An error occurred: {e}")
    else:
      # If no exception is raised, then it returns the count of sentences.
      return count