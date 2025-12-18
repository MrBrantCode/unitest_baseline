"""
QUESTION:
Develop a function named `longest_palindrome` that takes a string `s` as input and returns the longest palindromic substring. The function should ignore spaces and punctuation, and be case-insensitive. The function should also be able to identify palindromes formed by multiple words. The function should run in linear time complexity.
"""

def longest_palindrome(s):
    def process_string(s):
        # Remove spaces and punctuation from string, convert to lowercase
        s = ''.join(i.lower() for i in s if i.isalnum())
        return "^#" + "#".join(s) + "#$"

    string = process_string(s)
    P = [0] * len(string) 
    C = R = answerLength = answerCenter = 0

    for i in range(1, len(string) - 1):
        if R > i:
            iMirror = 2*C - i 
            P[i] = min(R - i, P[iMirror])
        else:
            P[i] = 0

        while string[i + 1 + P[i]] == string[i - 1 - P[i]]:
            P[i] += 1

        if i + P[i] > R:
            C = i
            R = i + P[i]
            if P[i] > answerLength:
                answerLength = P[i]
                answerCenter = i

    s = s.replace(" ", "")
    return s[(answerCenter - 1 - answerLength) // 2: (answerCenter - 1 + answerLength) // 2]