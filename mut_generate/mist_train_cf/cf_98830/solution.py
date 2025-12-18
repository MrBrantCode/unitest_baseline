"""
QUESTION:
Write a function `generate_latex_table` that takes a list of integers as input and returns a string representing a Latex table. The table should have three columns: "Number", "English", and "French". Each row in the table corresponds to a number in the input list, and the "English" and "French" columns contain the worded forms of the number in the respective languages. If a number in the input list is outside the range 1-100, the corresponding row in the table should contain "Invalid input" in both the "English" and "French" columns. The function should be able to handle input lists with up to 1000 values.
"""

# Define dictionaries for English and French number words
english_num_words = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred'
}
french_num_words = {
    0: 'zéro', 1: 'un', 2: 'deux', 3: 'trois', 4: 'quatre', 5: 'cinq', 6: 'six', 7: 'sept', 8: 'huit', 9: 'neuf',
    10: 'dix', 11: 'onze', 12: 'douze', 13: 'treize', 14: 'quatorze', 15: 'quinze', 16: 'seize', 20: 'vingt',
    30: 'trente', 40: 'quarante', 50: 'cinquante', 60: 'soixante', 70: 'soixante-dix', 80: 'quatre-vingt',
    90: 'quatre-vingt-dix', 100: 'cent'
}

# Define a function to convert a number to its worded form
def num_to_words(num, lang='english'):
    if lang == 'english':
        num_words = english_num_words
    elif lang == 'french':
        num_words = french_num_words
    else:
        return ''
    
    if num in num_words:
        return num_words[num]
    elif num < 100:
        ones = num % 10
        tens = num - ones
        if tens == 0 and ones > 0:
            return num_words[ones]
        else:
            return num_words[tens] + '-' + num_words[ones]
    elif num == 100:
        return num_words[100]
    else:
        return ''

# Define a function to generate the Latex table
def generate_latex_table(nums):
    table = '\\begin{tabular}{|c|c|c|}\n\\hline\nNumber & English & French\\\\\n\\hline\n'
    for num in nums:
        if num < 1 or num > 100:
            table += '{} & Invalid input & Invalid input\\\\\n'.format(num)
        else:
            table += '{} & {} & {}\\\\\n'.format(num, num_to_words(num), num_to_words(num, 'french'))
    table += '\\hline\n\\end{tabular}'
    return table