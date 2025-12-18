"""
QUESTION:
Implement the function `count_korean_words(input_string)` that takes a string as input and returns a dictionary where the keys are the unique Korean words found in the input string, and the values are the counts of each word's occurrences. A Korean word is defined as a sequence of Hangul syllables (characters) surrounded by spaces or at the beginning/end of the string. Punctuation marks and numbers should be ignored.
"""

def entrance(input_string: str) -> dict:
    korean_words = {}
    words = input_string.split()
    for word in words:
        # Remove punctuation and numbers
        word = ''.join(filter(lambda x: '가' <= x <= '힣', word))
        if word:
            korean_words[word] = korean_words.get(word, 0) + 1
    return korean_words