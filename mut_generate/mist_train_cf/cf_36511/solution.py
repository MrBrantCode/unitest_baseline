"""
QUESTION:
Create a function `resolved_nonflashed_winner(N, moves)` where `N` is an integer (1 <= N <= 100) representing the total numbers in the game, and `moves` is a list of strings representing the moves made by the players. Each string is of the form "P X", where P is the player's name ("A" or "B") and X is the number they want to mark or unmark. The function should return the name of the winner ("A" or "B") or "Tie" if the game ends in a tie.
"""

def resolved_nonflashed_winner(N, moves):
    marked_numbers = set()
    player_moves = {"A": [], "B": []}

    for move in moves:
        player, number = move.split()
        number = int(number)
        
        if number in marked_numbers:
            player_moves[player].remove(number)
            marked_numbers.remove(number)
        else:
            player_moves[player].append(number)
            marked_numbers.add(number)
        
        if len(marked_numbers) == N:
            return "A" if len(player_moves["A"]) > len(player_moves["B"]) else "B" if len(player_moves["B"]) > len(player_moves["A"]) else "Tie"
    
    return "Tie"  