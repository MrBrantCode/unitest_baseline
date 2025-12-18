"""
QUESTION:
Write a function `is_palindrome(word)` that determines if a given word is a palindrome using recursion without any built-in functions or libraries. The function should ignore non-alphanumeric characters and consider only alphanumeric characters in a case-insensitive manner.
"""

def entance(word):
    # 首先去掉所有非字母和数字的字符
    word = ''.join(filter(str.isalnum, word)).lower()
    # 若字長小於等於1，則為回文
    if len(word) <= 1:
        return True
    # 檢查首尾字母是否相同，如果不同，則不是回文
    elif word[0] != word[-1]:
        return False
    # 否則繼續檢查中間的字母是否回文
    else:
        return entance(word[1:-1])