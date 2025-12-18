"""
QUESTION:
Write a function `number_to_words(num)` that takes a positive integer up to 9999 and returns its word representation.
"""

def number_to_words(num):
    units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    thousands = ['', 'Thousand', 'Million', 'Billion']

    thousands_digit = (num // 1000) % 10
    hundreds_digit = (num // 100) % 10
    tens_digit = (num // 10) % 10
    units_digit = num % 10

    words = []
    if thousands_digit != 0:
        words.append(units[thousands_digit] + ' ' + thousands[1])
    if hundreds_digit != 0:
        words.append(units[hundreds_digit] + ' Hundred')
    if tens_digit != 0 or units_digit != 0:
        if tens_digit == 1 and units_digit != 0:
            words.append(teens[units_digit])
        else:
            words.append(tens[tens_digit])
            if units_digit != 0:
                words.append(units[units_digit])

    output = ' '.join(words)
    return output