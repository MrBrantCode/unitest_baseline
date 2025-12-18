"""
QUESTION:
Write a function `count_strings_formed(strings, words_lists)` that takes two parameters: a list of strings and a list of lists of words. The function should return the number of strings that can be formed by concatenating any number of words in the corresponding list. The function should return a count, not the actual strings or words.
"""

def count_strings_formed(strings, words_lists):
    count = 0
    for i in range(len(strings)):
        dp_arr = [0]*(len(strings[i])+1)
        dp_arr[0] = 1
        words = words_lists[i]
        for j in range(1, len(strings[i])+1):
            for word in words:
                if strings[i][:j].endswith(word):
                    dp_arr[j] += dp_arr[j-len(word)]
        if dp_arr[-1] != 0:
            count += 1
    
    return count