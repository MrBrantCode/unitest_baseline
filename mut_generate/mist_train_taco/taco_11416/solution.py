"""
QUESTION:
Abhi and his friends (Shanky,Anku and Pandey) love to play with strings. Abhi invented a simple game. He will give a string S to his friends. Shanky and Anku will play the game while Pandey is just a spectator. Shanky will traverse the string from beginning (left to right) while Anku will traverse from last (right to left). Both have to find the first character they encounter during their traversal,that appears only once in the entire string. Winner will be one whose character is alphabetically more superior(has higher ASCII value). When it is not possible to decide the winner by comparing their characters, Pandey will be the winner.

-----Input-----
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

Each test case contains a string S having only lowercase alphabets ( a..z ).

-----Output-----
For each test case, output a single line containing "SHANKY" if Shanky is the winner or "ANKU" if Anku is the winner or "PANDEY" if the winner is Pandey. Output your answer without quotes.

-----Constraints-----
- 1 ≤ T ≤ 100
- 1 < |S| ≤ 10^5

-----Example-----
Input:
3
google
breakraekb
aman

Output:
SHANKY
PANDEY
ANKU

-----Explanation-----
Example case 2. Both Shanky and Anku can not find any such character. Hence it is not possible to decide the winner between these two. So Pandey is the winner.
"""

def determine_winner(S: str) -> str:
    char_index_map = {}
    
    # Populate the dictionary with the first occurrence index of each character
    for index, char in enumerate(S):
        if char in char_index_map:
            char_index_map[char] = -1
        else:
            char_index_map[char] = index
    
    shanky_index = len(S)
    anku_index = -1
    
    # Determine the first unique character from the beginning and end
    for char, index in char_index_map.items():
        if index != -1:
            if index < shanky_index:
                shanky_index = index
            if index > anku_index:
                anku_index = index
    
    shanky_char = None
    anku_char = None
    
    # Get the characters corresponding to the indices found
    if shanky_index != len(S):
        shanky_char = S[shanky_index]
    if anku_index != -1:
        anku_char = S[anku_index]
    
    # Determine the winner based on the characters found
    if shanky_char is None and anku_char is None:
        return "PANDEY"
    elif shanky_char is None:
        return "ANKU"
    elif anku_char is None:
        return "SHANKY"
    else:
        if shanky_char > anku_char:
            return "SHANKY"
        elif anku_char > shanky_char:
            return "ANKU"
        else:
            return "PANDEY"