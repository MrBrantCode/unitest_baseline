"""
QUESTION:
Evaluate the function `evaluate(s, knowledge)` which takes two parameters: a string `s` and a 2D string array `knowledge` where each `knowledge[i] = [keyi, valuei]`. The function replaces all bracket pairs in `s` with the corresponding values from `knowledge` and replaces unknown keys with a question mark `?`. Assume that each key appears at most once in `knowledge`, there are no nested brackets in `s`, and every open bracket has a corresponding close bracket. Return the resulting string after evaluating all bracket pairs.

Constraints: `1 <= s.length <= 10^5`, `0 <= knowledge.length <= 10^5`, `1 <= keyi.length, valuei.length <= 10`, `s` consists of lowercase English letters and round brackets, and `keyi` and `valuei` consist of lowercase English letters.
"""

def evaluate(s, knowledge):
    k_dict = {k: v for k, v in knowledge}
    i, n, result = 0, len(s), ""
    while i < n:
        if s[i] == '(':
            j = i
            while s[j] != ')':
                j += 1
            key = s[i+1:j]
            result += k_dict.get(key, '?')
            i = j + 1
        else:
            result += s[i]
            i += 1
    return result