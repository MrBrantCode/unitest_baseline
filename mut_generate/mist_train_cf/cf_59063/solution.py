"""
QUESTION:
Given a set of symbols and their frequencies, along with a lexicon of terms, write a function `solve(lexicon, symbols_freq)` that returns the length of the longest term that can be formed using the given symbols without exceeding their frequencies, and the number of distinct terms of that maximum length that can be created.
"""

from collections import Counter
import itertools

def solve(lexicon, symbols_freq):
    lexicon.sort(key=len, reverse=True)
    lexicon_set = set(lexicon)

    symbols_freq_list = list(symbols_freq.items())
    longest_term_length = 0
    longest_term_count = 0

    def recurse(index, remaining_freq_map, current_word):
        nonlocal longest_term_length, longest_term_count
        if index == len(symbols_freq_list):
            word = ''.join(current_word)
            if word in lexicon_set:
                if len(word) > longest_term_length:
                    longest_term_length = len(word)
                    longest_term_count = 1
                elif len(word) == longest_term_length:
                    longest_term_count += 1
        else:
            symbol, freq = symbols_freq_list[index]
            recurse(index + 1, remaining_freq_map, current_word)
            if remaining_freq_map[symbol] > 0:
                remaining_freq_map[symbol] -= 1
                current_word.append(symbol)
                recurse(index, remaining_freq_map, current_word)
                current_word.pop()
                remaining_freq_map[symbol] += 1

    recurse(0, Counter(symbols_freq), [])
    return longest_term_length, longest_term_count