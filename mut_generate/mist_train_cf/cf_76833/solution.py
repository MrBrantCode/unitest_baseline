"""
QUESTION:
Implement a function `lex_sort(words)` that takes a list of words as input. Sort the words in lexicographical order, but if a word begins with a vowel, sort those words in reverse lexicographical order. The solution should not use any built-in sort functions. The vowels are 'a', 'e', 'i', 'o', 'u'.
"""

def lex_sort(words):
    # Separate words to two lists depending whether it starts with vowel or not
    vowels = [word for word in words if word[0].lower() in 'aeiou']
    others = [word for word in words if word[0].lower() not in 'aeiou']

    # Bubble sort for words starting with vowels
    for passnum in range(len(vowels)-1, 0, -1):
        for i in range(passnum):
            if vowels[i] < vowels[i+1]:
                temp = vowels[i]
                vowels[i] = vowels[i+1]
                vowels[i+1] = temp

    # Bubble sort for other words
    for passnum in range(len(others)-1, 0, -1):
        for i in range(passnum):
            if others[i] > others[i+1]:
                temp = others[i]
                others[i] = others[i+1]
                others[i+1] = temp  

    # Concatenate both lists
    sorted_list = others + vowels
    return sorted_list