"""
QUESTION:
Create a function `repeat_string(string, num_times)` that repeats the input string `n` times, where `n` is the absolute value of the input integer `num_times`. The function should support special characters and Unicode characters. If `num_times` is negative, the function should return the reversed repeated string. The time complexity should be O(n), where n is the length of the string, and the space complexity should be O(1), excluding the space required for the output string.
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