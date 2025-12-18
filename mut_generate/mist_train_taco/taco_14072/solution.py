"""
QUESTION:
In this kata you must take an input string, reverse the order of the words, and reverse the order of the letters within the words.

But, as a bonus, every test input will end with a punctuation mark (! ? .) and the output should be returned with the mark at the end.

A few examples should help clarify:

```python
esrever("hello world.") == "dlrow olleh."

esrever("Much l33t?") == "t33l hcuM?"

esrever("tacocat!") == "tacocat!"
```

Quick Note: A string will always be passed in (though it may be empty) so no need for error-checking other types.
"""

def reverse_words_and_letters(s):
    if not s:
        return ''
    punctuation_mark = s[-1]
    reversed_string = s[:-1][::-1]
    return reversed_string + punctuation_mark