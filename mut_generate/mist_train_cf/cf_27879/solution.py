"""
QUESTION:
Write a function `guess_pixels(image, k, guesses)` that simulates a game where a player guesses the values of k pixels in a given grayscale image. The function takes as input: 
- `image`, a 2D list of integers representing the grayscale image, where each element is in the range [0, 255].
- `k`, an integer representing the number of pixels the player will guess.
- `guesses`, a list of tuples, each containing the row and column indices of the pixels the player guesses, with a length equal to `k`.
The function should return an integer representing the total score achieved by the player, where the player earns a point for each correct guess.
"""

def guess_pixels(image, k, guesses):
    score = 0
    for guess in guesses:
        row, col = guess
        if 0 <= row < len(image) and 0 <= col < len(image[0]):
            if image[row][col] == 255:
                score += 1
    return score