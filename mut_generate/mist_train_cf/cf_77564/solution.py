"""
QUESTION:
Write a function `remove_superfluous_spaces` that takes a string `text` as input and returns a string with uniform spacing between words, considering punctuation marks as word separators and ensuring they are surrounded by spaces. The function must have a space complexity of O(1).
"""

def remove_superfluous_spaces(text: str) -> str:
    words = text.split()
    
    for i, word in enumerate(words):
       if word in [".", ","]:
          words[i] = " " + word
          
    return " ".join(words).replace(" .", ".").replace(" ,", ",")