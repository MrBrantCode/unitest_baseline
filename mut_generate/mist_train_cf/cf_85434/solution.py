"""
QUESTION:
Write a function `numSmallerByFrequency(queries, words)` where `queries` and `words` are arrays of strings. The function should return an array `answer` where `answer[i]` is the number of words in `words` where the frequency of the lexicographically smallest character in `queries[i]` is less than the frequency of the lexicographically smallest character in each word in `words`.

The function should work under the following constraints:
- `1 <= queries.length, words.length <= 2000`
- `1 <= queries[i].length, words[i].length <= 10`
- `queries[i][j], words[i][j]` consist of lowercase English alphabets.
"""

def numSmallerByFrequency(queries, words):
    def f(s):
        return s.count(min(s))

    f_words = sorted([f(word) for word in words])

    return [len(f_words) - next((i for i, x in enumerate(f_words) if x > f(query)), len(f_words)) for query in queries]