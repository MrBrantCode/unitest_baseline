"""
QUESTION:
Given a sentence as a string S. Calculate difficulty of a given sentence. 
Difficulty of sentence is defined as 5*(number of hard words) + 3*(number of easy words). A word in the given string is considered hard if it has 4 consecutive consonants or number of consonants are more than number of vowels. Else the word is easy.
Note: uppercase and lowercase characters are same.
Example
Input:
S = "Difficulty of sentence"
Output:
13
Explanation:
2 hard words + 1 easy word
Example
Input:
S = "I am good"
Output:
9
Explanation:
3 easy words
Your task:
You don't have to read input or print anything. Your task is to complete the functioin calcDiff() which takes the string S as input and returns the difficulty of the sentence.
 
Expected Time Complexity : O(len(s)
Expected Auxilliary Space : O(1)
Constraints:
1<= length( S ) <= 105
"""

def calculate_sentence_difficulty(S: str) -> int:
    (h, e) = (0, 0)
    vowels = 'AEIOUaeiou'
    words = S.split()
    
    for word in words:
        consonants = ''
        vowel_chars = ''
        consecutive_consonants = 0
        
        for char in word:
            if char not in vowels:
                consonants += char
                consecutive_consonants += 1
                if consecutive_consonants >= 4:
                    break
            else:
                vowel_chars += char
                consecutive_consonants = 0
        
        if consecutive_consonants >= 4:
            h += 1
        elif len(consonants) > len(vowel_chars):
            h += 1
        else:
            e += 1
    
    return 5 * h + 3 * e