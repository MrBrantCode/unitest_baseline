"""
QUESTION:
Write a function `findWords` that takes a list of words and returns the words that can be typed using only the letters present on a single row of the American keyboard. The function should return the words in the order of the keyboard rows they belong to, starting from the top row to the bottom row. The keyboard rows are defined as follows: the top row is composed of the characters `"qwertyuiop"`, the middle row is composed of the characters `"asdfghjkl"`, and the bottom row is composed of the characters `"zxcvbnm"`. The input list `words` has the following restrictions: `1 <= words.length <= 20` and `1 <= words[i].length <= 100`, where `words[i]` is composed of English alphabets (both lowercase and uppercase).
"""

def findWords(words):
    keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    row_wise_words = {index: [] for index in range(len(keyboard))}  
    for word in words:
        for index, row in enumerate(keyboard):
            if set(word.lower()) <= set(row):
                row_wise_words[index].append(word)
                break   # break when the row is found
    result = row_wise_words[0] + row_wise_words[1] + row_wise_words[2]
    return result