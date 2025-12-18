"""
QUESTION:
Write a function `convertRomanToInteger` to convert a valid Roman numeral string to an integer value. The Roman numeral string will be in uppercase, have a maximum length of 15, and follow the standard Roman numeral rules, including rules for subtraction and repetition. The function should return the integer value of the Roman numeral or an error message if the input is invalid.
"""

def convertRomanToInteger(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    max_counts = {
        'I': 3,
        'V': 1,
        'X': 3,
        'L': 1,
        'C': 3,
        'D': 1,
        'M': 3
    }
    
    num = 0
    count = {symbol: 0 for symbol in roman_values}
    
    for i in range(len(s)):
        curr = roman_values[s[i]]
        if i < len(s) - 1 and curr < roman_values[s[i+1]]:
            next = roman_values[s[i+1]]
            if next > curr * 10:
                return "Error: Invalid Roman numeral"
            num -= curr
        else:
            num += curr
        
        count[s[i]] += 1
        if count[s[i]] > max_counts[s[i]]:
            return "Error: Invalid Roman numeral"
        
    return num