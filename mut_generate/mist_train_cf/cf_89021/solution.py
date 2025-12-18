"""
QUESTION:
Write a function `convertToHex(num)` that converts a given non-negative integer to its equivalent hexadecimal value using recursion. The function should handle the case where `num` is 0 by returning '0'. If `num` is negative, it should print "Error: Invalid input!" and end the program. The function should use a dictionary to map decimal values to their equivalent hexadecimal characters.
"""

def convertToHex(num):
    hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    if not isinstance(num, int) or num < 0:
        print("Error: Invalid input!")
        exit()
    
    if num == 0:
        return '0'
    
    remainder = num % 16
    remainder = hex_map[remainder] if remainder > 9 else str(remainder)
    
    return convertToHex(num // 16) + remainder