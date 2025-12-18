"""
QUESTION:
Given a set of keywords `words` and a string `S`, create a function `boldWords` to make all appearances of all keywords in `S` bold by wrapping them in `<b>` and `</b>` tags. The returned string should use the least number of tags possible and handle both overlapping and non-overlapping segments of keywords in `S`. The function should take `words` and `S` as input and return the processed string. The length of `words` is in range `[0, 50]`, the length of each word is in range `[1, 10]`, and the length of `S` is in range `[0, 500]`. All characters in `words` and `S` are lowercase letters.
"""

def boldWords(words, S):
    mask = [0] * len(S)
    for word in words:
        start = S.find(word)
        while start != -1:
            mask[start:start+len(word)] = [1]*len(word)
            start = S.find(word, start + 1)
        
    output = []
    for i in range(len(S)):
        if mask[i] and (i == 0 or not mask[i-1]):
            output.append("<b>")
        output.append(S[i])
        if mask[i] and (i == len(S)-1 or not mask[i+1]):
            output.append("</b>")
    return "".join(output)