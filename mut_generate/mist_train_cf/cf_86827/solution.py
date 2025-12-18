"""
QUESTION:
Create a function named `convert_integers_to_strings` that takes an array of up to 5000 integers as input. The function should convert each integer to a string based on its parity: even numbers should be converted to Roman numerals, and odd numbers should be converted to binary representation. Ignore negative integers and floating-point numbers should be rounded down to the nearest integer. The resulting array of strings should be sorted in descending order by length, then in ascending lexicographic order for strings of the same length. Remove duplicates, limit the array to 500 strings, and return the result as a comma-separated string. The time complexity of the function should be O(nlogn) or better.
"""

def convert_integers_to_strings(arr):
    def convert_to_roman(num):
        roman_map = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        result = ''
        
        for value, symbol in sorted(roman_map.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value
        
        return result

    def convert_to_binary(num):
        return bin(int(num))[2:]

    converted = []
    
    for num in arr:
        if num < 0:
            continue
        
        if num % 2 == 0:
            converted.append(convert_to_roman(num))
        else:
            converted.append(convert_to_binary(num))
    
    converted = list(set(converted))
    converted.sort(key=lambda x: (-len(x), x))
    
    if len(converted) > 500:
        converted = converted[:500]
    
    return ','.join(converted)