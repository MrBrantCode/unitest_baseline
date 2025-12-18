"""
QUESTION:
Implement the `getPlayersInRoom` method in the `GameManager` class, which takes a room name as a parameter and returns a list of player names currently in that room. The method should handle cases where the specified room is not found in the game map. The `GameManager` class has a `Players` list of `Player` objects, each with a `Name` and `Room`, and a `Map` object that can retrieve a room by its name. If the room is not found, return the string "Sala nao encontrada".
"""

def getPlayersInRoom(self, room):
    sala = self.Map.getRoom(room)
    if sala is None:
        return "Sala nao encontrada"
    playersNaSala = [player for player in self.Players if player.Room == room]
    return [player.Name for player in playersNaSala]