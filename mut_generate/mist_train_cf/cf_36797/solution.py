"""
QUESTION:
Create a function `guess_game(secret, max_attempts)` that simulates a guessing game. The function takes a secret word `secret` (string) and the maximum number of attempts `max_attempts` (integer) as input. The function should prompt the player to input their guesses, provide feedback on the correctness of each guess, and allow the player to continue guessing until they either guess the word correctly or exhaust all attempts. The function should return a message indicating whether the player has won or lost the game.
"""

def guess_game(secret, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        guess = input("Enter your guess: ")
        if guess == secret:
            return "Congratulations! You guessed the word correctly.\nYou won!"
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect guess. Attempts left: {max_attempts - attempts}")
    return "Sorry, you have exhausted all attempts. The secret word was: " + secret + "\nYou lost!"