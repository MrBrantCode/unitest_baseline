"""
QUESTION:
Write a function named `generate_latex_table` that takes a list of integers as input and returns a string representing a Latex table. The table should have three columns for the numerical value, its English worded form, and its French worded form. The input list should contain integers between 1 and 100. If the input list contains any invalid values, the corresponding table rows should display "Invalid input" for both English and French worded forms.
"""

def generate_latex_table(nums):
    table = '\\begin{tabular}{|c|c|c|}\n\\hline\nNumber & English & French\\\\\n\\hline\n'
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
            return num_words[tens] + '-' + num_words[ones]
        elif num == 100:
            return num_words[100]
        else:
            return ''
            
    for num in nums:
        if num < 1 or num > 100:
            table += '{} & Invalid input & Invalid input\\\\\n'.format(num)
        else:
            table += '{} & {} & {}\\\\\n'.format(num, num_to_words(num), num_to_words(num, 'french'))
    table += '\\hline\n\\end{tabular}'
    return table