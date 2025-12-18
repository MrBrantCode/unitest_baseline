"""
QUESTION:
Write a function `solve_problem` that takes a string `s` and an integer `n` as input, splits `s` into words containing exactly `n` consonants, treats uppercase and lowercase letters as distinct, ignores spaces and special characters, and returns a dictionary with words as keys and their frequency as values in reverse order of their appearance. If `s` is empty, return an empty dictionary.
"""

def solve_problem(s, n):
    def count_consonants(word):
        return sum(1 for char in word if char.isalpha() and char.lower() in 'bcdfghjklmnpqrstvwxyz')

    words = s.split()
    filtered_words = [word for word in words if count_consonants(word) == n]
    result = {}
    for word in reversed(filtered_words):
        result[word] = filtered_words.count(word)
    return result