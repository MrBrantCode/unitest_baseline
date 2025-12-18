"""
QUESTION:
Write a function to convert a given number into words.
Example 1:
Input:
N = 438237764
Output: forty three crore eighty two lakh 
thirty seven thousand seven hundred and 
sixty four
 
Example 2:
Input:
N = 1000
Output: one thousand
Your Task:
You don't need to read input or print anything. Your task is to complete the function convertToWords() which takes the integer n as input parameters and returns a string containing n in words.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{9} - 1
"""

def convert_number_to_words(n: int) -> str:
    one = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']
    ten = ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']

    def num_to_words(n: int, s: str) -> str:
        str_out = ''
        if n > 19:
            str_out += ten[n // 10] + one[n % 10]
        else:
            str_out += one[n]
        if n:
            str_out += s
        return str_out

    output = ''
    output += num_to_words(n // 10000000, 'crore ')
    output += num_to_words(n // 100000 % 100, 'lakh ')
    output += num_to_words(n // 1000 % 100, 'thousand ')
    output += num_to_words(n // 100 % 10, 'hundred ')
    if n > 100 and n % 100:
        output += 'and '
    output += num_to_words(n % 100, '')
    return output.strip()