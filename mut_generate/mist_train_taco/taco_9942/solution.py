"""
QUESTION:
Consider a game, wherein the player has to guess a target word. All the player knows is the length of the target word.

To help them in their goal, the game will accept guesses, and return the number of letters that are in the correct position.

Write a method that, given the correct word and the player's guess, returns this number.

For example, here's a possible thought process for someone trying to guess the word "dog":

```cs
CountCorrectCharacters("dog", "car"); //0 (No letters are in the correct position)
CountCorrectCharacters("dog", "god"); //1 ("o")
CountCorrectCharacters("dog", "cog"); //2 ("o" and "g")
CountCorrectCharacters("dog", "cod"); //1 ("o")
CountCorrectCharacters("dog", "bog"); //2 ("o" and "g")
CountCorrectCharacters("dog", "dog"); //3 (Correct!)
```
```python
count_correct_characters("dog", "car"); #0 (No letters are in the correct position)
count_correct_characters("dog", "god"); #1 ("o")
count_correct_characters("dog", "cog"); #2 ("o" and "g")
count_correct_characters("dog", "cod"); #1 ("o")
count_correct_characters("dog", "bog"); #2 ("o" and "g")
count_correct_characters("dog", "dog"); #3 (Correct!)
```

The caller should ensure that the guessed word is always the same length as the correct word, but since it could cause problems if this were not the case, you need to check for this eventuality:

```cs
//Throw an InvalidOperationException if the two parameters are of different lengths.
```
```python
#Raise an exception if the two parameters are of different lengths.
```

You may assume, however, that the two parameters will always be in the same case.
"""

def count_correct_positions(correct_word: str, guess: str) -> int:
    """
    Counts the number of letters in the guessed word that are in the correct position compared to the target word.

    :param correct_word: The target word that the player is trying to guess.
    :param guess: The word that the player has guessed.
    :return: The number of letters in the guessed word that are in the correct position.
    :raises ValueError: If the lengths of `correct_word` and `guess` are different.
    """
    if len(correct_word) != len(guess):
        raise ValueError("The lengths of the correct word and the guessed word must be the same.")
    
    return sum(1 for correct_char, guess_char in zip(correct_word, guess) if correct_char == guess_char)