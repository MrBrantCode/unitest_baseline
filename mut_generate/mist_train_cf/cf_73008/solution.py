"""
QUESTION:
Write a function named `validWordSquare` that takes a list of strings `words` as input and returns a boolean value indicating whether the sequence of words forms a valid word square and a palindrome. The word square is valid if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns), and the sequence of words is the same read forwards and backwards. The input list `words` contains at least 1 and at most 500 words, each containing only lowercase English alphabet `a-z` and having a length between 1 and 500.
"""

def is_valid_word_square(words):
    # Check if words sequence forms a valid word square
    for i in range(len(words)):
        for j in range(len(words[i])):
            try:
                if words[i][j] != words[j][i]:
                    return False
            except IndexError:
                return False

    # Check if words sequence forms a palindrome
    if words != list(map(list,zip(*words[::-1]))):
        return False

    return True