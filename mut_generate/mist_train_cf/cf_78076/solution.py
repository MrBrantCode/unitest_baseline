"""
QUESTION:
Create a function named `multiplication_table(n)` that prints a Roman numeral multiplication table up to the given number `n`. The function should take an integer `n` as input and print the multiplication table with the multiplicand and multiplier, as well as their product, all represented as Roman numerals.
"""

def entrance(n):
    def int_to_roman(input):
        if isinstance(input, type(1)):
            num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
            syb = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
            roman_num = ''
            i = 12
            while input:
                div = input // num[i]
                input %= num[i]
                while div:
                    roman_num += syb[i]
                    div -= 1
                i -= 1
            return roman_num
        else:
            print("Not a valid number")
        
    for i in range(1, n+1):
        for j in range(1, n+1):
            product = int_to_roman(i*j)
            print(f'{int_to_roman(i)} times {int_to_roman(j)} equals {product}')