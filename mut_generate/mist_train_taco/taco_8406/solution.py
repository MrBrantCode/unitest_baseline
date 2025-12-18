"""
QUESTION:
Daisy loves playing games with words. Recently, she has been playing the following Deletive Editing word game with Daniel.

Daisy picks a word, for example, "DETERMINED". On each game turn, Daniel calls out a letter, for example, 'E', and Daisy removes the first occurrence of this letter from the word, getting "DTERMINED". On the next turn, Daniel calls out a letter again, for example, 'D', and Daisy removes its first occurrence, getting "TERMINED". They continue with 'I', getting "TERMNED", with 'N', getting "TERMED", and with 'D', getting "TERME". Now, if Daniel calls out the letter 'E', Daisy gets "TRME", but there is no way she can get the word "TERM" if they start playing with the word "DETERMINED".

Daisy is curious if she can get the final word of her choice, starting from the given initial word, by playing this game for zero or more turns. Your task it help her to figure this out.


-----Input-----

The first line of the input contains an integer $n$ — the number of test cases ($1 \le n \le 10000$). The following $n$ lines contain test cases.

Each test case consists of two words $s$ and $t$ separated by a space. Each word consists of at least one and at most 30 uppercase English letters; $s$ is the Daisy's initial word for the game; $t$ is the final word that Daisy would like to get at the end of the game.


-----Output-----

Output $n$ lines to the output — a single line for each test case. Output "YES" if it is possible for Daisy to get from the initial word $s$ to the final word $t$ by playing the Deletive Editing game. Output "NO" otherwise.


-----Examples-----

Input
6
DETERMINED TRME
DETERMINED TERM
PSEUDOPSEUDOHYPOPARATHYROIDISM PEPA
DEINSTITUTIONALIZATION DONATION
CONTEST CODE
SOLUTION SOLUTION
Output
YES
NO
NO
YES
NO
YES


-----Note-----

None
"""

def can_transform_word(s: str, t: str) -> str:
    """
    Determines if the initial word `s` can be transformed into the target word `t`
    using the Deletive Editing game rules.

    Parameters:
    s (str): The initial word.
    t (str): The target word.

    Returns:
    str: "YES" if the transformation is possible, "NO" otherwise.
    """
    # Iterate over the initial word `s` from the end to the beginning
    for i in range(len(s) - 1, -1, -1):
        # Check if the target word `t` is empty or if the current character in `s`
        # is in `t` but not at the end of `t`
        if len(t) == 0 or (s[i] in t and t[-1] != s[i]):
            break
        # If the current character in `s` matches the last character in `t`,
        # remove the last character from `t`
        if s[i] in t and t[-1] == s[i]:
            t = t[:-1]
    
    # If `t` is empty, it means we have successfully transformed `s` into `t`
    if len(t) == 0:
        return 'YES'
    else:
        return 'NO'