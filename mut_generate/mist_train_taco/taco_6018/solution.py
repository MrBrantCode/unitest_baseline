"""
QUESTION:
Lets play some Pong! 

![pong](http://gifimage.net/wp-content/uploads/2017/08/pong-gif-3.gif)

For those who don't know what Pong is, it is a simple arcade game where two players can move their paddles to hit a ball towards the opponent's side of the screen, gaining a point for each opponent's miss. You can read more about it [here](https://en.wikipedia.org/wiki/Pong).

___

# Task:

You must finish the `Pong` class. It has a constructor which accepts the `maximum score` a player can get throughout the game, and a method called `play`. This method determines whether the current player hit the ball or not, i.e. if the paddle is at the sufficient height to hit it back. There're 4 possible outcomes: player successfully hits the ball back, player misses the ball, player misses the ball **and his opponent reaches the maximum score winning the game**, either player tries to hit a ball despite the game being over. You can see the input and output description in detail below.

### "Play" method input:

* ball position - The Y coordinate of the ball
* player position - The Y coordinate of the centre(!) of the current player's paddle

### "Play" method output:

One of the following strings:

* `"Player X has hit the ball!"` - If the ball "hits" the paddle
* `"Player X has missed the ball!"` - If the ball is above/below the paddle
* `"Player X has won the game!"` - If one of the players has reached the maximum score
* `"Game Over!"` - If the game has ended but either player still hits the ball

### Important notes:

* Players take turns hitting the ball, always starting the game with the Player 1.
* The paddles are `7` pixels in height.
* The ball is `1` pixel in height.

___

## Example
"""

def play_pong(max_score, scores, current_player, ball_pos, player_pos):
    """
    Simulates a single play in a Pong game.

    Parameters:
    - max_score (int): The maximum score a player can achieve to win the game.
    - scores (dict): A dictionary with keys 1 and 2 representing the scores of Player 1 and Player 2.
    - current_player (int): The current player (1 or 2) who is attempting to hit the ball.
    - ball_pos (int): The Y coordinate of the ball.
    - player_pos (int): The Y coordinate of the center of the current player's paddle.

    Returns:
    - str: A string indicating the outcome of the play.
    """
    if any(score >= max_score for score in scores.values()):
        return 'Game Over!'
    
    if abs(ball_pos - player_pos) <= 3:
        return f'Player {current_player} has hit the ball!'
    else:
        scores[current_player] += 1
        if scores[current_player] == max_score:
            next_player = 2 if current_player == 1 else 1
            return f'Player {next_player} has won the game!'
        else:
            return f'Player {current_player} has missed the ball!'