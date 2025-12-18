"""
QUESTION:
Implement the `handle_drawing_submission` function. This function takes two parameters: `request` (which contains the current user making the request and the drawing submitted by the user) and `game` (which contains the game information, including the players). 

In the function, check if the current user is the first player in the game. If so, update the `player` variable to represent the first player. Then set the `hasDrawed` flag for the player to indicate that the player has submitted a drawing. Finally, retrieve the drawing submitted by the player from the HTTP POST request.

Assume that the `Game` class has `player1` and `player2` attributes, and the `Player` class has `user` and `hasDrawed` attributes. The function should also handle the scenario where there may be only one player in the game or the current user is not part of the game.
"""

def handle_drawing_submission(request, game):
    if game.player2 and game.player2.user == request.user:
        player = game.player2
    elif game.player1 and game.player1.user == request.user:
        player = game.player1
    else:
        # Handle the scenario where the current user is not part of the game
        return "User is not a player in the game"

    player.hasDrawed = True
    drawing = request.POST.get('drawing', 0)

    # Further processing of the drawing submission
    # ...

    return "Drawing submitted successfully"