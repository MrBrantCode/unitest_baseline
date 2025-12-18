"""
QUESTION:
Implement a function named `rle_encode` that takes an array of distinct strings as input and returns the array with each string encoded using Run-length encoding (RLE) to minimize storage footprint. The input array contains strings only, and the function should return the encoded array of strings.
"""

def rle_encode(arr):
    rle_arr = []
    for word in arr:
        encoded = ""
        i = 0
        while i < len(word):
            count = 1
            while i + 1 < len(word) and word[i] == word[i+1]:
                i += 1
                count += 1
            encoded += "{}{}".format(word[i], count)
            i += 1
        rle_arr.append(encoded)
    return rle_arr