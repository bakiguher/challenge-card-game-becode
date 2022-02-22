from utils.player import Player
from utils.game import Board


"""
Create 4 player
"""


_pnames = ["Player 1", "Player 2", "Player 3", "Player 4"]
_names = input("Enter player names comma seperated:  ")


if len(_names) > 0:
    n = _names.split(",")
    for a in n:
        print(n.index(a))
        _pnames[n.index(a)] = a


p1 = Player(_pnames[0])
p2 = Player(_pnames[1])
p3 = Player(_pnames[2])
p4 = Player(_pnames[3])


_players = [p1, p2, p3, p4]

"""
Create the board and start the game
"""
game = Board(_players)
game.start_game()
