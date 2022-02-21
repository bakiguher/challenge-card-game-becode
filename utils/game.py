from card import Card
from player import Player, Deck
# A class called Board that contains:

# An attribute players that is a list of Player. It will contain all the players that are playing.
# An attribute turn_count that is an int.
# An attribute active_cards that will contain the last card played by each player.
# An attribute history_cards that will contain all the cards played since the start of the game, except for active_cards.
# A method start_game() that will:
# Start the game,
# Fill a Deck,
# Distribute the cards of the Deck to the players.
# Make each Player play() a Card, where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.
# At the end of each turn, print:
# The turn count.
# The list of active cards.
# The number of cards in the history_cards.


class Board:
    players: list[Player] = []
    turn_count: int = 0
    active_cards: list[Card] = []
    history_cards: list[Card] = []

    def __init__(self, players: list[Player]):
        self.players = players

    def start_game(self):
        # self.active_cards=deck
        a = Deck()
        a.fill_deck()
        a.shuffle()
        a.distrubute(self.players)
        self.active_cards = a

        for t in range(0, 13):
            print("________________")
            print("Turn: " + str(t+1))
            
            for k in self.players:
                k.play()

        # start thegame
        # fill a deck
        # distrubute
        # each player play
        pass


p1 = Player("Azra")
p2 = Player("Baki")
p3 = Player("Coni")
p4 = Player("Desta")


_players = [p1, p2, p3, p4]

a = Deck()
k = Board(_players)
k.start_game()


# a.fill_deck()
# a.shuffle()
# a.distrubute(_players)
