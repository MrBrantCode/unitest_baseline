"""
QUESTION:
Write a function `intToRoman(num)` that converts an integer `num` to a Roman numeral string. The function should take an integer as input and return a string. The input integer is assumed to be a positive integer between 1 and 3999. The function should use the standard Roman numeral symbols M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, and I.
"""

def intToRoman(num):
    val = [ 
            1000, 900, 500, 400, 
            100, 90, 50, 40, 
            10, 9, 5, 4, 
            1 
            ] 
    rom_num = [ 
                "M", "CM", "D", "CD", 
                "C", "XC", "L", "XL", 
                "X", "IX", "V", "IV", 
                "I"
                ] 
  
    res = "" 
    i = 0
    while num > 0: 
  
        # Find the greatest value smaller 
        # than the given number num 
        div = num // val[i] 
  
        # Update the number after each 
        # iteration 
        num = num % val[i] 
  
        # Concatenate the roman characters 
        # equal to the power value of div 
        while div > 0: 
            res = res + rom_num[i] 
            div = div - 1
        
        i = i + 1
  
    return res