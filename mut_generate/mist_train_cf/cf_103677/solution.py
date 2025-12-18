"""
QUESTION:
Implement the `convert_number` function to return a string representation of an integer based on its value. If the integer is negative, return "negative". If it is zero, return "zero". For non-negative integers, use a conversion function based on the number of digits (1-9, 10-99, 100-999, etc.). If the integer has more than three digits, return "out of range". The function should handle a larger range of input values efficiently.
"""

def convert_number(i):
    def convert_single_digit(i):
        return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][i]

    def convert_double_digit(i):
        if i < 20:
            return ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][i-10]
        tens, ones = divmod(i, 10)
        return ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][tens-2] + (" " + convert_single_digit(ones) if ones else "")

    def convert_triple_digit(i):
        hundreds, rest = divmod(i, 100)
        if rest == 0:
            return ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"][hundreds-1]
        return ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"][hundreds-1] + " " + (convert_double_digit(rest) if rest >= 10 else convert_single_digit(rest))

    if i < 0:
        return "negative"
    elif i == 0:
        return "zero"
    elif i < 10:
        return convert_single_digit(i)
    elif i < 100:
        return convert_double_digit(i)
    elif i < 1000:
        return convert_triple_digit(i)
    else:
        return "out of range"