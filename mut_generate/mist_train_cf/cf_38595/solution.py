"""
QUESTION:
Implement a function `process_guess` that processes a player's guess in a game of Mastermind, handling the logic for incorrect guesses. The function should take the following parameters: `guess` (the current guess), `max_color` (the correct color for the current position), `q` (a deque representing the queue of guesses), `idx_guess` (the index of the current guess), `invalid_color_idx` (a set containing the indices of invalid colors), and `idx` (the index to be moved to the next position). The function should put the correct color back, add the new color to the queue, reset invalid colors, and move to the next index when the guess is incorrect.
"""

def process_guess(guess, max_color, q, idx_guess, invalid_color_idx, idx):
    # Put the old color back
    guess[idx] = max_color
    # Put the new color back into the queue
    q.appendleft(idx_guess)
    # Reset invalid colors
    invalid_color_idx.clear()
    # Move to next index
    return idx + 1