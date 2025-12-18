"""
QUESTION:
Implement a function `compress_string(s)` that takes a string `s` as input and returns a compressed version of the string using Run-Length Encoding (RLE). The function should have a time complexity of O(n), where n is the length of the input string. The compressed string should represent each run of consecutive characters by the character itself followed by the count.
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