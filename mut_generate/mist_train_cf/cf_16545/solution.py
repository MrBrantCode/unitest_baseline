"""
QUESTION:
Write a function `count_unique_three_letter_words(string)` that takes a string as input and returns the number of unique three-letter words in the string, ignoring case and non-alphabetic characters. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def count_unique_three_letter_words(string):
    count = 0
    visited = [False] * 26 * 26 * 26

    string = string.lower()
    for i in range(len(string) - 2):
        if not string[i].isalpha() or not string[i+1].isalpha() or not string[i+2].isalpha():
            continue

        word = string[i:i+3]
        index = (ord(word[0]) - ord('a')) * 26 * 26 + (ord(word[1]) - ord('a')) * 26 + (ord(word[2]) - ord('a'))

        if not visited[index]:
            count += 1
            visited[index] = True

    return count