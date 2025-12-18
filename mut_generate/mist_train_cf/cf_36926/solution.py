"""
QUESTION:
Write a function `vowel_game_score(s)` that takes a string `s` of lowercase English letters as input and returns the result of a vowel game between two players, Stuart and Kevin. The game's rules are as follows: a player earns 1 point for each occurrence of a substring in `s` that starts with a vowel and ends with a consonant, but since this is not possible to determine from the string alone, assume the score of a player is the sum of the lengths of all substrings that start with a vowel for Kevin or a consonant for Stuart. If Stuart wins, return "Stuart" followed by his score. If Kevin wins, return "Kevin" followed by his score. If the game is a draw, return "Draw".
"""

def vowel_game_score(s: str) -> str:
    vowels = "aeiou"
    stuart = 0
    kevin = 0
    length = len(s)

    for i in range(length):
        if s[i] in vowels:
            kevin += length - i
        else:
            stuart += length - i

    if stuart > kevin:
        return f"Stuart {stuart}"
    elif kevin > stuart:
        return f"Kevin {kevin}"
    else:
        return "Draw"