"""
QUESTION:
Write a function `letterCombinations` that takes a string of digits and returns all possible letter combinations that the number could represent using the following mapping:

2: ['a', 'b', 'c']
3: ['d', 'e', 'f']
4: ['g', 'h', 'i']
5: ['j', 'k', 'l']
6: ['m', 'n', 'o']
7: ['p', 'q', 'r', 's']
8: ['t', 'u', 'v']
9: ['w', 'x', 'y', 'z']

The order of the output does not matter. The function should use recursion.
"""

def letterCombinations(digits):
    dic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in dic[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output