"""
QUESTION:
Develop a function `longest_subsequence(word)` that identifies if a word solely consists of consonants and determines the longest subsequence of consonants within the word. The function should return the length of the longest subsequence and its starting and ending indices.
"""

def longest_subsequence(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_length = 0
    start = 0
    end = 0
    current_length = 0
    current_start = 0

    for i in range(len(word)):
        if word[i].lower() not in vowels:
            if current_length == 0:
                current_start = i
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                start = current_start
                end = i
        else:
            current_length = 0

    # If the word only consists of consonants
    if max_length == len(word):
        print('The word solely consists of consonants.')
        return max_length, start, end

    print('The longest subsequence of consonants is from index', start, 'to', end, '.')
    return max_length, start, end