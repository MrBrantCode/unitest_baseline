"""
QUESTION:
Write a function `letterCombinations(digits)` that returns all possible letter combinations that the number could represent. The function takes a string containing digits from `2-9` inclusive as input and returns the answer in any order. The function should use a mapping of digit to letters as follows: 
`'2': ['a', 'b', 'c']`, 
`'3': ['d', 'e', 'f']`, 
`'4': ['g', 'h', 'i']`, 
`'5': ['j', 'k', 'l']`, 
`'6': ['m', 'n', 'o']`, 
`'7': ['p', 'q', 'r', 's']`, 
`'8': ['t', 'u', 'v']`, 
`'9': ['w', 'x', 'y', 'z']`. The function should work for `0 <= digits.length <= 10` and `digits[i]` is a digit in the range `['2', '9']`.
"""

def letterCombinations(digits):
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
             
    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
                
    output = []
    backtrack("", digits)
    return output