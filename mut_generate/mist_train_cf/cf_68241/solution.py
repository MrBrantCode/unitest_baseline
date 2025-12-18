"""
QUESTION:
Write a function `numTilePossibilities` that takes a string `tiles` as input, where `tiles` consists of uppercase English letters and 1 <= tiles.length <= 7. The function should return the number of possible non-empty sequences of letters that can be made using the letters in `tiles`, with the following constraints:

- No sequence can have the same letter appear consecutively more than once.
- The sequence must start and end with the same letter.

Example inputs and outputs:
- Input: "AAB", Output: 2
- Input: "AAABBC", Output: 8
- Input: "V", Output: 1
"""

def numTilePossibilities(tiles: str) -> int:
    count = [0] * 26
    for ch in tiles:
        count[ord(ch)-ord('A')] += 1
        
    def countSequences(count, prev, first):
        total = 1 if prev == first and prev != '' else 0
        for i in range(26):
            if count[i] > 0 and chr(i+ord('A')) != prev:
                count[i] -= 1
                total += countSequences(count, chr(i+ord('A')), first if first else chr(i+ord('A')))
                count[i] += 1
        return total
            
    result = 0
    for i in range(26):
        if count[i] > 0:
            count[i] -= 1
            result += countSequences(count, chr(i+ord('A')), chr(i+ord('A')))
            count[i] += 1
            
    return result