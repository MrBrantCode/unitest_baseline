"""
QUESTION:
Implement a function named `compress_string` that compresses the input string using the Run-Length Encoding (RLE) algorithm. The function should have a time complexity of O(n), where n is the length of the input string. The function should take a string as input and return a string where each run of consecutive characters is represented by the character itself followed by the count.
"""

def compress_string(s):
    compressed = ""
    count = 1
    
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i+1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1
    
    return compressed