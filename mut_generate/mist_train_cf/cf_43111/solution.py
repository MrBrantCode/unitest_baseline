"""
QUESTION:
Write a function `replace_nth_word(sentence, target_word, replacement_word, n)` that takes four parameters: the input string `sentence`, a word `target_word`, a word `replacement_word`, and an integer `n`. The function should replace the nth occurrence of `target_word` in the `sentence` with `replacement_word` and return the modified sentence. If the `target_word` does not occur n times in the `sentence`, the function should return the original sentence.
"""

def replace_nth_word(sentence, target_word, replacement_word, n):
    words = sentence.split()
    count = 0
    for i, word in enumerate(words):
        if word == target_word:
            count += 1
            if count == n:
                words[i] = replacement_word
                return ' '.join(words)
    return sentence