"""
QUESTION:
Create a program with two functions, `format_number(n)` and `original_number(formatted_num)`, to format and unformat a given numerical figure for enhanced readability. The `format_number(n)` function should add commas after every three digits from the right, handling negative numbers and decimal points accurately. The `original_number(formatted_num)` function should remove the commas from the formatted number to retrieve its original format. The program should be scalable and efficient, handling significantly large numbers without noticeable performance decrease. The input `n` and `formatted_num` are strings, and the output should be a string. Ensure the program accounts for potential issues such as loss of precision when dealing with very large decimal numbers.
"""

def format_number(n):
    try:
        float_n = float(n)
        if '.' in n:
            int_part, dec_part = n.split('.')
            return '{:,}'.format(int(float_n)) + '.' + dec_part
        else:
            return '{:,}'.format(int(n))
    except ValueError:
        return "Invalid Input"

def original_number(formatted_num):
    return formatted_num.replace(',','')