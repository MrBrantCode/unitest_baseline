"""
QUESTION:
Write a function `rearrange_word(word)` that rearranges the input string in alphabetical order in chunks of 5 consecutive characters, and then reverses the order of every alternate chunk.
"""

def rearrange_word(word):
    chunks = [sorted(word[i:i+5]) for i in range(0, len(word), 5)]
    for i in range(len(chunks)):
        if i % 2 != 0:
            chunks[i] = chunks[i][::-1]
    return ''.join([''.join(chunk) for chunk in chunks])