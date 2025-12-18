"""
QUESTION:
Write a function `reconstruct_digits(s)` that takes a string `s` representing an unordered English depiction of digits ranging from 0-9 and returns a tuple containing a string of digits in ascending order and a dictionary representing the frequency of each digit present in the string. The string `s` has a length between 1 and 105 and only contains the characters 'e', 'g', 'f', 'i', 'h', 'o', 'n', 's', 'r', 'u', 't', 'w', 'v', 'x', and 'z'.
"""

def reconstruct_digits(s):
    count = [0]*10
    for letter in s:
        if letter == 'z': count[0] += 1
        if letter == 'w': count[2] += 1
        if letter == 'u': count[4] += 1
        if letter == 'x': count[6] += 1
        if letter == 'g': count[8] += 1
        if letter == 'o': count[1] += 1 # o is in one, zero and two. but zero, two are already counted.
        if letter == 'h': count[3] += 1 # h is in three and eight. but eight is already counted.
        if letter == 'f': count[5] += 1 # f is in five and four. but four is already counted.
        if letter == 's': count[7] += 1 # s is in seven and six. but six is already counted.
        if letter == 'i': count[9] += 1 # i is in nine, five and six. but five and six are already counted.
   
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