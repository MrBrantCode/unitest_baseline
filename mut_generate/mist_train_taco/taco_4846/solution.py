"""
QUESTION:
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:

word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
        For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).

Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].
 
Example :
Input: 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.

 
Constraints:

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] are English lowercase letters.
Each puzzles[i] doesn't contain repeated characters.
"""

from collections import defaultdict
from typing import List

def count_valid_words(words: List[str], puzzles: List[str]) -> List[int]:
    orda = ord('a')
    mask = defaultdict(int)
    
    # Create a bitmask for each word
    for w in words:
        m = 0
        for c in w:
            m |= 1 << ord(c) - orda
        mask[m] += 1
    
    res = []
    
    # Process each puzzle
    for p in puzzles:
        ones = []
        for c in p:
            ones.append(1 << ord(c) - orda)
        
        # Generate all possible valid masks for the puzzle
        valid = [ones[0]]
        for i in range(1, 7):
            valid.extend([ones[i] + v for v in valid])
        
        # Count the number of valid words for the current puzzle
        novw = 0
        for v in valid:
            if v in mask:
                novw += mask[v]
        
        res.append(novw)
    
    return res