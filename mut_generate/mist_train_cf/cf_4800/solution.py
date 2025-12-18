"""
QUESTION:
Implement the `string_formatter` function to process an input string `s` as follows: split the string into a list of words, remove any duplicate words, and return the list of unique words in alphabetical order. The function should ignore any punctuation marks and consider words with different capitalizations as the same word. Implement a custom sorting and duplicate removal algorithm, not using built-in functions for sorting or duplicate removal. Ensure the solution has a time complexity of O(n log n) or better and uses minimal extra space. The function should only make a single pass over the input string.
"""

def string_formatter(s):
    words = []
    word = ''
    for char in s:
        if char.isalpha():
            word += char.lower()
        elif word:
            words.append(word)
            word = ''
    if word:
        words.append(word)

    # Remove duplicates
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Sort words alphabetically
    def merge_sort(words):
        if len(words) <= 1:
            return words
        mid = len(words) // 2
        left = merge_sort(words[:mid])
        right = merge_sort(words[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    return merge_sort(unique_words)