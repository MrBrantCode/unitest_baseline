"""
QUESTION:
Create a function called `advanced_dict_sort` that takes a dictionary of words and their frequencies as input and returns a sorted list of words. The function should filter out words with prime number frequencies and sort the remaining words based on their frequencies in ascending order. In cases where frequencies are identical, sort the words alphabetically in ascending order, ignoring case sensitivity. The function should also accept an optional boolean argument `reverse` to switch the sort order from ascending to descending, defaulting to `False`. The input dictionary should only contain string keys (words) and integer values (frequencies).
"""

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def advanced_dict_sort(words_frequencies, reverse=False):
    words_frequencies = {word: freq for word, freq in words_frequencies.items() if not is_prime(freq)}
    sorted_words = sorted(words_frequencies.items(), key=lambda x: (x[1], x[0].lower()), reverse=reverse)
    return [word for word, freq in sorted_words]