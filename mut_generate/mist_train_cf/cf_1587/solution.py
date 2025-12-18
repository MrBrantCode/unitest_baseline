"""
QUESTION:
Given a string `s` containing only lowercase letters, write a function `count_unique_three_letter_words(s)` that counts the number of unique three-letter words in the string. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), excluding the space needed for the input and output.
"""

def count_unique_three_letter_words(s):
    count = 0
    visited = [False] * (26 * 26 * 26)
    for i in range(len(s) - 2):
        word = s[i:i+3]
        index = (ord(word[0]) - ord('a')) * 26 * 26 + (ord(word[1]) - ord('a')) * 26 + (ord(word[2]) - ord('a'))
        if not visited[index]:
            count += 1
            visited[index] = True
    return count