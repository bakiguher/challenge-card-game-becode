from utils.player import Player
from utils.game import Board


"""
Create 4 player
"""

p1 = Player("Azra")
p2 = Player("Baki")
p3 = Player("Coni")
p4 = Player("Desta")


_players = [p1, p2, p3, p4]

"""
Create the board and start the game 
"""
game = Board(_players)
game.start_game()
