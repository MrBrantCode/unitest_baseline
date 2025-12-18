"""
QUESTION:
Given a list of unique strings `words`, write a function `composite_words(words)` that returns all the composite words present in the list. A composite word is a string that is entirely composed of at least two shorter words from the provided array. The length of `words` array is between 1 and 104, the length of each string `words[i]` is between 0 and 1000, and `words[i]` is composed of only lowercase English alphabets. The total length of all strings in `words` is between 0 and 6 * 10^5.
"""

def composite_words(words):
    def search(word, index):
        if word in seen:
            return True
        for j in range(1, len(word)):
            prefix = word[:j]
            suffix = word[j:]
            if prefix in seen and (suffix in seen or search(suffix, index)):
                return True
        return False

    words.sort(key=lambda x: len(x))
    seen = set()
    result = []

    for i, word in enumerate(words):
        if search(word, i):
            result.append(word)
        seen.add(word)

    return result