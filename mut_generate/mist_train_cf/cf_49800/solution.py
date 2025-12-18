"""
QUESTION:
Write a function `reconstruct_digits(s)` that takes a string `s` as input and returns a string and a dictionary. The string `s` contains letters from 0-9 digits. The function should return the digits in the order of their appearance in the string and a dictionary where the keys are the digits and the values are their frequencies. The function should ignore any characters in the string that are not digits. The function should handle the cases where a letter appears in multiple digits, such as 'o' appears in 'one', 'zero', and 'two'.
"""

def reconstruct_digits(s):
    count = [0]*10
    for letter in s:
        if letter == 'z': count[0] += 1
        if letter == 'w': count[2] += 1
        if letter == 'u': count[4] += 1
        if letter == 'x': count[6] += 1
        if letter == 'g': count[8] += 1
        if letter == 'o': count[1] += 1  
        if letter == 'h': count[3] += 1  
        if letter == 'f': count[5] += 1  
        if letter == 's': count[7] += 1  
        if letter == 'i': count[9] += 1  

    count[1] -= count[0] + count[2] + count[4]
    count[3] -= count[8]
    count[5] -= count[4]
    count[7] -= count[6]
    count[9] -= count[5] + count[6] + count[8]

    output = ''
    freq = {}
    for i in range(10):
        if count[i] > 0:
            output += str(i)*count[i]
            freq[i] = count[i]

    return output, freq