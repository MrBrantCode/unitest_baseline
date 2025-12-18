"""
QUESTION:
Implement the function `reverseOnlyLetters(S)` that takes a string `S` as input, where `S` contains at least one letter and one number, `S.length <= 100`, and `33 <= S[i].ASCIIcode <= 122`. The function should return the "reversed" string where all characters that are not a letter or a number stay in the same place, and all letters and numbers reverse their positions separately.
"""

def reverseOnlyLetters(S):
    S = list(S)
    letters = [char for char in S if char.isalpha()]
    digits = [char for char in S if char.isdigit()]
    
    letters.reverse()
    digits.reverse()

    letter_index, digit_index = 0, 0
    
    for i in range(len(S)):
        if S[i].isalpha():
            S[i] = letters[letter_index]
            letter_index += 1
        elif S[i].isdigit():
            S[i] = digits[digit_index]
            digit_index += 1

    return "".join(S)