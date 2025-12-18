"""
QUESTION:
Implement the `check_same`, `check_letter`, and `check_finished` functions for a word guessing game. 

- The `check_same` function takes two parameters: `guess` and `output`. It checks if the `guess` is the same as the `output` and returns the `output`. 
- The `check_letter` function takes three parameters: `guess`, `word`, and `tries`. It checks if the `guess` is a single letter and if it is present in the `word`. If the `guess` is valid, it updates the game state by filling in the correct letter in the `output` and decreasing the `tries` if the letter is not in the `word`. It returns the updated `tries`.
- The `check_finished` function takes two parameters: `output` and `tries`. It checks if the game has been won (no more underscores in `output`) or lost (no more `tries` left) and returns `True` if the game is finished, `False` otherwise.

Restrictions: 
- The `output` is a list of characters representing the current state of the word.
- The `word` is a string representing the word to be guessed.
- The `tries` is an integer representing the number of attempts remaining.
- The `guess` is a string representing the player's current guess.
"""

def check_same(guess, output):
    if guess == output:
        return output
    else:
        return False

def check_letter(guess, word, output, tries):
    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    output[i] = guess
        else:
            tries -= 1
        return output, tries
    else:
        return output, tries

def check_finished(output, tries):
    if "_" not in output:
        return True
    elif tries == 0:
        return True
    return False