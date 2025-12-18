"""
QUESTION:
Given a screen with dimensions `rows x cols` and a sentence represented by a list of non-empty words, write a function `screen_fit(sentence, rows, cols)` to determine the number of times the provided sentence can be accommodated on the screen. A word cannot be split across two lines, the sequence of words in the sentence must remain unaltered, and there must be a single space separating two consecutive words in a line. The total number of words in the sentence will not exceed 100, the length of each word will be greater than 0 and will not exceed 10, and the values for rows and cols will be within the range of 1 ≤ rows, cols ≤ 20,000.
"""

def screen_fit(sentence, rows, cols):
    s = ' '.join(sentence) + ' '
    start, l = 0, len(s)
    fit_array = [0]*l
    for i in range(1, l):
        if s[i] == ' ':
            fit_array[i] = 1
        else:
            fit_array[i] = fit_array[i-1]
        if s[i] != ' ' and s[i-1] == ' ':
            fit_array[i] -= 1
      
    for _ in range(rows):
        start += cols
        if s[start%l] == ' ':
            start += 1
        elif s[(start-1)%l] != ' ':
            while start > 0 and s[(start-1)%l] != ' ':
                start -= 1

    return (start // l)