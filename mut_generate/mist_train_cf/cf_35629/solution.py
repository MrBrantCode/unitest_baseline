"""
QUESTION:
Implement a function `int_to_polish_word(num: int) -> str` that takes an integer `num` as input and returns its Polish word representation. The function should support integers in the range from 0 to 999.
"""

def int_to_polish_word(num: int) -> str:
    ones = ["", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
    teens = ["", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
    tens = ["", "dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
    hundreds = ["", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset", "osiemset", "dziewięćset"]

    if num == 0:
        return "zero"

    result = ""
    if num // 100 > 0:
        result += hundreds[num // 100] + " "
        num %= 100
    if num // 10 > 1:
        result += tens[num // 10] + " "
        num %= 10
    if num // 10 == 1:
        result += teens[num % 10] + " "
        num = 0
    if num > 0:
        result += ones[num] + " "

    return result.strip()