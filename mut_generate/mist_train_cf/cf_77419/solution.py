"""
QUESTION:
Implement a function called `case_preserve_replace` that takes three parameters: a string `s`, the old string `old`, and the new string `new`. The function should replace every occurrence of `old` in `s` with `new` while preserving the casing of the original text. The function should be efficient enough to handle large strings.
"""

def case_preserve_replace(s, old, new):
    # Split the string into words
    words = s.split(' ')
    replace_words = []

    # Check each word in the list
    for word in words:
        # Preserve the case while replacing
        if word.lower() == old.lower():
            new_word = ''.join([n.upper() if o.isupper() else n.lower() for o, n in zip(word, new)])
            new_word += new[len(word):]
            replace_words.append(new_word)
        else:
            replace_words.append(word)

    # Return the replaced string
    return ' '.join(replace_words)