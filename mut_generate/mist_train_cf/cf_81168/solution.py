"""
QUESTION:
Write a function `maxScoreWords` that takes three parameters: `words` (a list of strings), `letters` (a list of single characters), and `score` (a list of integers representing the scores of each character from 'a' to 'z'). The function should return a tuple containing the maximum score that can be achieved by forming words from the given letters and the set of words that make up this maximum score.

Restrictions:

- Each word in `words` can be used at most once.
- Each character in `letters` can be used at most once.
- The length of `words` is between 1 and 14.
- The length of each word in `words` is between 1 and 15.
- The length of `letters` is between 1 and 100.
- The length of `score` is 26.
- All scores in `score` are between 0 and 10.
- All characters in `words` and `letters` are lowercase English letters.
"""

def maxScoreWords(words, letters, score):
    # compute the frequency of each letter
    freq = [0] * 26
    for ch in letters:
        freq[ord(ch) - ord('a')] += 1

    # compute the score of each word
    words_score = []
    for word in words:
        word_score, word_freq = 0, [0] * 26
        for ch in word:
            word_score += score[ord(ch) - ord('a')]
            word_freq[ord(ch) - ord('a')] += 1
        words_score.append((word_score, word_freq))

    # define the function to perform depth first search
    def dfs(index, curr_freq, curr_score, chosen_words):
        max_score = curr_score
        max_words = chosen_words[:]
        for i in range(index, len(words_score)):
            word_score, word_freq = words_score[i]
            # check if the word can be formed by the available letters
            if all(word_freq[j] <= curr_freq[j] for j in range(26)):
                new_freq = curr_freq[:]
                for j in range(26):
                    new_freq[j] -= word_freq[j]
                # make a recursive call to process the remaining words
                new_score, new_words = dfs(i + 1, new_freq, curr_score + word_score, chosen_words + [words[i]])
                if new_score > max_score:
                    max_score = new_score
                    max_words = new_words
        return max_score, max_words

    # search from the first word
    max_score, max_words = dfs(0, freq, 0, [])
    return (max_score, set(max_words))