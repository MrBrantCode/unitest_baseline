"""
QUESTION:
Create a function `repeat_string` that takes a string and an integer as parameters. The function should return the string repeated the absolute value of the specified integer times. If the integer is negative, the repeated string should be reversed. The function should handle strings containing special or unicode characters. The time complexity should be O(n), where n is the length of the string, and the space complexity should be O(1).
"""

def repeat_string(string, num_times):
    if num_times == 0:
        return ""
    
    result = ""
    for _ in range(abs(num_times)):
        result += string
    
    if num_times < 0:
        result = result[::-1]
    
    return result