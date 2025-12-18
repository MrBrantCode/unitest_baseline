"""
QUESTION:
Implement the function `guess_word(guessed_word, random_word, attempts)` that takes in a partially completed word `guessed_word`, a randomly selected word `random_word`, and the number of `attempts` the player has. The function should allow the player to guess letters and update the `guessed_word` accordingly. If the guessed letter matches a letter in the `random_word`, it should be inserted into the `guessed_word` at the correct index. If the guessed letter does not match, the number of attempts should be decremented. The function should return the updated `guessed_word` after each guess. The input `guessed_word` will have the same length as the `random_word` and will contain underscores "_" in the positions of the unguessed letters.
"""

def guess_word(guessed_word: str, random_word: str, attempts: int, guess: str) -> str:
    """
    Updates the guessed_word based on the guessed letter.

    Args:
    guessed_word (str): The current state of the guessed word.
    random_word (str): The randomly selected word.
    attempts (int): The number of attempts left.
    guess (str): The guessed letter.

    Returns:
    str: The updated guessed_word.
    int: The updated number of attempts.
    """
    for char in range(len(random_word)):
        if guessed_word[char] == "_":
            if guess.upper() == random_word[char].upper():
                guessed_word = guessed_word[:char] + random_word[char] + guessed_word[char+1:]
            else:
                attempts -= 1
    return guessed_word, attempts