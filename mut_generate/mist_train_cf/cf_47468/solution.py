"""
QUESTION:
Create a function named `find_word` that takes a 2D array `matrix` and a word `word` as inputs. The function should return the index location of the first occurrence of the word in the matrix in the form of row and column. The word should be searched in the lowercase version of the matrix, and it can be split across multiple elements in the same row but not across different rows or columns. If the word is not found, the function should return -1.
"""

def find_word(matrix, word):
    word = word.lower()
    for i in range(len(matrix)):
        string = ''.join(matrix[i]).lower()
        if word in string:
            return i, string.find(word)
    return -1