"""
QUESTION:
Write a function `check_isogram` to determine if a given string is an isogram (a word or phrase without a repeating letter), ignoring the case of the letters and disregarding special characters and spaces. The function should be efficient to handle large inputs. Additionally, create a function `print_all_isograms` to list and print all the isograms in a given sentence.
"""

def check_isogram(word):
    word = ''.join(e for e in word.lower() if e.isalnum()) 
    chars = set(word)
    return len(chars)==len(word)